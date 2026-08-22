from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import exact_compare, expression_payload, fraction_text, q
from .model import load_instance
from .oracle import primitive_triples, solve_exact_cap_oracle, triple_policy


DOCUMENT_SCHEMA = "jrp3.policy-portfolio.v3"
PORTFOLIO_SCHEMA = "jrp3.certified-policy-portfolio.v2"
DOCUMENT_PURPOSE = (
    "Frozen synthetic regression fixtures only; every fitted operational instance must "
    "regenerate and verify its own boundary-and-primitive candidate set."
)
PORTFOLIO_ROLE = (
    "frozen synthetic regression fixture only; do not transfer these policies to an "
    "operational instance"
)


def _resolved_package_path(root: Path, value: Any, *, name: str) -> Path:
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError(f"{name} must be a nonempty package-relative path")
    resolved_root = root.resolve()
    resolved = (resolved_root / value).resolve()
    if not resolved.is_relative_to(resolved_root):
        raise ValueError(f"{name} escapes the package root")
    if not resolved.is_file():
        raise ValueError(f"{name} does not resolve to a file")
    return resolved


def build_policy_portfolio(
    instance_path: str | Path,
    label: str,
    *,
    package_root: str | Path,
) -> dict[str, Any]:
    root = Path(package_root).resolve()
    instance_path = Path(instance_path).resolve()
    if not instance_path.is_relative_to(root):
        raise ValueError("instance_path must remain inside package_root")
    instance = load_instance(instance_path)
    result = solve_exact_cap_oracle(instance)
    tolerance = Fraction(1, 1_000_000)
    threshold = sp.simplify(result.best_cost.expression * (1 + q(tolerance)))
    if exact_compare(result.tail_lower_bound, threshold) <= 0:
        raise RuntimeError(
            "The certified tail does not exclude omitted primitive policies inside the "
            "registered portfolio tolerance"
        )

    policies: list[dict[str, Any]] = []
    excluded: list[tuple[str, sp.Expr]] = []
    for multipliers in primitive_triples(result.cutoff):
        policy = triple_policy(instance, multipliers)
        regret = sp.simplify(policy.cost.expression - result.best_cost.expression)
        relative_regret = sp.simplify(policy.cost.expression / result.best_cost.expression - 1)
        if exact_compare(relative_regret, q(tolerance)) <= 0:
            policies.append(
                {
                    "primitive_multipliers": list(multipliers),
                    "cost": policy.cost.to_dict(),
                    "absolute_regret": expression_payload(regret),
                    "relative_regret": expression_payload(relative_regret),
                    "inside_registered_relative_tolerance": True,
                    "scale_mode": "interior" if policy.interior else "cap",
                    "t": str(policy.t_expression),
                    "frequencies": [
                        str(sp.simplify(1 / (a_i * policy.t_expression)))
                        for a_i in multipliers
                    ],
                }
            )
        else:
            excluded.append((f"primitive triple {multipliers}", relative_regret))
    policies.sort(key=lambda entry: tuple(entry["primitive_multipliers"]))

    boundary_comparators: list[dict[str, Any]] = []
    boundary_policies: list[dict[str, Any]] = []
    boundary_specs: list[tuple[str, sp.Expr, dict[str, Any]]] = [
        (
            "pairwise-incommensurable closure",
            result.desynchronised.cost,
            {},
        )
    ]
    for pair_result in result.pair_results:
        boundary_specs.append(
            (
                f"one-pair closure {pair_result.pair}",
                pair_result.best_cost,
                {
                    "cutoff_R": pair_result.cutoff,
                    "optimal_reduced_pairs": [
                        [policy.p, policy.q] for policy in pair_result.policies
                    ],
                },
            )
        )
    for regime, cost, details in boundary_specs:
        relative_regret = sp.simplify(cost / result.best_cost.expression - 1)
        inside = exact_compare(relative_regret, q(tolerance)) <= 0
        record = {
            "regime": regime,
            "cost": expression_payload(cost),
            "relative_regret": expression_payload(relative_regret),
            "inside_registered_relative_tolerance": inside,
            **details,
        }
        boundary_comparators.append(record)
        if inside:
            boundary_policies.append(record)
        else:
            excluded.append((regime, relative_regret))

    minimum_excluded_regime, minimum_excluded_regret = excluded[0]
    for regime, regret in excluded[1:]:
        if exact_compare(regret, minimum_excluded_regret) < 0:
            minimum_excluded_regime, minimum_excluded_regret = regime, regret

    included_boundary_count = len(boundary_policies)
    excluded_boundary_count = len(boundary_comparators) - included_boundary_count
    included_triple_count = len(policies)
    excluded_triple_count = result.enumerated_triples - included_triple_count
    return {
        "schema": PORTFOLIO_SCHEMA,
        "portfolio_role": PORTFOLIO_ROLE,
        "label": label,
        "instance": instance_path.relative_to(root).as_posix(),
        "instance_sha256": hashlib.sha256(instance_path.read_bytes()).hexdigest(),
        "registered_relative_cost_tolerance": fraction_text(tolerance),
        "registered_relative_cost_tolerance_percent": "0.0001%",
        "winner": list(result.policies[0].multipliers),
        "optimal_policies": [list(policy.multipliers) for policy in result.policies],
        "completeness_certificate": {
            "candidate_classes": [
                "fully commensurable primitive triples",
                "three one-pair closure regimes",
                "pairwise-incommensurable closure",
                "omitted primitive-triple tail",
            ],
            "primitive_cutoff_S": result.cutoff,
            "enumerated_primitive_triples": result.enumerated_triples,
            "included_primitive_triple_count": included_triple_count,
            "excluded_primitive_triple_count": excluded_triple_count,
            "included_boundary_policy_count": included_boundary_count,
            "excluded_boundary_policy_count": excluded_boundary_count,
            "included_policy_count": included_triple_count + included_boundary_count,
            "excluded_finite_policy_count": excluded_triple_count + excluded_boundary_count,
            "minimum_excluded_relative_regret": expression_payload(minimum_excluded_regret),
            "minimum_excluded_regime": minimum_excluded_regime,
            "tail_lower_bound": expression_payload(result.tail_lower_bound),
            "portfolio_cost_threshold": expression_payload(threshold),
            "tail_excludes_all_omitted_primitive_policies_within_tolerance": True,
            "all_boundary_regimes_classified": True,
            "boundary_comparators": boundary_comparators,
        },
        "primitive_triple_policies": policies,
        "boundary_policies": boundary_policies,
    }


