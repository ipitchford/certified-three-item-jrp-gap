from __future__ import annotations

import hashlib
import json
from pathlib import Path

from jrp3.model import load_instance
from jrp3.oracle import solve_exact_cap_oracle
from jrp3.contracts import certificate_conclusion


ROOT = Path(__file__).resolve().parents[1]
PAIRS = (
    (
        ROOT / "data" / "three_item_gap_witness.json",
        ROOT / "certificates" / "three_item_gap_witness.certificate.json",
    ),
    (
        ROOT / "data" / "near_extremal_three_item_gap_witness.json",
        ROOT / "certificates" / "near_extremal_three_item_gap_witness.certificate.json",
    ),
    (
        ROOT / "data" / "active_envelope_three_item_gap_witness.json",
        ROOT / "certificates" / "active_envelope_three_item_gap_witness.certificate.json",
    ),
)
GAMMA_UPPER = "1111889593940297/1000000000000000"


def build(instance_path: Path, output_path: Path) -> None:
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
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output_path)


def main() -> None:
    for instance_path, output_path in PAIRS:
        build(instance_path, output_path)


if __name__ == "__main__":
    main()
