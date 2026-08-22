from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import gcd, lcm
from typing import Any, Iterable

import sympy as sp

from .algebra import ScaleCost, decimal_text, exact_compare, expression_payload, fraction_text, q
from .contracts import (
    CERTIFICATE_SCHEMA,
    PREDECESSOR_STATUS,
    PROOF_DEPENDENCY,
    VERIFICATION_INDEPENDENCE,
)
from .model import CapInstance


@dataclass(frozen=True)
class ComponentOptimum:
    coefficient: Fraction
    holding: Fraction
    cap: Fraction
    mode: str
    frequency: sp.Expr
    cost: sp.Expr

    def to_dict(self) -> dict[str, Any]:
        return {
            "coefficient": fraction_text(self.coefficient),
            "holding": fraction_text(self.holding),
            "frequency_cap": fraction_text(self.cap),
            "mode": self.mode,
            "frequency": str(self.frequency),
            "cost": expression_payload(self.cost),
        }


def component_optimum(coefficient: Fraction, holding: Fraction, cap: Fraction) -> ComponentOptimum:
    if coefficient <= 0 or holding <= 0 or cap <= 0:
        raise ValueError("component coefficients, holding and cap must be positive")
    if holding >= coefficient * cap * cap:
        frequency = q(cap)
        cost = q(coefficient * cap + holding / cap)
        mode = "cap"
    else:
        frequency = sp.sqrt(q(holding / coefficient))
        cost = 2 * sp.sqrt(q(coefficient * holding))
        mode = "interior"
    return ComponentOptimum(coefficient, holding, cap, mode, frequency, sp.simplify(cost))


@dataclass(frozen=True)
class RelaxationResult:
    max_frequency: sp.Expr
    frequencies: tuple[sp.Expr, sp.Expr, sp.Expr]
    cost: sp.Expr
    candidate_count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "model": "K0*max_i(f_i)+sum_i(K_i*f_i+H_i/f_i)",
            "max_frequency": str(self.max_frequency),
            "frequencies": [str(value) for value in self.frequencies],
            "cost": expression_payload(self.cost),
            "candidate_count": self.candidate_count,
        }


def _min_expr(left: sp.Expr, right: sp.Expr) -> sp.Expr:
    return left if exact_compare(left, right) <= 0 else right


def relaxation_optimum(instance: CapInstance) -> RelaxationResult:
    """Solve the standard independent-cap relaxation exactly.

    For a fixed maximum frequency m, item i uses min(m, v_i), where v_i is
    its individually optimal capped frequency. The remaining objective is a
    one-dimensional piecewise expression c*m+h/m+constant. Enumerating its
    breakpoints and stationary points is exact.
    """
    v: list[sp.Expr] = []
    for item in instance.items:
        if item.K == 0:
            v.append(q(item.cap))
        else:
            v.append(_min_expr(q(item.cap), sp.sqrt(q(item.H / item.K))))

    candidates: list[sp.Expr] = list(v)
    indices = range(3)
    for size in (1, 2, 3):
        for active_tuple in combinations(indices, size):
            active = set(active_tuple)
            c = instance.K0 + sum(instance.items[i].K for i in active)
            h = sum(instance.items[i].H for i in active)
            m = sp.sqrt(q(h / c))
            consistent = True
            for i in indices:
                relation = exact_compare(m, v[i])
                if i in active and relation > 0:
                    consistent = False
                    break
                if i not in active and relation < 0:
                    consistent = False
                    break
            if consistent:
                candidates.append(m)

    # Deduplicate by exact equality.
    unique: list[sp.Expr] = []
    for candidate in candidates:
        if all(exact_compare(candidate, existing) != 0 for existing in unique):
            unique.append(sp.simplify(candidate))

    best: RelaxationResult | None = None
    for m in unique:
        frequencies = tuple(_min_expr(m, v_i) for v_i in v)
        actual_max = frequencies[0]
        for frequency in frequencies[1:]:
            if exact_compare(frequency, actual_max) > 0:
                actual_max = frequency
        cost = q(instance.K0) * actual_max
        for item, frequency in zip(instance.items, frequencies):
            cost += q(item.K) * frequency + q(item.H) / frequency
        result = RelaxationResult(
            max_frequency=sp.simplify(actual_max),
            frequencies=tuple(sp.simplify(x) for x in frequencies),  # type: ignore[arg-type]
            cost=sp.simplify(cost),
            candidate_count=len(unique),
        )
        if best is None or exact_compare(result.cost, best.cost) < 0:
            best = result
    if best is None:
        raise RuntimeError("Relaxation candidate set was empty")
    return best


