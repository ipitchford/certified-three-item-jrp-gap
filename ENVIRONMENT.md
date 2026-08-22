# Reproduction environment

Verified on 22 August 2026:

```text
platform: macOS-26.5.2-arm64-arm-64bit-Mach-O
Python:   3.14.6
SymPy:    1.14.0
mpmath:   1.3.0
Pandoc:   3.9
WeasyPrint: 68.1
```

Minimum declared runtime: Python 3.10+. The package pins SymPy 1.14.0 for this candidate. Paper generation additionally uses Node.js with KaTeX, Pandoc, and WeasyPrint through `scripts/build_paper.sh`. Exact installed versions are re-recorded in the final replay receipt. A clean archive-extraction replay passed on the recorded macOS environment; clean cross-platform replay remains open.
