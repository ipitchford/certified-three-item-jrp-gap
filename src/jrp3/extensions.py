from __future__ import annotations

from dataclasses import replace
from fractions import Fraction
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any, Iterable

from .algebra import fraction_text
from .model import CapInstance, CapItem, load_instance
from .oracle import triple_policy
from .verify import _canonical_identifier, verify_certificate


ROBUSTNESS_SCHEMA = "jrp3.holding-box-certificate.v1"
WINNER = (3, 3, 2)
ACTIVE_RUNNERS = ((2, 1, 1), (2, 2, 1), (3, 2, 2), (4, 3, 2))


def active_envelope_holdings(y: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    """Return the exact four-runner equalisation family at item-2 cap ``y``."""
    y = Fraction(y)
    if not 0 < y < 1:
        raise ValueError("The active-envelope parameter y must lie in (0, 1)")
    h1 = Fraction(2, 3) * y * y
    h2 = Fraction(2, 3)
    h3 = -(4 * y**3 - 7 * y**2 + 7 * y - 2) / (3 * (y - 1))
    if h3 <= 0:
        raise ValueError("The selected y does not give a positive third holding coefficient")
    return h1, h2, h3


def active_envelope_instance(name: str, x: Fraction, y: Fraction) -> CapInstance:
    """Construct a rational member of the five-policy active-envelope family."""
    h1, h2, h3 = active_envelope_holdings(y)
    return CapInstance(
        name=name,
        K0=Fraction(1),
        items=(
            CapItem("item-1", Fraction(0), h1, Fraction(x)),
            CapItem("item-2", Fraction(0), h2, Fraction(y)),
            CapItem("item-3", Fraction(0), h3, Fraction(1)),
        ),
    )


def active_runner_cost(y: Fraction) -> Fraction:
    """Common exact cost of the four runner policies on the envelope family."""
    y = Fraction(y)
    return (3 * y * y - 5) / (3 * (y - 1))


def crossover_polynomial(x: Fraction, y: Fraction) -> Fraction:
    """Cleared five-policy equality equation E(x,y); zero is the crossover."""
    x, y = Fraction(x), Fraction(y)
    return (
        18 * x * x * y
        - 18 * x * x
        - 9 * x * y * y
        + 15 * x
        - 2 * y**3
        + 8 * y * y
        - 8 * y
        - 2
    )


def policy_holding_slopes(instance: CapInstance, multipliers: tuple[int, int, int]) -> tuple[Fraction, Fraction, Fraction]:
    """Holding-cost slopes for a cap-bound fixed triple policy."""
    policy = triple_policy(instance, multipliers)
    if policy.interior or policy.cost.kind != "rational":
        raise ValueError(f"Policy {multipliers} is not cap-bound")
    return tuple(Fraction(a_i) * policy.t_min for a_i in multipliers)  # type: ignore[return-value]


def active_runner_radius(
    instance: CapInstance,
    *,
    safety: Fraction = Fraction(1, 2),
) -> tuple[Fraction, list[dict[str, Any]]]:
    """Choose a conservative relative holding box from the active halfspaces.

    At relative radius rho, item i varies by at most rho*H_i.  For a runner
    with base margin m and holding-slope difference d, the worst linear loss
    of margin is rho*sum_i |d_i|H_i.  Half the smallest exact threshold leaves
    a strict buffer at every vertex.  The global oracle later certifies every
    vertex; affinity then fills the whole box.
    """
    if not 0 < safety < 1:
        raise ValueError("safety must lie in (0, 1)")
    winner = triple_policy(instance, WINNER)
    if winner.cost.kind != "rational" or winner.interior:
        raise ValueError("The declared winner must be cap-bound")
    winner_slopes = policy_holding_slopes(instance, WINNER)
    thresholds: list[Fraction] = []
    records: list[dict[str, Any]] = []
    for multipliers in ACTIVE_RUNNERS:
        runner = triple_policy(instance, multipliers)
        if runner.cost.kind != "rational" or runner.interior:
            raise ValueError(f"Active runner {multipliers} must be cap-bound")
        margin = runner.cost.value - winner.cost.value
        if margin <= 0:
            raise ValueError(f"Active runner {multipliers} does not have positive margin")
        slopes = policy_holding_slopes(instance, multipliers)
        weighted_slope = sum(
            abs(runner_slope - winner_slope) * item.H
            for runner_slope, winner_slope, item in zip(slopes, winner_slopes, instance.items)
        )
        if weighted_slope <= 0:
            raise ValueError(f"Active runner {multipliers} has no holding sensitivity")
        threshold = margin / weighted_slope
        thresholds.append(threshold)
        records.append(
            {
                "primitive_multipliers": list(multipliers),
                "base_margin": fraction_text(margin),
                "base_margin_decimal": str(float(margin)),
                "relative_box_crossover_threshold": fraction_text(threshold),
                "holding_slope_difference": [
                    fraction_text(runner_slope - winner_slope)
                    for runner_slope, winner_slope in zip(slopes, winner_slopes)
                ],
            }
        )
    return safety * min(thresholds), records


def holding_box_instance(instance: CapInstance, rho: Fraction, signs: tuple[int, int, int]) -> CapInstance:
    if len(signs) != 3 or any(sign not in (-1, 1) for sign in signs):
        raise ValueError("signs must be a three-vector over {-1,+1}")
    rho = Fraction(rho)
    if not 0 < rho < 1:
        raise ValueError("rho must lie in (0, 1)")
    items = tuple(
        replace(item, H=item.H * (1 + sign * rho))
        for item, sign in zip(instance.items, signs)
    )
    return replace(instance, name=f"{instance.name}-holding-vertex-{'p' if signs[0] > 0 else 'm'}{'p' if signs[1] > 0 else 'm'}{'p' if signs[2] > 0 else 'm'}", items=items)


def holding_box_vertices() -> Iterable[tuple[int, int, int]]:
    return product((-1, 1), repeat=3)


def _instance_equal_ignoring_name(left: CapInstance, right: CapInstance) -> bool:
    return left.K0 == right.K0 and left.items == right.items and left.time_unit == right.time_unit and left.currency_unit == right.currency_unit


def _package_file(root: Path, token: Any, *, name: str) -> Path:
    if not isinstance(token, str) or not token or Path(token).is_absolute():
        raise ValueError(f"{name} must be a nonempty package-relative path")
    resolved_root = root.resolve()
    resolved = (resolved_root / token).resolve()
    if not resolved.is_relative_to(resolved_root):
        raise ValueError(f"{name} escapes the package root")
    if not resolved.is_file():
        raise ValueError(f"{name} does not resolve to a file")
    return resolved


def verify_holding_box_certificate(path: str | Path) -> dict[str, Any]:
    """Verify all exact vertex certificates and the affine-box conditions."""
    path = Path(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != ROBUSTNESS_SCHEMA:
        raise ValueError(f"Unsupported robustness schema: {payload.get('schema')!r}")
    root = path.resolve().parents[1]
    base_path = _package_file(root, payload["base_instance"], name="base_instance")
    base = load_instance(base_path)
    expected_hash = hashlib.sha256(base_path.read_bytes()).hexdigest()
    if payload.get("base_instance_sha256") != expected_hash:
        raise AssertionError("base_instance_sha256")
    rho = Fraction(payload["relative_holding_radius"])
    recomputed_rho, _ = active_runner_radius(base)
    if rho != recomputed_rho:
        raise AssertionError("relative_holding_radius")
    if tuple(payload.get("winner", ())) != WINNER:
        raise AssertionError("winner")

    declared = payload.get("vertices")
    if not isinstance(declared, list) or len(declared) != 8:
        raise AssertionError("eight vertices are required")
    expected_signs = set(holding_box_vertices())
    seen: set[tuple[int, int, int]] = set()
    checks: list[dict[str, Any]] = []
    for entry in declared:
        signs = tuple(int(value) for value in entry["signs"])
        if signs not in expected_signs or signs in seen:
            raise AssertionError(f"invalid or duplicate signs: {signs}")
        seen.add(signs)  # type: ignore[arg-type]
        instance_path = _package_file(root, entry["instance"], name="vertex.instance")
        certificate_path = _package_file(root, entry["certificate"], name="vertex.certificate")
        vertex = load_instance(instance_path)
        expected_vertex = holding_box_instance(base, rho, signs)  # type: ignore[arg-type]
        if not _instance_equal_ignoring_name(vertex, expected_vertex):
            raise AssertionError(f"vertex instance mismatch: {signs}")
        report = verify_certificate(certificate_path, instance_path=instance_path)
        certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
        policies = [tuple(item["primitive_multipliers"]) for item in certificate["optimal_triple_policies"]]
        if policies != [WINNER]:
            raise AssertionError(f"winner mismatch at {signs}: {policies}")
        winner = triple_policy(vertex, WINNER)
        if winner.interior or winner.cost.kind != "rational":
            raise AssertionError(f"winner is not affine at {signs}")
        checks.append(
            {
                "signs": list(signs),
                "vertex_certificate_passed": bool(report["passed"]),
                "winner_cap_bound": True,
                "integrality_gap": certificate["integrality_gap"],
            }
        )
    if seen != expected_signs:
        raise AssertionError("vertex set is incomplete")
    return {
        "schema": "jrp3.holding-box-verification.v1",
        "certificate": _canonical_identifier(path),
        "passed": True,
        "vertex_count": len(checks),
        "checks": checks,
        "conclusion": (
            "The declared policy is globally optimal throughout the holding-cost box: "
            "every fixed schedule cost is affine in H, the declared cap-bound winner is "
            "the same fixed schedule throughout the box, and all eight exact-oracle vertex "
            "certificates select that winner."
        ),
    }
