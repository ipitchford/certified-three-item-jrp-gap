from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import ScaleCost, exact_compare, q
from .contracts import (
    CERTIFICATE_SCHEMA,
    PREDECESSOR_STATUS,
    PROOF_DEPENDENCY,
    VERIFICATION_INDEPENDENCE,
    certificate_conclusion,
)
from .model import CapInstance, instance_from_dict, load_instance


EXPECTED_PAIRS = ((0, 1), (0, 2), (1, 2))
_RATIONAL_TEXT = re.compile(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?")
MAX_EXPRESSION_LENGTH = 4096
MAX_EXPRESSION_NODES = 256
MAX_INTEGER_DIGITS = 512
MAX_POLYNOMIAL_EXPONENT = 16


def _mapping(
    value: Any,
    *,
    name: str,
    required: set[str],
    allowed: set[str],
) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise TypeError(f"{name} must be an object")
    missing = sorted(required - set(value))
    if missing:
        raise ValueError(f"{name} is missing required fields: {', '.join(missing)}")
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ValueError(f"{name} has unknown fields: {', '.join(unknown)}")
    return value


def _list(value: Any, *, name: str, length: int | None = None) -> list[Any]:
    if not isinstance(value, list):
        raise TypeError(f"{name} must be an array")
    if length is not None and len(value) != length:
        raise ValueError(f"{name} must contain exactly {length} entries")
    return value


def _integer(value: Any, *, name: str, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


def _rational_text(value: Any, *, name: str) -> str:
    if not isinstance(value, str) or not _RATIONAL_TEXT.fullmatch(value):
        raise ValueError(f"{name} must be a canonical integer or rational string")
    Fraction(value)
    return value


def _validate_expression_payload(value: Any, *, name: str) -> dict[str, Any]:
    payload = _mapping(
        value,
        name=name,
        required={"expression"},
        allowed={"expression", "rational", "decimal", "minimal_polynomial", "kind", "value"},
    )
    expression = _parse_expression_text(payload["expression"], name=f"{name}.expression")
    exact_fields: list[tuple[str, sp.Expr]] = [("expression", expression)]
    if "rational" in payload:
        token = _rational_text(payload["rational"], name=f"{name}.rational")
        exact_fields.append(("rational", q(Fraction(token))))
    if "value" in payload:
        token = _rational_text(payload["value"], name=f"{name}.value")
        exact_fields.append(("value", q(Fraction(token))))
    for field, exact_value in exact_fields[1:]:
        if exact_compare(expression, exact_value) != 0:
            raise ValueError(f"{name}.{field} contradicts {name}.expression")
    if "decimal" in payload:
        _validate_decimal(payload["decimal"], expression, name=f"{name}.decimal")
    if "minimal_polynomial" in payload:
        polynomial = _parse_polynomial_text(
            payload["minimal_polynomial"], name=f"{name}.minimal_polynomial"
        )
        x = sp.Symbol("x")
        if exact_compare(sp.simplify(polynomial.as_expr().subs(x, expression)), sp.Integer(0)) != 0:
            raise ValueError(f"{name}.minimal_polynomial does not vanish at the expression")
    return payload


def _validate_certificate_schema(certificate: Any) -> dict[str, Any]:
    """Validate the complete load-bearing certificate shape before arithmetic.

    The certificate contains explanatory fields in addition to the proof
    objects.  Unknown fields are rejected at every object consumed by this
    verifier; explanatory component records remain opaque because they are not
    used to establish the certified optimum.
    """
    top_required = {
        "schema", "instance", "instance_sha256", "relaxation",
        "desynchronised_regime", "one_pair_oracles", "boundary_cost",
        "triple_cutoff_S", "component_bound", "tail_factor_squared",
        "enumerated_primitive_triples", "optimal_triple_policies",
        "true_optimum", "tail_lower_bound", "tail_minus_incumbent",
        "integrality_gap", "candidate_global_optimum_under_stated_proof",
        "proof_dependency", "predecessor_status", "verification_independence",
    }
    top_allowed = top_required | {
        "assurance", "conclusion", "enumeration_condition", "regimes",
        "scope", "tail_formula", "two_item_gamma_upper_bound_used_for_comparison",
    }
    certificate = _mapping(
        certificate,
        name="certificate",
        required=top_required,
        allowed=top_allowed,
    )
    if certificate["schema"] != CERTIFICATE_SCHEMA:
        raise ValueError(f"Unsupported certificate schema: {certificate['schema']!r}")
    expected_contract = {
        "proof_dependency": PROOF_DEPENDENCY,
        "predecessor_status": PREDECESSOR_STATUS,
        "verification_independence": VERIFICATION_INDEPENDENCE,
    }
    for field, expected in expected_contract.items():
        if certificate[field] != expected:
            raise ValueError(f"certificate.{field} does not match the v2 assurance contract")
    if not isinstance(certificate["instance_sha256"], str) or not re.fullmatch(
        r"[0-9a-f]{64}", certificate["instance_sha256"]
    ):
        raise ValueError("instance_sha256 must be a lowercase SHA-256 digest")
    instance_from_dict(certificate["instance"])

    relaxation = _mapping(
        certificate["relaxation"],
        name="relaxation",
        required={"cost", "frequencies"},
        allowed={"candidate_count", "cost", "frequencies", "max_frequency", "model"},
    )
    _validate_expression_payload(relaxation["cost"], name="relaxation.cost")
    frequencies = _list(relaxation["frequencies"], name="relaxation.frequencies", length=3)
    for index, token in enumerate(frequencies):
        _parse_expression_text(token, name=f"relaxation.frequencies[{index}]")

    desynchronised = _mapping(
        certificate["desynchronised_regime"],
        name="desynchronised_regime",
        required={"cost"},
        allowed={"components", "cost", "interpretation"},
    )
    _validate_expression_payload(desynchronised["cost"], name="desynchronised_regime.cost")

    pair_entries = _list(certificate["one_pair_oracles"], name="one_pair_oracles", length=3)
    declared_pairs: list[tuple[int, int]] = []
    for index, raw_entry in enumerate(pair_entries):
        name = f"one_pair_oracles[{index}]"
        entry = _mapping(
            raw_entry,
            name=name,
            required={
                "pair_indices", "cutoff_R", "enumerated_coprime_pairs",
                "optimal_policies", "best_cost", "tail_lower_bound",
                "tail_minus_incumbent", "certified",
            },
            allowed={
                "pair_indices", "pair_names", "cutoff_R", "enumerated_coprime_pairs",
                "omitted_condition", "optimal_policies", "best_cost",
                "desynchronised_cost", "tail_formula", "tail_lower_bound",
                "tail_minus_incumbent", "certified",
            },
        )
        indices = _list(entry["pair_indices"], name=f"{name}.pair_indices", length=2)
        pair = tuple(_integer(value, name=f"{name}.pair_indices", minimum=0) for value in indices)
        if pair not in EXPECTED_PAIRS:
            raise ValueError(f"{name}.pair_indices is not a canonical item pair")
        declared_pairs.append(pair)  # type: ignore[arg-type]
        _integer(entry["cutoff_R"], name=f"{name}.cutoff_R", minimum=2)
        _integer(entry["enumerated_coprime_pairs"], name=f"{name}.enumerated_coprime_pairs", minimum=1)
        if entry["certified"] is not True:
            raise ValueError(f"{name}.certified must be true")
        policies = _list(entry["optimal_policies"], name=f"{name}.optimal_policies")
        if not policies:
            raise ValueError(f"{name}.optimal_policies must not be empty")
        seen_policies: set[tuple[int, int]] = set()
        for policy_index, raw_policy in enumerate(policies):
            policy_name = f"{name}.optimal_policies[{policy_index}]"
            policy = _mapping(
                raw_policy,
                name=policy_name,
                required={"p", "q"},
                allowed={
                    "p", "q", "convention", "cost", "pair_component", "pair_indices",
                    "pair_names", "period_ratio_Tj_over_Ti", "singleton_component",
                    "singleton_index", "singleton_name",
                },
            )
            key = (
                _integer(policy["p"], name=f"{policy_name}.p", minimum=1),
                _integer(policy["q"], name=f"{policy_name}.q", minimum=1),
            )
            if key in seen_policies:
                raise ValueError(f"{name}.optimal_policies contains a duplicate {key}")
            seen_policies.add(key)
        _validate_expression_payload(entry["best_cost"], name=f"{name}.best_cost")
        _validate_expression_payload(entry["tail_lower_bound"], name=f"{name}.tail_lower_bound")
        _validate_expression_payload(entry["tail_minus_incumbent"], name=f"{name}.tail_minus_incumbent")
    if sorted(declared_pairs) != list(EXPECTED_PAIRS):
        raise ValueError("one_pair_oracles must contain each canonical pair exactly once")

    _validate_expression_payload(certificate["boundary_cost"], name="boundary_cost")
    _integer(certificate["triple_cutoff_S"], name="triple_cutoff_S", minimum=2)
    _integer(certificate["component_bound"], name="component_bound", minimum=1)
    _rational_text(certificate["tail_factor_squared"], name="tail_factor_squared")
    _integer(certificate["enumerated_primitive_triples"], name="enumerated_primitive_triples", minimum=1)
    if certificate["candidate_global_optimum_under_stated_proof"] is not True:
        raise ValueError("candidate_global_optimum_under_stated_proof must be true")

    triple_policies = _list(certificate["optimal_triple_policies"], name="optimal_triple_policies")
    if not triple_policies:
        raise ValueError("optimal_triple_policies must not be empty")
    seen_triples: set[tuple[int, int, int]] = set()
    for index, raw_policy in enumerate(triple_policies):
        name = f"optimal_triple_policies[{index}]"
        policy = _mapping(
            raw_policy,
            name=name,
            required={"primitive_multipliers"},
            allowed={
                "A", "B", "cost", "frequencies", "frequency_caps", "pair_complexities",
                "periods", "primitive_multipliers", "scale_mode", "second_pair_complexity",
                "t", "t_min", "union_density_coefficient",
            },
        )
        raw_multipliers = _list(
            policy["primitive_multipliers"], name=f"{name}.primitive_multipliers", length=3
        )
        multipliers = tuple(
            _integer(value, name=f"{name}.primitive_multipliers", minimum=1)
            for value in raw_multipliers
        )
        if multipliers in seen_triples:
            raise ValueError(f"optimal_triple_policies contains duplicate {multipliers}")
        seen_triples.add(multipliers)  # type: ignore[arg-type]

    true_optimum = _mapping(
        certificate["true_optimum"],
        name="true_optimum",
        required={"kind", "value", "expression"},
        allowed={"kind", "value", "expression", "decimal"},
    )
    if true_optimum["kind"] not in {"rational", "two_sqrt"}:
        raise ValueError("true_optimum.kind must be rational or two_sqrt")
    optimum_value = _rational_text(true_optimum["value"], name="true_optimum.value")
    optimum_expression = _parse_expression_text(
        true_optimum["expression"], name="true_optimum.expression"
    )
    expected_optimum = ScaleCost(true_optimum["kind"], Fraction(optimum_value)).expression
    if exact_compare(optimum_expression, expected_optimum) != 0:
        raise ValueError("true_optimum.expression contradicts true_optimum.kind/value")
    if "decimal" in true_optimum:
        _validate_decimal(true_optimum["decimal"], expected_optimum, name="true_optimum.decimal")
    _validate_expression_payload(certificate["tail_lower_bound"], name="tail_lower_bound")
    _validate_expression_payload(certificate["tail_minus_incumbent"], name="tail_minus_incumbent")
    _validate_expression_payload(certificate["integrality_gap"], name="integrality_gap")
    if "two_item_gamma_upper_bound_used_for_comparison" in certificate:
        _rational_text(
            certificate["two_item_gamma_upper_bound_used_for_comparison"],
            name="two_item_gamma_upper_bound_used_for_comparison",
        )
    if certificate.get("conclusion") != certificate_conclusion(
        certificate["integrality_gap"]["expression"]
    ):
        raise ValueError("certificate.conclusion does not match the v2 candidate assurance contract")
    return certificate


def _parse_expression_text(value: Any, *, name: str = "expression") -> sp.Expr:
    tree = _bounded_ast(value, name=name)

    def evaluate(node: ast.AST) -> sp.Expr:
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            return sp.Integer(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            operand = evaluate(node.operand)
            return operand if isinstance(node.op, ast.UAdd) else -operand
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left, right = evaluate(node.left), evaluate(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if right == 0:
                raise ValueError(f"{name} divides by zero")
            return left / right
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "sqrt"
            and len(node.args) == 1
            and not node.keywords
        ):
            return sp.sqrt(evaluate(node.args[0]))
        raise ValueError(f"{name} contains unsupported syntax")

    parsed = sp.simplify(evaluate(tree))
    if parsed.free_symbols or parsed.is_real is False:
        raise ValueError(f"{name} must be a real exact expression without symbols")
    return parsed


def _bounded_ast(value: Any, *, name: str) -> ast.Expression:
    if not isinstance(value, str) or not value or len(value) > MAX_EXPRESSION_LENGTH:
        raise ValueError(f"{name} is empty or exceeds the expression-size limit")
    if any(len(token) > MAX_INTEGER_DIGITS for token in re.findall(r"[0-9]+", value)):
        raise ValueError(f"{name} contains an oversized integer")
    try:
        tree = ast.parse(value, mode="eval")
    except (SyntaxError, ValueError) as exc:
        raise ValueError(f"{name} is not a valid exact arithmetic expression") from exc
    if sum(1 for _ in ast.walk(tree)) > MAX_EXPRESSION_NODES:
        raise ValueError(f"{name} exceeds the expression-complexity limit")
    return tree


def _parse_polynomial_text(value: Any, *, name: str) -> sp.Poly:
    tree = _bounded_ast(value, name=name)
    x = sp.Symbol("x")

    def evaluate(node: ast.AST) -> sp.Expr:
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        if isinstance(node, ast.Name) and node.id == "x":
            return x
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and not isinstance(node.value, bool):
            return sp.Integer(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            operand = evaluate(node.operand)
            return operand if isinstance(node.op, ast.UAdd) else -operand
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult)):
            left, right = evaluate(node.left), evaluate(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            return left * right
        if (
            isinstance(node, ast.BinOp)
            and isinstance(node.op, ast.Pow)
            and isinstance(node.right, ast.Constant)
            and isinstance(node.right.value, int)
            and 0 <= node.right.value <= MAX_POLYNOMIAL_EXPONENT
        ):
            return evaluate(node.left) ** node.right.value
        raise ValueError(f"{name} is not a bounded integer polynomial in x")

    try:
        return sp.Poly(evaluate(tree), x, domain=sp.ZZ)
    except Exception as exc:
        raise ValueError(f"{name} is not a bounded integer polynomial in x") from exc


def _validate_decimal(value: Any, exact: sp.Expr, *, name: str) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{name} must be a decimal string")
    try:
        observed = Decimal(value)
        expected = Decimal(str(sp.N(exact, 50)))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{name} is not a finite decimal") from exc
    if not observed.is_finite():
        raise ValueError(f"{name} is not a finite decimal")
    tolerance = Decimal("1e-35") * max(Decimal(1), abs(expected))
    if abs(observed - expected) > tolerance:
        raise ValueError(f"{name} contradicts the exact expression")


def _parse_expr(payload: dict[str, Any]) -> sp.Expr:
    if "rational" in payload:
        return q(Fraction(payload["rational"]))
    return _parse_expression_text(payload.get("expression"), name="certificate expression")


def _canonical_identifier(path: Path) -> str:
    resolved = path.resolve()
    for parent in (resolved.parent, *resolved.parents):
        if (parent / "pyproject.toml").is_file():
            return resolved.relative_to(parent).as_posix()
    return path.name


def _component(c: Fraction, h: Fraction, cap: Fraction) -> sp.Expr:
    if h >= c * cap * cap:
        return q(c * cap + h / cap)
    return 2 * sp.sqrt(q(c * h))


def _min_expr(a: sp.Expr, b: sp.Expr) -> sp.Expr:
    return a if exact_compare(a, b) <= 0 else b


def _relaxation(instance: CapInstance) -> tuple[sp.Expr, tuple[sp.Expr, ...]]:
    v: list[sp.Expr] = []
    for item in instance.items:
        individual = q(item.cap) if item.K == 0 else _min_expr(q(item.cap), sp.sqrt(q(item.H / item.K)))
        v.append(individual)
    candidates: list[sp.Expr] = list(v)
    for size in (1, 2, 3):
        for subset in combinations(range(3), size):
            active = set(subset)
            c = instance.K0 + sum(instance.items[i].K for i in active)
            h = sum(instance.items[i].H for i in active)
            m = sp.sqrt(q(h / c))
            if all(
                (exact_compare(m, v[i]) <= 0 if i in active else exact_compare(m, v[i]) >= 0)
                for i in range(3)
            ):
                candidates.append(m)
    unique: list[sp.Expr] = []
    for m in candidates:
        if all(exact_compare(m, prior) != 0 for prior in unique):
            unique.append(m)
    best_cost: sp.Expr | None = None
    best_f: tuple[sp.Expr, ...] | None = None
    for m in unique:
        f = tuple(_min_expr(m, v_i) for v_i in v)
        max_f = f[0]
        for value in f[1:]:
            if exact_compare(value, max_f) > 0:
                max_f = value
        cost = q(instance.K0) * max_f
        cost += sum(q(item.K) * value + q(item.H) / value for item, value in zip(instance.items, f))
        cost = sp.simplify(cost)
        if best_cost is None or exact_compare(cost, best_cost) < 0:
            best_cost, best_f = cost, f
    if best_cost is None or best_f is None:
        raise RuntimeError("No relaxation candidate")
    return best_cost, best_f


def _desync(instance: CapInstance) -> sp.Expr:
    return sp.simplify(sum(_component(instance.K0 + item.K, item.H, item.cap) for item in instance.items))


def _pair_cost(instance: CapInstance, pair: tuple[int, int], p: int, q_: int) -> sp.Expr:
    i, j = pair
    k = next(index for index in range(3) if index not in pair)
    ii, jj, kk = instance.items[i], instance.items[j], instance.items[k]
    c = instance.K0 * Fraction(p + q_ - 1, p * q_) + ii.K / q_ + jj.K / p
    h = ii.H * q_ + jj.H * p
    cap = min(q_ * ii.cap, p * jj.cap)
    return sp.simplify(_component(c, h, cap) + _component(instance.K0 + kk.K, kk.H, kk.cap))


def _pairs(R: int):
    for p in range(1, R):
        for q_ in range(1, R - p + 1):
            if gcd(p, q_) == 1:
                yield p, q_


def _pair_best(instance: CapInstance, pair: tuple[int, int], R: int) -> tuple[sp.Expr, list[tuple[int, int]], int]:
    best: sp.Expr | None = None
    policies: list[tuple[int, int]] = []
    count = 0
    for p, q_ in _pairs(R):
        count += 1
        cost = _pair_cost(instance, pair, p, q_)
        if best is None or exact_compare(cost, best) < 0:
            best, policies = cost, [(p, q_)]
        elif exact_compare(cost, best) == 0:
            policies.append((p, q_))
    if best is None:
        raise RuntimeError("No pair candidates")
    return best, policies, count


def _primitive(a: tuple[int, int, int]) -> tuple[int, int, int]:
    d = gcd(gcd(a[0], a[1]), a[2])
    return tuple(x // d for x in a)  # type: ignore[return-value]


def _sigma(a: tuple[int, int, int], i: int, j: int) -> int:
    return (a[i] + a[j]) // gcd(a[i], a[j])


def _second_sigma(a: tuple[int, int, int]) -> int:
    return sorted((_sigma(a, 0, 1), _sigma(a, 0, 2), _sigma(a, 1, 2)))[1]


def _triples(S: int) -> tuple[tuple[int, int, int], ...]:
    reduced = [
        (r, s)
        for r in range(1, S)
        for s in range(1, S - r + 1)
        if gcd(r, s) == 1
    ]
    output: set[tuple[int, int, int]] = set()
    for anchor in range(3):
        others = [i for i in range(3) if i != anchor]
        left, right = others
        for r, s in reduced:
            for u, v in reduced:
                L = lcm(r, u)
                raw = [0, 0, 0]
                raw[anchor], raw[left], raw[right] = L, L * s // r, L * v // u
                a = _primitive(tuple(raw))  # type: ignore[arg-type]
                if _second_sigma(a) <= S:
                    output.add(a)
    return tuple(sorted(output))


def _union(a: tuple[int, int, int]) -> Fraction:
    return (
        sum((Fraction(1, x) for x in a), Fraction())
        - Fraction(1, lcm(a[0], a[1]))
        - Fraction(1, lcm(a[0], a[2]))
        - Fraction(1, lcm(a[1], a[2]))
        + Fraction(1, lcm(lcm(a[0], a[1]), a[2]))
    )


def _triple_cost(instance: CapInstance, a: tuple[int, int, int]) -> ScaleCost:
    A = instance.K0 * _union(a) + sum(item.K / x for item, x in zip(instance.items, a))
    B = sum(item.H * x for item, x in zip(instance.items, a))
    t_min = max(Fraction(1, x * item.cap) for item, x in zip(instance.items, a))
    if t_min * t_min * B < A:
        return ScaleCost("two_sqrt", A * B)
    return ScaleCost("rational", A / t_min + B * t_min)


def _triple_best(instance: CapInstance, S: int) -> tuple[ScaleCost, list[tuple[int, int, int]], int]:
    triples = _triples(S)
    best: ScaleCost | None = None
    policies: list[tuple[int, int, int]] = []
    for a in triples:
        cost = _triple_cost(instance, a)
        if best is None or cost.compare(best) < 0:
            best, policies = cost, [a]
        elif cost.compare(best) == 0:
            policies.append(a)
    if best is None:
        raise RuntimeError("No triple candidates")
    return best, policies, len(triples)


def verify_certificate(
    certificate_path: str | Path,
    *,
    instance_path: str | Path | None = None,
) -> dict[str, Any]:
    certificate_path = Path(certificate_path)
    certificate = _validate_certificate_schema(
        json.loads(certificate_path.read_text(encoding="utf-8"))
    )
    instance = instance_from_dict(certificate["instance"])
    checks: list[dict[str, Any]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        checks.append({"name": name, "passed": bool(condition), "detail": detail})
        if not condition:
            raise AssertionError(f"{name}: {detail}")

    if instance_path is not None:
        raw = Path(instance_path).read_bytes()
        expected = certificate.get("instance_sha256")
        check("instance_sha256_present", isinstance(expected, str), "source instance hash is required")
        check("instance_sha256", expected == hashlib.sha256(raw).hexdigest(), "source instance hash")
        external = load_instance(instance_path)
        check("embedded_instance", external == instance, "embedded and external instances agree")

    relaxation, frequencies = _relaxation(instance)
    declared_relaxation = _parse_expr(certificate["relaxation"]["cost"])
    check("relaxation_cost", exact_compare(relaxation, declared_relaxation) == 0, str(relaxation))
    check(
        "relaxation_frequencies",
        all(
            exact_compare(value, _parse_expression_text(text, name="relaxation frequency")) == 0
            for value, text in zip(frequencies, certificate["relaxation"]["frequencies"])
        ),
        str(frequencies),
    )

    M0 = _desync(instance)
    declared_M0 = _parse_expr(certificate["desynchronised_regime"]["cost"])
    check("desynchronised_cost", exact_compare(M0, declared_M0) == 0, str(M0))

    pair_entries = certificate.get("one_pair_oracles")
    check("pair_oracle_count", isinstance(pair_entries, list) and len(pair_entries) == 3, "three pair oracles")
    declared_pair_set = sorted(tuple(entry["pair_indices"]) for entry in pair_entries)
    check("pair_oracle_partition", declared_pair_set == list(EXPECTED_PAIRS), str(declared_pair_set))

    pair_costs: list[sp.Expr] = []
    for pair_entry in pair_entries:
        pair = tuple(pair_entry["pair_indices"])
        R = int(pair_entry["cutoff_R"])
        check(f"pair_{pair}_cutoff_range", R >= 2, str(R))
        best, policies, count = _pair_best(instance, pair, R)  # type: ignore[arg-type]
        declared = _parse_expr(pair_entry["best_cost"])
        check(f"pair_{pair}_best", exact_compare(best, declared) == 0, str(best))
        check(f"pair_{pair}_count", count == pair_entry["enumerated_coprime_pairs"], str(count))
        declared_policies = sorted((p["p"], p["q"]) for p in pair_entry["optimal_policies"])
        check(f"pair_{pair}_policies", sorted(policies) == declared_policies, str(policies))
        tail = sp.sqrt(sp.Rational(R, R + 1)) * M0
        check(f"pair_{pair}_tail_closes", exact_compare(best, tail) <= 0, str(sp.simplify(tail - best)))
        check(f"pair_{pair}_certified_flag", pair_entry.get("certified") is True, "declared certified")
        declared_tail = _parse_expr(pair_entry["tail_lower_bound"])
        check(f"pair_{pair}_tail_value", exact_compare(tail, declared_tail) == 0, str(tail))
        declared_tail_margin = _parse_expr(pair_entry["tail_minus_incumbent"])
        check(
            f"pair_{pair}_tail_margin",
            exact_compare(tail - best, declared_tail_margin) == 0,
            str(sp.simplify(tail - best)),
        )
        if R > 2:
            prior_best, _, _ = _pair_best(instance, pair, R - 1)  # type: ignore[arg-type]
            prior_tail = sp.sqrt(sp.Rational(R - 1, R)) * M0
            check(f"pair_{pair}_minimal_cutoff", exact_compare(prior_best, prior_tail) > 0, f"R-1={R-1}")
        pair_costs.append(best)

    boundary = M0
    for value in pair_costs:
        if exact_compare(value, boundary) < 0:
            boundary = value
    declared_boundary = _parse_expr(certificate["boundary_cost"])
    check("boundary_cost", exact_compare(boundary, declared_boundary) == 0, str(boundary))

    S = int(certificate["triple_cutoff_S"])
    check("triple_cutoff_range", S >= 2, str(S))
    check("component_bound", certificate.get("component_bound") == (S - 1) ** 2, str((S - 1) ** 2))
    check(
        "tail_factor_squared",
        Fraction(certificate.get("tail_factor_squared", "0")) == Fraction(S - 1, S + 1),
        str(Fraction(S - 1, S + 1)),
    )
    check(
        "candidate_global_optimum_under_stated_proof_flag",
        certificate.get("candidate_global_optimum_under_stated_proof") is True,
        "declared candidate optimum under the bundled proof",
    )
    best, policies, count = _triple_best(instance, S)
    declared_best = certificate["true_optimum"]
    declared_scale = ScaleCost(declared_best["kind"], Fraction(declared_best["value"]))
    check("triple_best_cost", best.compare(declared_scale) == 0, str(best.expression))
    check("triple_count", count == certificate["enumerated_primitive_triples"], str(count))
    declared_policies = sorted(tuple(p["primitive_multipliers"]) for p in certificate["optimal_triple_policies"])
    check("triple_policies", sorted(policies) == declared_policies, str(policies))
    tail = sp.sqrt(sp.Rational(S - 1, S + 1)) * boundary
    check("triple_tail_closes", exact_compare(best.expression, tail) <= 0, str(sp.simplify(tail - best.expression)))
    declared_tail = _parse_expr(certificate["tail_lower_bound"])
    check("triple_tail_value", exact_compare(tail, declared_tail) == 0, str(tail))
    declared_tail_margin = _parse_expr(certificate["tail_minus_incumbent"])
    check(
        "triple_tail_margin",
        exact_compare(tail - best.expression, declared_tail_margin) == 0,
        str(sp.simplify(tail - best.expression)),
    )
    if S > 2:
        prior_best, _, _ = _triple_best(instance, S - 1)
        prior_tail = sp.sqrt(sp.Rational(S - 2, S)) * boundary
        check("triple_minimal_cutoff", exact_compare(prior_best.expression, prior_tail) > 0, f"S-1={S-1}")

    gap = sp.simplify(best.expression / relaxation)
    declared_gap = _parse_expr(certificate["integrality_gap"])
    check("integrality_gap", exact_compare(gap, declared_gap) == 0, str(gap))

    gamma_upper_text = certificate.get("two_item_gamma_upper_bound_used_for_comparison")
    if gamma_upper_text:
        gamma_upper = q(Fraction(gamma_upper_text))
        check("exceeds_two_item_gamma", exact_compare(gap, gamma_upper) > 0, f"{gap} > {gamma_upper}")

    return {
        "schema": "jrp3.verification-report.v1",
        "certificate": _canonical_identifier(certificate_path),
        "passed": True,
        "checks": checks,
        "check_count": len(checks),
        "recomputed_true_optimum": str(best.expression),
        "recomputed_relaxation": str(relaxation),
        "recomputed_gap": str(gap),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the same-producer solver-independent jrp3 certificate verifier"
    )
    parser.add_argument("certificate")
    parser.add_argument("--instance")
    parser.add_argument("--output", "-o")
    args = parser.parse_args()
    report = verify_certificate(args.certificate, instance_path=args.instance)
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
