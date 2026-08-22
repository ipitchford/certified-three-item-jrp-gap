#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PANDOC_BIN="${PANDOC_BIN:-pandoc}"
WEASYPRINT_BIN="${WEASYPRINT_BIN:-weasyprint}"
KATEX_MODULE="${KATEX_MODULE:-/opt/homebrew/lib/node_modules/@mermaid-js/mermaid-cli/node_modules/katex}"
RAW_HTML="$(mktemp "${TMPDIR:-/tmp}/jrp3-paper.XXXXXX.html")"
trap 'rm -f "$RAW_HTML"' EXIT

cd "$ROOT"
"$PANDOC_BIN" paper/three_item_jrp_gap_and_logistics.md \
  --standalone \
  --from=markdown+pipe_tables+tex_math_dollars+tex_math_single_backslash \
  --css=publication.css \
  --katex="file://${KATEX_MODULE}/dist/" \
  --output="$RAW_HTML"

KATEX_MODULE="$KATEX_MODULE" KATEX_OUTPUT=html \
  node scripts/render_katex.js "$RAW_HTML" paper/three_item_jrp_gap_and_logistics.html

"$WEASYPRINT_BIN" \
  paper/three_item_jrp_gap_and_logistics.html \
  paper/three_item_jrp_gap_and_logistics.pdf

