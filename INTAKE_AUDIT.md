# Intake audit: `exact-two-item-three-item`

Audit date: 22 August 2026. Source files were read in full. The source folder was left unchanged.

| File | Bytes | SHA-256 | Disposition |
|---|---:|---|---|
| `exact-three-item-oracle-v0.1.0.zip` | 45,069 | `2165119a68345747d0435aa2b57d696f4bea5791c7b3a13c694e5b6c310f1788` | Core input; all ZIP CRCs and all 27 declared manifest entries passed |
| `near_extremal_three_item_gap_witness.certificate.json` | 14,440 | `0ba7b5661897a3a4b03e4d9502a23ef0769afe26083f8e4e2e7b442343378f80` | Exact duplicate of packaged strong certificate |
| `near_extremal_three_item_gap_witness.verification.json` | 3,799 | `6cda9da7bb971ca38fa929b33e1732dee8456bba5179183057b0e62a375e6255` | Exact duplicate of packaged strong verification report |
| `three_item_oracle_note.md` | 15,021 | `8465032477b4857659f391fdaf5f32047b41e21daed6e374f77c5354583d01be` | Exact duplicate of packaged mathematical note; retained and repaired |
| `Exact Two-Item Resource-Constrained Joint Replenishment and Its Independent-Cap Relaxation Gap.md` | 10,472 | `5e3359466706e9329e73cfbf6b1f95d1f742c602e98043cba6df5e6446afbc4a` | Mixed predecessor/successor draft; excluded from canonical paper because of corrupt TeX, title mismatch, and local sandbox links |
| `factorisation_hc4_priority_note.md` | 4,678 | `d0c61eb6f56daed36fe49101d69cd657ff8105832053eaaa0a124842caea857d` | Unrelated factorisation material; quarantined from the JRP successor, not deleted |

## Rebuild findings

- The supplied exact replay script failed on this Mac because it invoked `python`, which is absent; the successor uses `python3` or `PYTHON_BIN`.
- With a temporary compatibility shim, the original ordinary and optimized replays passed, regenerated both certificates byte-for-byte, and passed 10 tests.
- The v0.2 successor initially passed 12 tests, including rejected floating-point inputs and structural certificate mutations. The v0.3.0 frozen submission expanded that suite to 15. The repaired v0.3.1 suite contains 21 tests, adding strict-shape and one-field exact-value negative controls, bounded expression parsing, package-root path containment, extraction-path byte identity, and complete primitive-plus-boundary portfolio reconstruction.
- The original verification report embedded an absolute path. The successor changes to a repository-relative path so clean-extraction reports are stable.
- The original checker did not require the full pair partition, certified flags, or all declared tail fields. The successor fails closed on these structures.
- The source wording called the checker an independent implementation. It is now described as solver-independent producer replay because it shares provenance and exact-algebra utilities.
- The supplied bibliography contained the wrong DOI for Segev’s pairwise-alignment article; `10.1287/mnsc.2023.00705` is the publisher DOI.
- Source authorship and licence metadata were brought into the current Anonymous scholarly-authorship boundary. Historical source hashes preserve the earlier metadata rather than silently rewriting provenance.

## Mathematical audit outcome

The regime partition, fixed-pattern formula, cap scale, finite generator, pair tail, and triple tail are coherent with the code and exact certificate. The bundled witness is closed without relying on numerical optimisation. The general generator/totality and tail argument remain candidate prose mathematics pending unaffiliated specialist audit or formalisation.

## Decision

The core is suitable for a repaired unrefereed successor candidate. It is not ready to be called published, independently reproduced, or operationally validated.