@dataclass(frozen=True)
class DesynchronisedResult:
    components: tuple[ComponentOptimum, ComponentOptimum, ComponentOptimum]
    cost: sp.Expr

    def to_dict(self) -> dict[str, Any]:
        return {
            "interpretation": "all three order lattices pairwise incommensurable",
            "components": [component.to_dict() for component in self.components],
            "cost": expression_payload(self.cost),
        }


def desynchronised_optimum(instance: CapInstance) -> DesynchronisedResult:
    components = tuple(
        component_optimum(instance.K0 + item.K, item.H, item.cap)
        for item in instance.items
    )
    return DesynchronisedResult(
        components=components,  # type: ignore[arg-type]
        cost=sp.simplify(sum(component.cost for component in components)),
    )


@dataclass(frozen=True)
class PairPolicy:
    pair: tuple[int, int]
    p: int
    q: int
    pair_component: ComponentOptimum
    singleton_component: ComponentOptimum
    cost: sp.Expr

    def to_dict(self, instance: CapInstance) -> dict[str, Any]:
        i, j = self.pair
        k = next(index for index in range(3) if index not in self.pair)
        return {
            "pair_indices": [i, j],
            "pair_names": [instance.items[i].name, instance.items[j].name],
            "singleton_index": k,
            "singleton_name": instance.items[k].name,
            "p": self.p,
            "q": self.q,
            "period_ratio_Tj_over_Ti": f"{self.p}/{self.q}",
            "convention": "T_i=q*t and T_j=p*t",
            "pair_component": self.pair_component.to_dict(),
            "singleton_component": self.singleton_component.to_dict(),
            "cost": expression_payload(self.cost),
        }


def pair_policy(instance: CapInstance, pair: tuple[int, int], p: int, q_: int) -> PairPolicy:
    if p <= 0 or q_ <= 0 or gcd(p, q_) != 1:
        raise ValueError("p and q must be positive and coprime")
    i, j = pair
    if i == j or not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("pair must contain two distinct item indices")
    k = next(index for index in range(3) if index not in pair)
    item_i, item_j, item_k = instance.items[i], instance.items[j], instance.items[k]
    coefficient = (
        instance.K0 * Fraction(p + q_ - 1, p * q_)
        + item_i.K / q_
        + item_j.K / p
    )
    holding = item_i.H * q_ + item_j.H * p
    cap = min(q_ * item_i.cap, p * item_j.cap)
    paired = component_optimum(coefficient, holding, cap)
    singleton = component_optimum(instance.K0 + item_k.K, item_k.H, item_k.cap)
    return PairPolicy(
        pair=pair,
        p=p,
        q=q_,
        pair_component=paired,
        singleton_component=singleton,
        cost=sp.simplify(paired.cost + singleton.cost),
    )


def coprime_pairs(cutoff: int) -> Iterable[tuple[int, int]]:
    if cutoff < 2:
        return
    for p in range(1, cutoff):
        for q_ in range(1, cutoff - p + 1):
            if gcd(p, q_) == 1:
                yield p, q_


