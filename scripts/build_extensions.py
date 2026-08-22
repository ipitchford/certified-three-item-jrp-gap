from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

import sympy as sp

from jrp3.algebra import decimal_text, exact_compare, expression_payload, fraction_text, q
from jrp3.extensions import (
    ACTIVE_RUNNERS,
    ROBUSTNESS_SCHEMA,
    WINNER,
    active_envelope_holdings,
    active_runner_cost,
    active_runner_radius,
    crossover_polynomial,
    holding_box_instance,
    holding_box_vertices,
    verify_holding_box_certificate,
)
from jrp3.model import CapInstance, load_instance
from jrp3.oracle import solve_exact_cap_oracle, triple_policy
from jrp3.portfolio import (
    build_policy_portfolio,
    build_portfolio_document,
    verify_policy_portfolio_document,
)
from jrp3.contracts import certificate_conclusion
from jrp3.verify import verify_certificate


ROOT = Path(__file__).resolve().parents[1]
GAMMA_UPPER = "1111889593940297/1000000000000000"
ACTIVE_PATH = ROOT / "data" / "active_envelope_three_item_gap_witness.json"
PRIOR_PATH = ROOT / "data" / "near_extremal_three_item_gap_witness.json"
STATIONARY_POLYNOMIAL = sp.Poly(
    "1800*y**22 - 20160*y**21 + 62586*y**20 + 83856*y**19 "
    "- 1007010*y**18 + 2524002*y**17 - 1393873*y**16 - 8014582*y**15 "
    "+ 27527650*y**14 - 49265226*y**13 + 58778589*y**12 - 47482598*y**11 "
    "+ 22570946*y**10 - 1147794*y**9 - 6560485*y**8 + 4306350*y**7 "
    "- 735394*y**6 - 432534*y**5 + 223453*y**4 - 6530*y**3 "
    "- 14120*y**2 + 1200*y + 450",
    sp.Symbol("y"),
)
STATIONARY_INTERVAL = (Fraction(1_918_287_599, 2_500_000_000), Fraction(7_673_150_397, 10_000_000_000))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_oracle_certificate(instance_path: Path, certificate_path: Path) -> dict:
    instance = load_instance(instance_path)
    result = solve_exact_cap_oracle(instance)
    if not result.certified:
        raise RuntimeError(f"Instance did not certify: {instance_path}")
    payload = result.to_dict()
    payload["instance_sha256"] = hashlib.sha256(instance_path.read_bytes()).hexdigest()
    payload["two_item_gamma_upper_bound_used_for_comparison"] = GAMMA_UPPER
    payload["conclusion"] = certificate_conclusion(
        payload["integrality_gap"]["expression"]
    )
    write_json(certificate_path, payload)
    return payload


