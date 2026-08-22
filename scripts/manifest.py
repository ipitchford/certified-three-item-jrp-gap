#!/usr/bin/env python3
"""Write or verify the candidate's complete SHA-256 manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"


def included_files() -> list[Path]:
    """Return every deliverable file except the self-referential manifest."""
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path != MANIFEST
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    )


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def manifest_lines() -> list[str]:
    return [
        f"{digest(path)}  ./{path.relative_to(ROOT).as_posix()}"
        for path in included_files()
    ]


def write_manifest() -> None:
    lines = manifest_lines()
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} entries to {MANIFEST.relative_to(ROOT)}")


def check_manifest() -> None:
    expected = manifest_lines()
    observed = MANIFEST.read_text(encoding="utf-8").splitlines()
    if observed != expected:
        missing = sorted(set(expected) - set(observed))
        stale = sorted(set(observed) - set(expected))
        details = []
        if missing:
            details.append(f"missing-or-changed={len(missing)}")
        if stale:
            details.append(f"stale-or-extra={len(stale)}")
        raise SystemExit("manifest verification failed: " + ", ".join(details))
    print(f"manifest verification passed: {len(observed)} files")


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        write_manifest()
    else:
        check_manifest()


if __name__ == "__main__":
    main()