def build_portfolio_document(portfolios: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema": DOCUMENT_SCHEMA,
        "purpose": DOCUMENT_PURPOSE,
        "portfolios": portfolios,
    }


def verify_policy_portfolio_document(
    path: str | Path,
    *,
    package_root: str | Path | None = None,
) -> dict[str, Any]:
    path = Path(path)
    root = Path(package_root).resolve() if package_root is not None else path.resolve().parents[1]
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or set(payload) != {"schema", "purpose", "portfolios"}:
        raise ValueError("portfolio document has an invalid top-level shape")
    if payload["schema"] != DOCUMENT_SCHEMA or payload["purpose"] != DOCUMENT_PURPOSE:
        raise ValueError("portfolio document contract mismatch")
    if not isinstance(payload["portfolios"], list) or not payload["portfolios"]:
        raise ValueError("portfolio document must contain at least one portfolio")

    checks: list[dict[str, Any]] = []
    seen_instances: set[str] = set()
    for index, observed in enumerate(payload["portfolios"]):
        if not isinstance(observed, dict):
            raise TypeError(f"portfolios[{index}] must be an object")
        instance_token = observed.get("instance")
        if instance_token in seen_instances:
            raise ValueError(f"duplicate portfolio instance: {instance_token}")
        seen_instances.add(instance_token)
        instance_path = _resolved_package_path(root, instance_token, name=f"portfolios[{index}].instance")
        if not isinstance(observed.get("label"), str) or not observed["label"]:
            raise ValueError(f"portfolios[{index}].label must be nonempty")
        expected = build_policy_portfolio(
            instance_path,
            observed["label"],
            package_root=root,
        )
        if observed != expected:
            raise AssertionError(f"portfolios[{index}] does not match complete recomputation")
        completeness = expected["completeness_certificate"]
        checks.append(
            {
                "instance": instance_token,
                "passed": True,
                "enumerated_primitive_triples": completeness["enumerated_primitive_triples"],
                "included_policy_count": completeness["included_policy_count"],
                "excluded_finite_policy_count": completeness["excluded_finite_policy_count"],
                "boundary_regimes": len(completeness["boundary_comparators"]),
                "tail_closed": completeness[
                    "tail_excludes_all_omitted_primitive_policies_within_tolerance"
                ],
            }
        )
    return {
        "schema": "jrp3.policy-portfolio-verification.v1",
        "portfolio_document": path.name,
        "passed": True,
        "portfolio_count": len(checks),
        "checks": checks,
    }