def active_analysis() -> dict:
    active = load_instance(ACTIVE_PATH)
    prior = load_instance(PRIOR_PATH)
    x, y = active.items[0].cap, active.items[1].cap
    if tuple(item.H for item in active.items) != active_envelope_holdings(y):
        raise AssertionError("active-envelope holdings")
    runner_cost = active_runner_cost(y)
    result = solve_exact_cap_oracle(active)
    prior_result = solve_exact_cap_oracle(prior)
    policies = []
    for multipliers in (WINNER,) + ACTIVE_RUNNERS:
        policy = triple_policy(active, multipliers)
        if policy.cost.kind != "rational":
            raise AssertionError(f"active policy {multipliers} is not rational")
        policies.append(
            {
                "primitive_multipliers": list(multipliers),
                "cost": policy.cost.to_dict(),
                "absolute_regret_from_winner": expression_payload(
                    sp.simplify(policy.cost.expression - result.best_cost.expression)
                ),
                "relative_regret_from_winner": expression_payload(
                    sp.simplify(policy.cost.expression / result.best_cost.expression - 1)
                ),
                "scale_mode": "interior" if policy.interior else "cap",
                "t": str(policy.t_expression),
            }
        )
    if any(triple_policy(active, a).cost.value != runner_cost for a in ACTIVE_RUNNERS):
        raise AssertionError("four-runner equality")
    if crossover_polynomial(x, y) <= 0:
        raise AssertionError("rational x must lie on the winner side of the crossover")

    lower, upper = STATIONARY_INTERVAL
    root_count = STATIONARY_POLYNOMIAL.count_roots(q(lower), q(upper))
    if root_count != 1:
        raise AssertionError("stationary root isolation")
    numerical_roots = [
        root
        for root in sp.nroots(STATIONARY_POLYNOMIAL, n=70, maxsteps=300)
        if abs(sp.im(root)) < sp.Rational(1, 10) ** 50
        and float(lower) < float(sp.re(root)) < float(upper)
    ]
    if len(numerical_roots) != 1:
        raise AssertionError("stationary numerical root")
    y_star = sp.re(numerical_roots[0])
    y_symbol = STATIONARY_POLYNOMIAL.gens[0]
    h1_symbol = sp.Rational(2, 3) * y_symbol**2
    h3_symbol = -(4 * y_symbol**3 - 7 * y_symbol**2 + 7 * y_symbol - 2) / (3 * (y_symbol - 1))
    runner_symbol = (3 * y_symbol**2 - 5) / (3 * (y_symbol - 1))
    d_symbol = (3 * h1_symbol + 2 + 2 * h3_symbol) / 3
    x_star = sp.simplify((runner_symbol - sp.sqrt(runner_symbol**2 - 8 * d_symbol)) / 4).subs(y_symbol, y_star)
    relaxation_star = (1 + h1_symbol / sp.Symbol("x") + sp.Rational(2, 3) / y_symbol + h3_symbol).subs(
        {y_symbol: y_star, sp.Symbol("x"): x_star}
    )
    ratio_star = runner_symbol.subs(y_symbol, y_star) / relaxation_star

    improvement = sp.simplify(result.gap - prior_result.gap)
    runner_margin = sp.simplify(q(runner_cost) - result.best_cost.expression)
    return {
        "schema": "jrp3.active-envelope-analysis.v1",
        "status": "producer-side exact derivation plus numerical stationary guide",
        "family": {
            "parameter": "y = item-2 frequency cap",
            "H1": "2*y^2/3",
            "H2": "2/3",
            "H3": "-(4*y^3 - 7*y^2 + 7*y - 2)/(3*(y - 1))",
            "four_runner_common_cost": "(3*y^2 - 5)/(3*(y - 1))",
            "winner_runner_crossover_polynomial": (
                "18*x^2*y - 18*x^2 - 9*x*y^2 + 15*x - 2*y^3 + 8*y^2 - 8*y - 2"
            ),
        },
        "rational_witness": {
            "x": fraction_text(x),
            "y": fraction_text(y),
            "crossover_polynomial_value": fraction_text(crossover_polynomial(x, y)),
            "winner": list(WINNER),
            "runner_cost": fraction_text(runner_cost),
            "runner_minus_winner": expression_payload(runner_margin),
            "relaxation": expression_payload(result.relaxation.cost),
            "true_optimum": result.best_cost.to_dict(),
            "gap": expression_payload(result.gap),
            "improvement_over_v0_2_witness": expression_payload(improvement),
            "policies": policies,
        },
        "stationary_guide": {
            "claim_boundary": (
                "This isolates a stationary point of the five-policy active family; it is not a proof "
                "of the exact three-item gap constant."
            ),
            "elimination_polynomial": str(STATIONARY_POLYNOMIAL.as_expr()),
            "isolating_interval": [fraction_text(lower), fraction_text(upper)],
            "root_count": int(root_count),
            "y_decimal": decimal_text(y_star, 60),
            "x_decimal": decimal_text(x_star, 60),
            "ratio_decimal": decimal_text(ratio_star, 60),
        },
    }


def policy_portfolio(instance_path: Path, label: str) -> dict:
    return build_policy_portfolio(instance_path, label, package_root=ROOT)


def write_instance(path: Path, instance: CapInstance) -> None:
    write_json(path, instance.to_dict())


