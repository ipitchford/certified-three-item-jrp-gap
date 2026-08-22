#!/usr/bin/env python3
"""Write or verify the exact expected bytes of every regenerated artifact."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "GENERATED_ARTIFACTS.sha256"


def generated_files() -> list[Path]:
    files = [
        *ROOT.glob("analysis/*.json"),
        *ROOT.glob("certificates/**/*.json"),
        *ROOT.glob("data/robustness/**/*.json"),
    ]
    return sorted({path.resolve() for path in files if path.is_file()})


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def lines() -> list[str]:
    return [
        f"{digest(path)}  ./{path.relative_to(ROOT).as_posix()}"
        for path in generated_files()
    ]


def write() -> None:
    expected = lines()
    LEDGER.write_text("\n".join(expected) + "\n", encoding="utf-8")
    print(f"wrote {len(expected)} generated-artifact hashes")


def check() -> None:
    expected = lines()
    observed = LEDGER.read_text(encoding="utf-8").splitlines()
    if observed != expected:
        raise SystemExit(
            "generated-artifact verification failed: "
            f"expected {len(observed)} frozen entries, recomputed {len(expected)} entries"
        )
    print(f"generated-artifact verification passed: {len(observed)} files")


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    write() if args.write else check()


if __name__ == "__main__":
    main()
