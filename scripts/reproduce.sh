#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"
cd "$ROOT"
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"
"$PYTHON_BIN" scripts/build_witness_certificates.py
"$PYTHON_BIN" -m jrp3.verify \
  certificates/three_item_gap_witness.certificate.json \
  --instance data/three_item_gap_witness.json \
  --output certificates/three_item_gap_witness.verification.json
"$PYTHON_BIN" -m jrp3.verify \
  certificates/near_extremal_three_item_gap_witness.certificate.json \
  --instance data/near_extremal_three_item_gap_witness.json \
  --output certificates/near_extremal_three_item_gap_witness.verification.json
"$PYTHON_BIN" -m jrp3.verify \
  certificates/active_envelope_three_item_gap_witness.certificate.json \
  --instance data/active_envelope_three_item_gap_witness.json \
  --output certificates/active_envelope_three_item_gap_witness.verification.json
"$PYTHON_BIN" scripts/build_extensions.py
"$PYTHON_BIN" -m unittest discover -s tests -v
"$PYTHON_BIN" scripts/generated_manifest.py --check
"$PYTHON_BIN" scripts/pdf_tex_preflight.py paper/three_item_jrp_gap_and_logistics.pdf
"$PYTHON_BIN" scripts/release_consistency.py --stage auto --allow-unsealed