def build_holding_box(base_path: Path, slug: str) -> tuple[Path, Path]:
    base = load_instance(base_path)
    base_result = solve_exact_cap_oracle(base)
    rho, active_thresholds = active_runner_radius(base)
    vertex_entries = []
    vertex_gaps = []
    for signs in holding_box_vertices():
        code = "".join("p" if sign > 0 else "m" for sign in signs)
        vertex = holding_box_instance(base, rho, signs)
        instance_path = ROOT / "data" / "robustness" / slug / f"vertex-{code}.json"
        certificate_path = ROOT / "certificates" / "robustness" / slug / f"vertex-{code}.certificate.json"
        verification_path = ROOT / "certificates" / "robustness" / slug / f"vertex-{code}.verification.json"
        write_instance(instance_path, vertex)
        certificate = build_oracle_certificate(instance_path, certificate_path)
        report = verify_certificate(certificate_path, instance_path=instance_path)
        write_json(verification_path, report)
        policies = [tuple(item["primitive_multipliers"]) for item in certificate["optimal_triple_policies"]]
        if policies != [WINNER]:
            raise AssertionError(f"holding vertex {slug}/{code} changes the winner: {policies}")
        vertex_gaps.append(q(Fraction(certificate["integrality_gap"]["rational"])))
        vertex_entries.append(
            {
                "signs": list(signs),
                "instance": str(instance_path.relative_to(ROOT)),
                "certificate": str(certificate_path.relative_to(ROOT)),
                "verification": str(verification_path.relative_to(ROOT)),
                "gap": certificate["integrality_gap"],
            }
        )
    minimum_gap = vertex_gaps[0]
    maximum_gap = vertex_gaps[0]
    for gap in vertex_gaps[1:]:
        if exact_compare(gap, minimum_gap) < 0:
            minimum_gap = gap
        if exact_compare(gap, maximum_gap) > 0:
            maximum_gap = gap
    certificate_path = ROOT / "certificates" / f"{slug}.holding_box.certificate.json"
    verification_path = ROOT / "certificates" / f"{slug}.holding_box.verification.json"
    payload = {
        "schema": ROBUSTNESS_SCHEMA,
        "scope": "simultaneous relative perturbations of all three holding coefficients",
        "base_instance": str(base_path.relative_to(ROOT)),
        "base_instance_sha256": hashlib.sha256(base_path.read_bytes()).hexdigest(),
        "base_gap": expression_payload(base_result.gap),
        "winner": list(WINNER),
        "relative_holding_radius": fraction_text(rho),
        "relative_holding_radius_decimal": decimal_text(q(rho), 30),
        "holding_intervals": [
            {
                "item": item.name,
                "lower": fraction_text(item.H * (1 - rho)),
                "upper": fraction_text(item.H * (1 + rho)),
            }
            for item in base.items
        ],
        "radius_construction": {
            "rule": "one half of the smallest active-runner relative-box crossover threshold",
            "active_runner_thresholds": active_thresholds,
        },
        "vertices": vertex_entries,
        "vertex_gap_range": {
            "minimum": expression_payload(minimum_gap),
            "maximum": expression_payload(maximum_gap),
        },
        "proof": {
            "schedule_affinity": (
                "For every fixed feasible schedule, the exact objective is affine in H."
            ),
            "winner_affinity": (
                "The (3,3,2) winner is cap-bound at every vertex, so the same fixed schedule and its "
                "affine cost apply throughout the box."
            ),
            "vertex_principle": (
                "For every competing fixed schedule, competitor cost minus winner cost is affine. Exact "
                "global optimality at all eight vertices makes that difference nonnegative at every vertex, "
                "and therefore throughout their convex hull."
            ),
        },
        "conclusion": (
            "The (3,3,2) policy is globally optimal throughout the declared holding-cost box, conditional "
            "on the candidate finite-closure theorem and the producer-side vertex certificates."
        ),
        "does_not_establish": [
            "robustness to cap, demand, lead-time, service, or fixed-cost misspecification",
            "operational benefit",
            "independent reproduction",
        ],
    }
    write_json(certificate_path, payload)
    write_json(verification_path, verify_holding_box_certificate(certificate_path))
    return certificate_path, verification_path


def main() -> None:
    analysis_path = ROOT / "analysis" / "active_envelope_analysis.json"
    write_json(analysis_path, active_analysis())
    print(analysis_path)
    portfolio_path = ROOT / "analysis" / "policy_portfolio.json"
    write_json(
        portfolio_path,
        build_portfolio_document(
            [
                policy_portfolio(ACTIVE_PATH, "strongest active-envelope witness"),
                policy_portfolio(PRIOR_PATH, "less-fragile v0.2 witness"),
            ]
        ),
    )
    print(portfolio_path)
    portfolio_verification_path = ROOT / "analysis" / "policy_portfolio.verification.json"
    write_json(
        portfolio_verification_path,
        verify_policy_portfolio_document(portfolio_path, package_root=ROOT),
    )
    print(portfolio_verification_path)
    for base_path, slug in (
        (PRIOR_PATH, "near_extremal_three_item_gap_witness"),
        (ACTIVE_PATH, "active_envelope_three_item_gap_witness"),
    ):
        for output in build_holding_box(base_path, slug):
            print(output)


if __name__ == "__main__":
    main()
