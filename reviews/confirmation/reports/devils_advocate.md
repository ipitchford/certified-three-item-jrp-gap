# Devil's Advocate Confirmation Review

**Target:** `exact-three-item-jrp-applications-v0.3.1-candidate`  
**Review type:** one permitted internal Evidence Press confirmation review; journal-like editorial evidence, not external peer review  
**Recommendation:** **Major Revision / HOLD_FOR_REPAIR**  
**Confidence:** **5/5**

## Executive decision

The revision is substantially stronger than v0.3.0. In particular, the manuscript now gives a mathematically plausible, journal-readable totality chain; the ordinary and optimized 19-test suites pass; every one of the 123 manifest entries verifies; and the logistics protocol is much more disciplined. I did not find a demonstrated P0 contradiction in the exact three-item witness, the finite-generation/tail argument, the fixed-item-count monotonicity implication, or the holding-box convexity argument.

Release approval nevertheless remains unsupported. A direct negative control shows that the public verifier accepts a certificate whose displayed `true_optimum.expression` is false. The package also ships machine certificates that state an unqualified certified comparison to the two-item constant, a portfolio completeness claim that is not bound to the boundary regimes it records, the retired 42.6709% statistic, a stale v0.3.0/15-test public draft, an unreleased CFF date, and an incomplete/dangling review ledger. These are not presentation nits: they directly fail R2, R4, R6, R7, and R8 acceptance conditions.

The strongest evidence-based decision is therefore **Major Revision**, not Reject. Reject would overstate what this confirmation review established: the mathematical core survived the adversarial checks I could perform, and the release blockers appear repairable. The Evidence Press state should remain **HOLD_FOR_REPAIR**. No third routine model review should be inferred from this recommendation; repairs can be checked through deterministic gates and editor verification unless a separately justified information-gain proposition authorizes further scientific review.

## Scope and independence boundary

I read the frozen manuscript and PDF text, oracle note, source/priority records, all implementation modules and build scripts, tests, point and robustness certificates, verification reports, analysis artifacts, replay/manifest receipts, response letter, revision tracking, every round-one role report and editorial decision, logistics protocol, governance/release files, licensing files, README/assurance/status/claims files, and the bundled site draft. I did not inspect any confirmation-review report, communicate with another reviewer, modify the candidate, or treat same-producer replay as independent reproduction. The source check below was a targeted authoritative-record spot check, not a systematic novelty review.

## Freeze and deterministic receipts

All four hashes in `FROZEN_TARGET.md` matched before substantive review:

| Object | Expected and observed SHA-256 | Result |
|---|---|---|
| `frozen-submission.zip` | `b51486d01b7aaddfad108c10f8ddbc8aa4fdfe27e3dc27d040b64e6a649ecdf3` | PASS |
| `MANIFEST.sha256` | `fa5a3537a362cde4b154fbe69accc453bf813eacf19d73867b6085e60c507199` | PASS |
| manuscript Markdown | `4f5c2d29df62eca54b9f38d95505785acf84f88ef5cb5f4cb876cfbc16cfa6ee` | PASS |
| manuscript PDF | `87f990da25b3cdaa4dfec4c44456ab0840b70a3a3f9dd256e937e8e887a73985` | PASS |

Further read-only checks produced these receipts:

- `python3 scripts/manifest.py --check`: **123 files passed**.
- Ordinary Python: **19 tests passed** in approximately 71.0 seconds.
- `PYTHONOPTIMIZE=2`: **19 tests passed** in approximately 71.1 seconds.
- The selected hashes embedded in `REPLAY_RECEIPT.json` match their referenced artifacts.
- The 15-page PDF text preflight found no raw TeX leakage. `pdfinfo` reports an untagged PDF; the accessible Markdown source remains available.

These establish frozen-byte integrity and same-producer consistency only. They do not establish theorem correctness, verifier independence, priority, operational validity, or external peer review.

## New findings

### DA-C1 — P1: the verifier accepts a false displayed optimum expression

`src/jrp3/verify.py:227-236` requires and syntax-checks all of `true_optimum.kind`, `value`, and `expression`, but `src/jrp3/verify.py:535-537` reconstructs the declared optimum solely from `kind` and `value`. More generally, `_parse_expr` at lines 275-278 prefers `rational` and silently ignores `expression` whenever both exist. No equality check binds redundant exact representations (`expression`, `rational`, `value`, `decimal`, or `minimal_polynomial`).

The following read-only mutation changed only the visible optimum expression to the false value `1`:

```sh
jq '.true_optimum.expression="1"' certificates/three_item_gap_witness.certificate.json \
  | PYTHONPATH=src python3 -m jrp3.verify /dev/stdin \
      --instance data/three_item_gap_witness.json
```

