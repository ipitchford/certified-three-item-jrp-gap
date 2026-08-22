from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt
from typing import Any, Literal

import sympy as sp
from sympy.polys.numberfields import to_number_field


CostKind = Literal["rational", "two_sqrt"]


def q(value: Fraction | int) -> sp.Rational:
    value = Fraction(value)
    return sp.Rational(value.numerator, value.denominator)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def exact_compare(left: sp.Expr, right: sp.Expr) -> int:
    """Compare two real algebraic SymPy expressions exactly.

    Every expression produced by this package lies in a multiquadratic number
    field. SymPy normally resolves its sign directly; ``to_number_field`` is a
    deterministic exact fallback rather than a floating-point comparison.
    """
    difference = sp.simplify(left - right)
    if difference == 0:
        return 0
    if difference.is_positive is True:
        return 1
    if difference.is_negative is True:
        return -1
    algebraic = to_number_field(difference)
    if algebraic.is_positive is True:
        return 1
    if algebraic.is_negative is True:
        return -1
    if algebraic.is_zero is True:
        return 0
    raise ArithmeticError(f"Could not determine exact algebraic sign: {difference}")


def exact_min(values: list[sp.Expr]) -> sp.Expr:
    if not values:
        raise ValueError("exact_min requires at least one value")
    best = values[0]
    for value in values[1:]:
        if exact_compare(value, best) < 0:
            best = value
    return sp.simplify(best)


def decimal_text(expr: sp.Expr, digits: int = 40) -> str:
    return str(sp.N(expr, digits))


def expression_payload(expr: sp.Expr, digits: int = 40) -> dict[str, Any]:
    simplified = sp.simplify(expr)
    payload: dict[str, Any] = {
        "expression": str(simplified),
        "decimal": decimal_text(simplified, digits),
    }
    if simplified.is_Rational:
        value = Fraction(int(simplified.p), int(simplified.q))
        payload["rational"] = fraction_text(value)
    else:
        x = sp.Symbol("x")
        try:
            payload["minimal_polynomial"] = str(sp.Poly(sp.minpoly(simplified, x), x).as_expr())
        except Exception:
            # The exact expression is still authoritative. The optional minimal
            # polynomial is diagnostic metadata, not part of verification.
            pass
    return payload


def sqrt_bounds(value: Fraction, bits: int = 256) -> tuple[Fraction, Fraction]:
    """Dyadic lower and upper bounds for sqrt(value), using integer arithmetic."""
    if value < 0:
        raise ValueError("Cannot bound a negative radicand")
    if bits < 1:
        raise ValueError("bits must be positive")
    scale = 1 << bits
    floor_scaled = value.numerator * scale * scale // value.denominator
    root = isqrt(floor_scaled)
    lower = Fraction(root, scale)
    if lower * lower == value:
        return lower, lower
    return lower, Fraction(root + 1, scale)


@dataclass(frozen=True)
class ScaleCost:
    """Exact fixed-pattern cost: either c or 2*sqrt(z), with c,z rational."""

    kind: CostKind
    value: Fraction

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Cost data must be nonnegative")

    @property
    def expression(self) -> sp.Expr:
        if self.kind == "rational":
            return q(self.value)
        return 2 * sp.sqrt(q(self.value))

    def compare(self, other: "ScaleCost") -> int:
        if self.kind == other.kind == "rational":
            return (self.value > other.value) - (self.value < other.value)
        if self.kind == other.kind == "two_sqrt":
            return (self.value > other.value) - (self.value < other.value)
        if self.kind == "rational":
            lhs = self.value * self.value
            rhs = 4 * other.value
            return (lhs > rhs) - (lhs < rhs)
        lhs = 4 * self.value
        rhs = other.value * other.value
        return (lhs > rhs) - (lhs < rhs)

    def to_dict(self, digits: int = 40) -> dict[str, Any]:
        if self.kind == "rational":
            expression = fraction_text(self.value)
        else:
            expression = f"2*sqrt({fraction_text(self.value)})"
        return {
            "kind": self.kind,
            "value": fraction_text(self.value),
            "expression": expression,
            "decimal": decimal_text(self.expression, digits),
        }


def rational_decimal(value: Fraction, precision: int = 50) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision
        return Decimal(value.numerator) / Decimal(value.denominator)
