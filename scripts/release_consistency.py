#!/usr/bin/env python3
"""Validate release-wide facts and assurance wording before replay or publication."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.3.1-candidate"
TITLE = (
    "A Candidate Exact Three-Item Independent-Cap Oracle: "
    "A Certified Rational Relaxation-Gap Lower Bound and Logistics Handoff"
)

CURRENT_SURFACES = (
    "README.md",
    "STATUS.md",
    "RELEASE_DECISION.md",
    "RESEARCH_EXTENSION_REPORT.md",
    "AI_INDEX.md",
    "narration.txt",
    "paper/three_item_jrp_gap_and_logistics.md",
    "CITATION.cff",
    "results.json",
    "reproduction_summary.json",
    "REPLAY_RECEIPT.json",
    "CLAIMS.json",
    "site/INTEGRATION.md",
    "site/WORK_LEDGER_RECORD.draft.json",
    "site/METHOD_LINEAGE_RECORD.draft.json",
    "site/papers/certified-three-item-jrp-gap/meta.draft.json",
    "site/papers/certified-three-item-jrp-gap/body.md",
)

BANNED_CURRENT_PATTERNS = {
    "retired predecessor-interval metric": re.compile(
        r"42\.670(?:8|9)|predecessor_interval_reduction", re.IGNORECASE
    ),
    "frozen-policy operational transfer": re.compile(
        r"five-policy logistics|carry (?:the )?(?:small |fixed )?portfolio|"
        r"use (?:the )?five-policy portfolio|operational handoff.*five", re.IGNORECASE
    ),
    "workstation-specific path": re.compile(r"/Users/"),
    "overstated independent verification": re.compile(
        r"\bindependently verified\b|\bindependent verifier\b", re.IGNORECASE
    ),
}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def load_json(relative: str) -> dict:
    return json.loads(read(relative))


def test_count() -> int:
    suite = unittest.defaultTestLoader.discover(str(ROOT / "tests"))
    return suite.countTestCases()


def detect_stage(cff: str) -> str:
    has_own_doi = bool(re.search(r"^doi:\s*['\"]?10\.", cff, re.MULTILINE))
    return "published" if has_own_doi else "candidate"


def check(stage: str, *, allow_unsealed: bool = False) -> list[str]:
    errors: list[str] = []
    cff = read("CITATION.cff")
    observed_stage = detect_stage(cff)
    if stage == "auto":
        stage = observed_stage

    if f"version: {VERSION}" not in cff:
        errors.append(f"CITATION.cff must declare version {VERSION}")
    if f'title: "{TITLE}"' not in cff:
        errors.append("CITATION.cff title does not match the canonical title")

    has_release_date = bool(re.search(r"^date-released:", cff, re.MULTILINE))
    if stage == "candidate" and has_release_date:
        errors.append("candidate-stage CITATION.cff must not claim date-released")
    if stage == "published":
        if not has_release_date:
            errors.append("published-stage CITATION.cff must declare date-released")
        for field in ("doi:", "repository-code:", "url:"):
            if not re.search(rf"^{re.escape(field)}", cff, re.MULTILINE):
                errors.append(f"published-stage CITATION.cff is missing {field}")

    unsealed_surfaces = {"STATUS.md", "reproduction_summary.json", "REPLAY_RECEIPT.json"}
    surfaces = (
        relative
        for relative in CURRENT_SURFACES
        if not allow_unsealed or relative not in unsealed_surfaces
    )
    combined = "\n".join(f"--- {relative} ---\n{read(relative)}" for relative in surfaces)
    for label, pattern in BANNED_CURRENT_PATTERNS.items():
        match = pattern.search(combined)
        if match:
            errors.append(f"{label}: found {match.group(0)!r}")

    count = test_count()
    if count != 21:
        errors.append(f"deterministic test inventory changed: expected 21, observed {count}")
    count_surfaces = ["README.md"]
    if not allow_unsealed:
        count_surfaces.extend(("STATUS.md", "reproduction_summary.json", "REPLAY_RECEIPT.json"))
    for relative in count_surfaces:
        text = read(relative)
        if not re.search(r"(?:tests[\"']?\s*[:=]\s*|)(?:21-test|21 tests|\"tests\"\s*:\s*21)", text):
            errors.append(f"{relative} does not expose the canonical 21-test count")
        if re.search(r"(?:15|19)[ -]tests|\"tests\"\s*:\s*(?:15|19)", text):
            errors.append(f"{relative} retains a stale test count")

    results = load_json("results.json")
    if results.get("schema") != "jrp3.result-summary.v2":
        errors.append("results.json has an unexpected schema")
    if results.get("status") not in {
        "anonymous_unrefereed_prepare_only_candidate",
        "anonymous_unrefereed_public_candidate",
    }:
        errors.append("results.json has an unexpected release status")

    portfolio = load_json("analysis/policy_portfolio.json")
    portfolio_report = load_json("analysis/policy_portfolio.verification.json")
    if portfolio.get("schema") != "jrp3.policy-portfolio.v3":
        errors.append("policy portfolio schema is not v3")
    if portfolio_report.get("schema") != "jrp3.policy-portfolio-verification.v1":
        errors.append("policy portfolio verification schema is missing")
    if portfolio_report.get("passed") is not True:
        errors.append("policy portfolio verification report did not pass")

    if not allow_unsealed and not (ROOT / "reviews/confirmation/DETERMINISTIC_REPAIR_CLOSURE.md").exists():
        errors.append("Editor-only deterministic repair closure is missing")
    if not (ROOT / "reviews/round-1/REVIEW_RECORD.json").exists():
        errors.append("round-one review record is missing")

    round_one = load_json("reviews/round-1/REVIEW_RECORD.json")
    decision_path = ROOT / "reviews/round-1" / round_one["editorial_decision"]["decision_file"]
    if not decision_path.is_file():
        errors.append("round-one editorial-decision path is not package-resolvable")
    policy = round_one["approval_standard"]
    policy_path = ROOT / "reviews/round-1" / policy["policy"]
    if not policy_path.is_file():
        errors.append("editorial approval policy is not package-resolvable")
    else:
        import hashlib

        observed = hashlib.sha256(policy_path.read_bytes()).hexdigest()
        if observed != policy["policy_sha256"]:
            errors.append("bundled editorial approval policy hash does not match the review record")

    state = load_json("PUBLICATION_STATE.json")
    reports = state.get("reviewPolicy", {}).get("roleReports", [])
    if len(reports) != 5:
        errors.append("publication state must bind all five confirmation role reports")
    for report in reports:
        report_path = ROOT / report["path"]
        if not report_path.is_file():
            errors.append(f"missing bound role report: {report['path']}")
    response_matrix = ROOT / state.get("reviewPolicy", {}).get("responseMatrix", "")
    if not response_matrix.is_file():
        errors.append("publication-state response matrix is not package-resolvable")
    elif re.search(r"\|\s*pending\s*\|", response_matrix.read_text(encoding="utf-8"), re.IGNORECASE):
        errors.append("response matrix retains a pending template row")

    for certificate in sorted((ROOT / "certificates").glob("*.certificate.json")):
        payload = json.loads(certificate.read_text(encoding="utf-8"))
        if payload.get("schema") == "jrp3.cap-oracle-certificate.v2":
            if payload.get("candidate_global_optimum_under_stated_proof") is not True:
                errors.append(f"{certificate.name} lacks the candidate proof-bound flag")
            if "certified_global_optimum" in payload:
                errors.append(f"{certificate.name} retains the retired assurance flag")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=("auto", "candidate", "published"), default="auto")
    parser.add_argument(
        "--allow-unsealed",
        action="store_true",
        help="check static release surfaces during replay before final receipts and Editor closure are sealed",
    )
    args = parser.parse_args()
    errors = check(args.stage, allow_unsealed=args.allow_unsealed)
    if errors:
        print("RELEASE CONSISTENCY FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("RELEASE CONSISTENCY PASS: 21 tests, portfolio v3, current facts aligned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