The verifier exited successfully with `passed: true`, 49 successful checks, and recomputed optimum `4793/1035`. The existing mutation test at `tests/test_oracle.py:220-228` changes `value` and `expression` together, so it cannot expose this split-representation defect.

**Why release-blocking:** the package claims strict, load-bearing schema validation and corrupt-claim rejection. A human- and machine-visible mathematical field can be false while the verifier reports success. This is a direct R2/DA-M2 failure and also defeats R8's assurance that the shipped artifacts are coherent.

**Required repair:** either eliminate redundant mathematical representations or prove exact equality among every retained representation. Add one-field-at-a-time negative controls for every redundant field, including `true_optimum.expression` and each payload's `expression` versus `rational`.

### DA-C2 — P1: machine evidence overstates what the shared verifier certifies

Every point/vertex certificate generated by `scripts/build_witness_certificates.py:39` and `scripts/build_extensions.py:59` concludes that the exact three-item gap “exceeds the certified upper endpoint” for the exact two-item constant. The certificates also declare `certified_global_optimum: true`. In isolation, those machine artifacts do not state that:

1. globality depends on the candidate prose totality theorem;
2. the checker shares exact-algebra and parsing substrate with the producer;
3. the two-item endpoint is an unrefereed predecessor candidate; and
4. internal replay is not an unaffiliated rerun or independent implementation.

The paper and `ASSURANCE.md` usually preserve these qualifications, but the public certificate is itself load-bearing evidence and can circulate without them. DA-C1 further shows that its strict-validation claim is not presently true.

**Why release-blocking:** R2 and R4 required the assurance and candidate-status boundary to hold at every load-bearing layer, not only in prose surrounding the JSON.

**Required repair:** replace unqualified certificate conclusions with candidate-relative language; include explicit `proof_dependency`, `predecessor_status`, and `verification_independence` fields; and make the verifier test those exact labels. Do not use “certified” as a free-standing theorem-status upgrade.

### DA-C3 — P1: the portfolio completeness claim omits its boundary regimes from the verification obligation

`scripts/build_extensions.py:190-205` classifies only primitive triple policies into the registered portfolio. Lines 207-229 separately record the desynchronised and one-pair boundary regimes, but do not compare their regrets to the portfolio tolerance, include a qualifying boundary policy, or emit a checked boolean covering them. The tail boolean at lines 247-250 excludes omitted **triple-tail** policies, not all policy classes. Correspondingly, `tests/test_oracle.py:190-218` reconstructs primitive triples and checks the triple tail, but never asserts that every boundary comparator exceeds the threshold.

I found no actual near-tolerance boundary counterexample in the two frozen fixtures; the defect is the claimed machine binding, not current membership. R6 nevertheless explicitly required completeness across boundary and primitive policies.

The top-level artifact purpose at `scripts/build_extensions.py:361-365` still calls this an “Exact five-policy handoff for secondary operational evaluation,” while only each nested portfolio says it is a frozen synthetic regression fixture.

**Why release-blocking:** the package represents boundary-complete portfolio construction as verified when the test obligation stops before the boundary comparison. This leaves a real cherry-picking/transfer escape route.

**Required repair:** form one checked candidate universe containing all boundary and primitive policy classes; assert exact threshold membership for every class; record included/excluded counts by class; fail the build if any boundary comparator is within tolerance but absent; and make the top-level purpose fixture-specific.

### DA-C4 — P1: R4/R5/R8 repairs did not propagate through the shipped package

The response says the 42.6709% metric was removed “everywhere substantive” and all mutable identity/count facts were advanced to v0.3.1/19 tests. The frozen package contradicts that account:

- `results.json:50` still publishes `predecessor_interval_reduction_percent = 42.670888681117245671` without denominator, formula, or retired status.
- `RESEARCH_EXTENSION_REPORT.md:85-93` still presents “Reduction of the predecessor lower-to-upper interval: 42.6708886811%,” and lines 83/100 recommend the five-policy portfolio for logistics simulation/shadow evaluation.
- `site/papers/certified-three-item-jrp-gap/meta.draft.json:10,44,47` remains `0.3.0-candidate`, describes the v0.3 package, and says all **fifteen** tests passed.
- That public draft's abstract/key results still present a five-policy logistics handoff; `body.md:45` says the four-order-of-magnitude radius contrast is why “the right handoff is a five-policy portfolio.” This conflicts with instance-specific regeneration and drops the conservative-inner-`H`-only qualification.
- `CITATION.cff:6` still declares `date-released: 2026-08-22`, although the package is prepare-only and R8 specifically required removal or qualification until release.
- `README.md:59` embeds `/Users/admin/.agents/skills/.../pdf_tex_preflight.py`, a workstation-specific, noncanonical command that does not match the skill location used for this confirmation.

