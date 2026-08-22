from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
from typing import Any

from .algebra import fraction_text


def as_fraction(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("Booleans are not valid numeric inputs")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ValueError("Empty numeric string")
        return Fraction(text)
    if isinstance(value, float):
        raise TypeError(
            "JSON floating-point numbers are not exact inputs; use an integer "
            "or a rational/decimal string"
        )
    raise TypeError(f"Unsupported numeric value: {value!r}")


@dataclass(frozen=True)
class CapItem:
    name: str
    K: Fraction
    H: Fraction
    cap: Fraction

    def __post_init__(self) -> None:
        if self.K < 0:
            raise ValueError(f"{self.name}: K must be nonnegative")
        if self.H <= 0:
            raise ValueError(f"{self.name}: H must be strictly positive")
        if self.cap <= 0:
            raise ValueError(f"{self.name}: cap must be strictly positive")

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "K": fraction_text(self.K),
            "H": fraction_text(self.H),
            "frequency_cap": fraction_text(self.cap),
        }


@dataclass(frozen=True)
class CapInstance:
    name: str
    K0: Fraction
    items: tuple[CapItem, CapItem, CapItem]
    time_unit: str = "normalised time unit"
    currency_unit: str = "normalised cost unit"

    def __post_init__(self) -> None:
        if self.K0 <= 0:
            raise ValueError("K0 must be strictly positive")
        if len(self.items) != 3:
            raise ValueError("Exactly three items are required")

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "K0": fraction_text(self.K0),
            "time_unit": self.time_unit,
            "currency_unit": self.currency_unit,
            "items": [item.to_dict() for item in self.items],
        }


def instance_from_dict(data: dict[str, Any]) -> CapInstance:
    if not isinstance(data, dict):
        raise TypeError("Instance document must be a JSON object")
    allowed = {"name", "K0", "items", "time_unit", "currency_unit"}
    unknown = sorted(set(data) - allowed)
    if unknown:
        raise ValueError(f"Unknown instance fields: {', '.join(unknown)}")
    if "K0" not in data or "items" not in data:
        raise ValueError("K0 and items are required")
    raw_items = data["items"]
    if not isinstance(raw_items, list) or len(raw_items) != 3:
        raise ValueError("items must contain exactly three objects")
    items: list[CapItem] = []
    for index, raw in enumerate(raw_items):
        if not isinstance(raw, dict):
            raise TypeError(f"Item {index}: expected an object")
        allowed_item = {"name", "K", "H", "frequency_cap", "cap"}
        unknown_item = sorted(set(raw) - allowed_item)
        if unknown_item:
            raise ValueError(f"Item {index}: unknown fields: {', '.join(unknown_item)}")
        cap_token = raw.get("frequency_cap", raw.get("cap"))
        if "K" not in raw or "H" not in raw or cap_token is None:
            raise ValueError(f"Item {index}: K, H and frequency_cap are required")
        items.append(
            CapItem(
                name=str(raw.get("name", f"item-{index + 1}")),
                K=as_fraction(raw["K"]),
                H=as_fraction(raw["H"]),
                cap=as_fraction(cap_token),
            )
        )
    return CapInstance(
        name=str(data.get("name", "three-item-cap-jrp")),
        K0=as_fraction(data["K0"]),
        items=tuple(items),  # type: ignore[arg-type]
        time_unit=str(data.get("time_unit", "normalised time unit")),
        currency_unit=str(data.get("currency_unit", "normalised cost unit")),
    )


def load_instance(path: str | Path) -> CapInstance:
    with Path(path).open("r", encoding="utf-8") as handle:
        return instance_from_dict(json.load(handle))
