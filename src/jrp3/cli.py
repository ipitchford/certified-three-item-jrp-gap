from __future__ import annotations

import argparse
import json
from pathlib import Path

from .model import load_instance
from .oracle import solve_exact_cap_oracle


def main() -> None:
    parser = argparse.ArgumentParser(description="Exact three-item independent-cap JRP oracle")
    parser.add_argument("instance", help="JSON instance path")
    parser.add_argument("--output", "-o", help="Write certificate JSON to this path")
    parser.add_argument("--max-cutoff", type=int, default=None, help="Fail-closed operational guard")
    args = parser.parse_args()

    instance = load_instance(args.instance)
    result = solve_exact_cap_oracle(instance, max_cutoff=args.max_cutoff)
    payload = result.to_dict()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    if not result.certified:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