**Why release-blocking:** these are shipped claim, logistics, version, count, date, and reproducibility facts, not hidden scratch files. They directly reproduce the defects R4, R5, and R8 were meant to close.

**Required repair:** regenerate or remove all superseded site/results/extension artifacts from one canonical metadata source; remove the retired statistic or label it explicitly as retired/nonstandard with its formula; replace five-policy transfer with per-instance regeneration; clear the unreleased CFF date; and use a package-relative/preflight-discovery command.

### DA-C5 — P1: the append-only review/release ledger is incomplete and contains dangling references

The response claims an added response matrix and complete append-only ledger. In the frozen package:

- `reviews/round-1/REVIEW_RECORD.json:59` points to `editorial/EDITORIAL_DECISION_ROUND_1.md`, which does not exist; the decision is directly under `reviews/round-1/`.
- The same record names `EVIDENCE_PRESS_EDITORIAL_APPROVAL_STANDARD.md` at line 87, but that policy is not bundled or otherwise resolvable inside the package.
- `reviews/round-1/RESPONSE_MATRIX_TEMPLATE.md` is still a blank template rather than a completed matrix.
- `PUBLICATION_STATE.json:204,214-215` leaves `frozenSubmissionSha256` and `responseMatrix` null and `roleReports` empty despite recording the round-one decision.
- `RESPONSE_TO_REVIEWERS.md:11` calls the five coordinated internal role reports “independent reports.” Later assurance language corrects the external boundary, but “independently filed internal role reports” would be less inflationary.

**Why release-blocking:** R7 was a governance gate and R8 a package-integrity gate. A ledger that cannot resolve its decision/policy and omits its own reports/matrix cannot support release accountability.

**Required repair:** make every ledger path package-resolvable, bundle or immutably identify the governing policy, complete the response matrix, bind the frozen archive and reports by hash, populate the canonical state record, and use unambiguous internal-role language.

### DA-C6 — P2: predecessor creator metadata conflicts with the canonical immutable release page