@dataclass(frozen=True)
class PairOracleResult:
    pair: tuple[int, int]
    cutoff: int
    enumerated_count: int
    best_cost: sp.Expr
    policies: tuple[PairPolicy, ...]
    desynchronised_cost: sp.Expr
    tail_lower_bound: sp.Expr
    certified: bool

    def to_dict(self, instance: CapInstance) -> dict[str, Any]:
        margin = sp.simplify(self.tail_lower_bound - self.best_cost)
        return {
            "pair_indices": list(self.pair),
            "pair_names": [instance.items[i].name for i in self.pair],
            "cutoff_R": self.cutoff,
            "enumerated_coprime_pairs": self.enumerated_count,
            "omitted_condition": f"p+q >= {self.cutoff + 1}",
            "best_cost": expression_payload(self.best_cost),
            "optimal_policies": [policy.to_dict(instance) for policy in self.policies],
            "desynchronised_cost": expression_payload(self.desynchronised_cost),
            "tail_formula": f"sqrt({self.cutoff}/{self.cutoff + 1})*M0",
            "tail_lower_bound": expression_payload(self.tail_lower_bound),
            "tail_minus_incumbent": expression_payload(margin),
            "certified": self.certified,
        }


def pair_oracle(
    instance: CapInstance,
    pair: tuple[int, int],
    desynchronised: DesynchronisedResult | None = None,
    *,
    max_cutoff: int | None = None,
) -> PairOracleResult:
    baseline = desynchronised or desynchronised_optimum(instance)
    cutoff = 2
    while True:
        best_cost: sp.Expr | None = None
        policies: list[PairPolicy] = []
        count = 0
        for p, q_ in coprime_pairs(cutoff):
            count += 1
            policy = pair_policy(instance, pair, p, q_)
            if best_cost is None or exact_compare(policy.cost, best_cost) < 0:
                best_cost = policy.cost
                policies = [policy]
            elif exact_compare(policy.cost, best_cost) == 0:
                policies.append(policy)
        if best_cost is None:
            raise RuntimeError("No pair policies were enumerated")
        tail = sp.sqrt(sp.Rational(cutoff, cutoff + 1)) * baseline.cost
        closes = exact_compare(best_cost, tail) <= 0
        result = PairOracleResult(
            pair=pair,
            cutoff=cutoff,
            enumerated_count=count,
            best_cost=sp.simplify(best_cost),
            policies=tuple(policies),
            desynchronised_cost=baseline.cost,
            tail_lower_bound=sp.simplify(tail),
            certified=closes,
        )
        if closes:
            return result
        if max_cutoff is not None and cutoff >= max_cutoff:
            return result
        cutoff += 1


def union_coefficient(a: tuple[int, int, int]) -> Fraction:
    if any(value <= 0 for value in a):
        raise ValueError("Primitive multipliers must be positive")
    a1, a2, a3 = a
    return (
        Fraction(1, a1)
        + Fraction(1, a2)
        + Fraction(1, a3)
        - Fraction(1, lcm(a1, a2))
        - Fraction(1, lcm(a1, a3))
        - Fraction(1, lcm(a2, a3))
        + Fraction(1, lcm(lcm(a1, a2), a3))
    )


def pair_complexity(a: tuple[int, int, int], i: int, j: int) -> int:
    return (a[i] + a[j]) // gcd(a[i], a[j])


def second_pair_complexity(a: tuple[int, int, int]) -> int:
    return sorted(
        [pair_complexity(a, 0, 1), pair_complexity(a, 0, 2), pair_complexity(a, 1, 2)]
    )[1]