`SOURCES.md`, `CITATION_AUDIT.md`, and `CITATION.cff` identify the v1.2.0 predecessor creator as `Anonymous`. The canonical Evidence Press predecessor page gives the citation as `Agent collective, & Pitchford, I.` while retaining v1.2.0-candidate status ([canonical predecessor page](https://evidencepress.org/releases/certified-two-item-jrp/)). Preserving `Anonymous` for the present manuscript does not authorize rewriting the immutable parent's creator metadata.

The wider source revisions are otherwise materially improved: targeted checks confirmed the cited 2026 preprint's `5/(6 ln 2)` result ([arXiv record](https://arxiv.org/abs/2603.18720)) and the publication status of the cited Segev article ([INFORMS record](https://pubsonline.informs.org/doi/abs/10.1287/moor.2024.0635)). I found no direct priority collision, but this spot check is not a systematic novelty finding.

**Required repair:** reproduce the parent release's authoritative creator/citation metadata exactly, or document an explicit, evidence-backed metadata correction without altering the immutable predecessor record.

### DA-C7 — P2: the exact-expression and file-reference attack surfaces remain unnecessarily broad

The “safe” grammar at `src/jrp3/verify.py:21,248-272` permits arbitrary repetition of `*`, including exponentiation, and imposes no input-length, exponent-size, nesting-depth, or evaluation-cost bound before `sympy.parse_expr`. That is a potential denial-of-service path for a verifier presented as accepting public certificate input. Separately, the holding-box verifier resolves certificate-supplied paths without an explicit package-root containment test; the frozen hashes constrain the shipped fixture but not arbitrary verifier input.

**Required repair:** parse a small explicit AST or canonical expression schema with resource limits, and require every certificate-resolved path to remain under a declared package root before opening it. Add adversarial size/depth and `..` path tests.

### DA-C8 — P3: PDF accessibility is not demonstrated

`pdfinfo` reports `Tagged: no`. The Markdown source mitigates access, and this does not affect the mathematics, but a public PDF accessibility claim should not be inferred from text extractability or producer-side visual inspection.

**Suggested repair:** generate a tagged PDF or state the accessible-source route and known PDF limitation.

## Required-revision trace: R1–R8

| ID | Status | Confirmation assessment |
|---|---|---|
| R1 | **Fully addressed** | The manuscript now defines the model/policy/constant scope and supplies explicit pair-tail, finite-generation, triple-tail, cap-restoration, totality, monotonicity, and robustness arguments. I found no finite-search counterexample or omitted asymptotic order. “Fully” here means the requested candidate-proof presentation is present; it is not external proof validation or formal verification. |
| R2 | **Partly addressed** | Unknown/missing-field handling, canonical identifiers, negative tests, and same-producer disclosure improved. DA-C1 proves inconsistent load-bearing representations can pass; DA-C2 shows the machine assurance layer is not self-calibrated; DA-C7 leaves parser/path attack surfaces. |
| R3 | **Partly addressed** | The bibliography, related-work table, dependency labels, and priority protocol are much improved, and targeted authoritative checks largely agree. DA-C6 leaves predecessor attribution inconsistent with its canonical release. Novelty remains appropriately partial, not established. |
| R4 | **Partly addressed** | The manuscript title, abstract, inner-radius language, active-guide boundary, and candidate wording are improved. DA-C2 and DA-C4 show unqualified certificate language, the retired 42.6709% statistic, and stale robustness/portfolio rhetoric remain in shipped artifacts. |
| R5 | **Partly addressed** | The paper/protocol now handle event ownership, marginal-event semantics, units, joint uncertainty, design adequacy, outcomes, stopping, and RACI well. The stale site/extension handoff in DA-C4 still transfers a frozen five-policy set into operational evaluation, so the repair is not package-wide. |
| R6 | **Partly addressed** | Exhaustive primitive-triple membership and tail exclusion are implemented. Boundary regimes are recorded but not threshold-checked or included in the test obligation (DA-C3), and transfer rhetoric remains (DA-C4). |
| R7 | **Partly addressed** | Disclosures, maintainer/correction accountability, funding/conflict/AI statements, licences, and role reports are present. The formal ledger has dangling paths, no completed response matrix, and an unpopulated canonical review state (DA-C5). |
| R8 | **Partly addressed** | Frozen hashes, 123-entry manifest, 19-test normal/optimized runs, selected receipt hashes, counts in the main paper, and PDF text preflight pass. The stale site version/count, CFF release date, absolute README path, retired result field, and broken governance references in DA-C4/C5 prevent whole-package reconciliation. |

## Devil's Advocate trace: DA-M1–DA-M7

| ID | Status | Confirmation assessment |
|---|---|---|
| DA-M1 | **Fully addressed** | A quantified totality proof is now in the manuscript and expanded oracle note. I did not find a totality counterexample. This remains a candidate proof, not an external theorem audit. |
| DA-M2 | **Partly addressed** | Shared substrate is disclosed and tests are broader, but the verifier accepts a false redundant expression (DA-C1) and machine certificates overstate their assurance boundary (DA-C2). |
| DA-M3 | **Fully addressed** | The event-closure alternatives—owned event, frozen-background/marginal-event treatment, or software-only exclusion—are explicit in the paper and protocol. |
| DA-M4 | **Partly addressed** | The manuscript correctly calls the radii conservative inner boxes for simultaneous relative `H` perturbation and lists fixed/omitted variables. The bundled site summary reverts to “complete holding-cost boxes” and transfers the radius contrast operationally (DA-C4). |
| DA-M5 | **Partly addressed** | Primitive-triple enumeration is no longer hand-picked and operational regeneration is specified in the main protocol. Boundary completeness is not actually verifier-bound and the package still contains frozen five-policy handoff language (DA-C3/C4). |
| DA-M6 | **Partly addressed** | The 42.6709% statistic was removed from the main manuscript's rhetoric, but remains an unlabeled shipped result and a highlighted extension-report bullet (DA-C4). |
| DA-M7 | **Fully addressed** | The main field protocol now distinguishes simulation, shadow, pilot, and scaling evidence; addresses assignment, interference, carryover, missingness, multiplicity, cost boundaries, RACI, and stopping; and does not claim savings or field validation. |

## Severity summary and release gate

| Severity | Count | Findings |
|---|---:|---|
| P0 | 0 | No demonstrated fatal mathematical contradiction or corrupted frozen target. |
| P1 | 5 | DA-C1 through DA-C5: verifier semantics, assurance inflation, portfolio binding, package reconciliation, and governance ledger. |
| P2 | 2 | DA-C6 source metadata; DA-C7 parser/path hardening. |
| P3 | 1 | DA-C8 PDF accessibility. |

Acceptance and Minor Revision are excluded by multiple independently release-blocking P1 groups. Reject is not supported because the core mathematical contribution remains plausible and the defects are specific and repairable. The correct confirmation outcome is:

> **MAJOR REVISION — HOLD_FOR_REPAIR (confidence 5/5).**

Before any release decision, require DA-C1–DA-C5 to be closed, rerun the ordinary/optimized suites plus the new one-field mutation and boundary-universe tests, regenerate the full package from one canonical metadata source, re-freeze all artifacts, and have the editor verify the resulting hashes and ledger without representing this internal confirmation as external peer review.