def _primitive(a: tuple[int, int, int]) -> tuple[int, int, int]:
    common = gcd(gcd(a[0], a[1]), a[2])
    return tuple(value // common for value in a)  # type: ignore[return-value]


@lru_cache(maxsize=128)
def _reduced_pairs(cutoff: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (r, s)
        for r in range(1, cutoff)
        for s in range(1, cutoff - r + 1)
        if gcd(r, s) == 1
    )


@lru_cache(maxsize=128)
def primitive_triples(cutoff: int) -> tuple[tuple[int, int, int], ...]:
    """Enumerate exactly the primitive triples with second pair complexity <= cutoff.

    Any two qualifying pair ratios share a vertex. Writing those two ratios in
    lowest terms determines a primitive triple. Conversely every qualifying
    triple appears under at least one anchor. This is finite; each component is
    at most (cutoff-1)^2.
    """
    if cutoff < 2:
        return ()
    pairs = _reduced_pairs(cutoff)
    triples: set[tuple[int, int, int]] = set()
    for anchor in range(3):
        others = [index for index in range(3) if index != anchor]
        left, right = others
        for r, s in pairs:
            for u, v in pairs:
                common_anchor = lcm(r, u)
                values = [0, 0, 0]
                values[anchor] = common_anchor
                values[left] = common_anchor * s // r
                values[right] = common_anchor * v // u
                candidate = _primitive(tuple(values))  # type: ignore[arg-type]
                if second_pair_complexity(candidate) <= cutoff:
                    triples.add(candidate)
    return tuple(sorted(triples))


@dataclass(frozen=True)
class TriplePolicy:
    multipliers: tuple[int, int, int]
    union_density_coefficient: Fraction
    A: Fraction
    B: Fraction
    t_min: Fraction
    interior: bool
    cost: ScaleCost

    @property
    def t_expression(self) -> sp.Expr:
        if self.interior:
            return sp.sqrt(q(self.A / self.B))
        return q(self.t_min)

    def to_dict(self, instance: CapInstance) -> dict[str, Any]:
        t = self.t_expression
        frequencies = [sp.simplify(1 / (a_i * t)) for a_i in self.multipliers]
        return {
            "primitive_multipliers": list(self.multipliers),
            "periods": [f"{a_i}*t" for a_i in self.multipliers],
            "pair_complexities": {
                "0-1": pair_complexity(self.multipliers, 0, 1),
                "0-2": pair_complexity(self.multipliers, 0, 2),
                "1-2": pair_complexity(self.multipliers, 1, 2),
            },
            "second_pair_complexity": second_pair_complexity(self.multipliers),
            "union_density_coefficient": fraction_text(self.union_density_coefficient),
            "A": fraction_text(self.A),
            "B": fraction_text(self.B),
            "t_min": fraction_text(self.t_min),
            "scale_mode": "interior" if self.interior else "cap",
            "t": str(t),
            "frequencies": [str(value) for value in frequencies],
            "frequency_caps": [fraction_text(item.cap) for item in instance.items],
            "cost": self.cost.to_dict(),
        }


def triple_policy(instance: CapInstance, a: tuple[int, int, int]) -> TriplePolicy:
    if gcd(gcd(a[0], a[1]), a[2]) != 1:
        raise ValueError("Triple multipliers must be primitive")
    union = union_coefficient(a)
    A = instance.K0 * union + sum(item.K / multiplier for item, multiplier in zip(instance.items, a))
    B = sum(item.H * multiplier for item, multiplier in zip(instance.items, a))
    t_min = max(Fraction(1, 1) / (multiplier * item.cap) for item, multiplier in zip(instance.items, a))
    interior = t_min * t_min * B < A
    if interior:
        cost = ScaleCost("two_sqrt", A * B)
    else:
        cost = ScaleCost("rational", A / t_min + B * t_min)
    return TriplePolicy(a, union, A, B, t_min, interior, cost)


@dataclass(frozen=True)
class TripleOracleResult:
    instance: CapInstance
    relaxation: RelaxationResult
    desynchronised: DesynchronisedResult
    pair_results: tuple[PairOracleResult, PairOracleResult, PairOracleResult]
    boundary_cost: sp.Expr
    cutoff: int
    enumerated_triples: int
    best_cost: ScaleCost
    policies: tuple[TriplePolicy, ...]
    tail_lower_bound: sp.Expr
    certified: bool

    @property
    def gap(self) -> sp.Expr:
        return sp.simplify(self.best_cost.expression / self.relaxation.cost)

    def to_dict(self) -> dict[str, Any]:
        r = Fraction(self.cutoff - 1, self.cutoff + 1)
        return {
            "schema": CERTIFICATE_SCHEMA,
            "scope": "three items with independent rational frequency caps",
            "instance": self.instance.to_dict(),
            "regimes": [
                "fully commensurable primitive integer triples",
                "exactly one commensurable pair",
                "pairwise incommensurable",
            ],
            "relaxation": self.relaxation.to_dict(),
            "desynchronised_regime": self.desynchronised.to_dict(),
            "one_pair_oracles": [result.to_dict(self.instance) for result in self.pair_results],
            "boundary_cost": expression_payload(self.boundary_cost),
            "triple_cutoff_S": self.cutoff,
            "enumerated_primitive_triples": self.enumerated_triples,
            "enumeration_condition": f"second-smallest pair complexity <= {self.cutoff}",
            "component_bound": (self.cutoff - 1) ** 2,
            "optimal_triple_policies": [policy.to_dict(self.instance) for policy in self.policies],
            "true_optimum": self.best_cost.to_dict(),
            "tail_factor_squared": fraction_text(r),
            "tail_formula": f"sqrt(({self.cutoff}-1)/({self.cutoff}+1))*M_boundary",
            "tail_lower_bound": expression_payload(self.tail_lower_bound),
            "tail_minus_incumbent": expression_payload(sp.simplify(self.tail_lower_bound - self.best_cost.expression)),
            "candidate_global_optimum_under_stated_proof": self.certified,
            "proof_dependency": PROOF_DEPENDENCY,
            "predecessor_status": PREDECESSOR_STATUS,
            "verification_independence": VERIFICATION_INDEPENDENCE,
            "integrality_gap": expression_payload(self.gap),
            "assurance": {
                "search": "finite exact enumeration with rational arithmetic and exact algebraic comparison",
                "tail": "second-pair-complexity lower bound",
                "verification": (
                    "same-producer solver-independent verifier re-enumerates every declared finite set"
                ),
            },
        }


def solve_exact_cap_oracle(
    instance: CapInstance,
    *,
    start_cutoff: int = 2,
    max_cutoff: int | None = None,
) -> TripleOracleResult:
    relaxation = relaxation_optimum(instance)
    desynchronised = desynchronised_optimum(instance)
    pair_results = tuple(
        pair_oracle(instance, pair, desynchronised)
        for pair in ((0, 1), (0, 2), (1, 2))
    )
    boundary_candidates = [desynchronised.cost] + [result.best_cost for result in pair_results]
    boundary = boundary_candidates[0]
    for candidate in boundary_candidates[1:]:
        if exact_compare(candidate, boundary) < 0:
            boundary = candidate

    cutoff = max(2, start_cutoff)
    seen: set[tuple[int, int, int]] = set()
    best_cost: ScaleCost | None = None
    policies: list[TriplePolicy] = []
    while True:
        candidates = primitive_triples(cutoff)
        for a in candidates:
            if a in seen:
                continue
            seen.add(a)
            policy = triple_policy(instance, a)
            if best_cost is None or policy.cost.compare(best_cost) < 0:
                best_cost = policy.cost
                policies = [policy]
            elif policy.cost.compare(best_cost) == 0:
                policies.append(policy)
        if best_cost is None:
            raise RuntimeError("No primitive triples were enumerated")
        factor = sp.sqrt(sp.Rational(cutoff - 1, cutoff + 1))
        tail = sp.simplify(factor * boundary)
        closes = exact_compare(best_cost.expression, tail) <= 0
        result = TripleOracleResult(
            instance=instance,
            relaxation=relaxation,
            desynchronised=desynchronised,
            pair_results=pair_results,  # type: ignore[arg-type]
            boundary_cost=sp.simplify(boundary),
            cutoff=cutoff,
            enumerated_triples=len(candidates),
            best_cost=best_cost,
            policies=tuple(policies),
            tail_lower_bound=tail,
            certified=closes,
        )
        if closes:
            return result
        if max_cutoff is not None and cutoff >= max_cutoff:
            return result
        cutoff += 1
