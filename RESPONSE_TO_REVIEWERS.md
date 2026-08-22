# Response to the Round-One Editor and Reviewers

Manuscript: *A Candidate Exact Three-Item Independent-Cap Oracle: A Certified Rational Relaxation-Gap Lower Bound and Logistics Handoff*  
Original submission: `exact-three-item-jrp-applications-v0.3.0-candidate`  
Revised submission: `exact-three-item-jrp-applications-v0.3.1-candidate`  
Previous decision: **Major Revision / `HOLD_FOR_REPAIR`**  
Revision date: **22 August 2026**

Dear Editor and Reviewers,

Thank you for the five separately conducted internal role reports and the traced editorial synthesis. The v0.3.0 submission remains frozen. Version 0.3.1 is an additive successor that addresses R1–R8 and DA-M1–DA-M7 without upgrading internal review into external assurance. Locations below refer to the revised Markdown source and its generated PDF; executable evidence is identified by path and regression name.

## Priority 1 — Required revisions

| # | Original review requirement | Author response and change | Revision location | Verification evidence | Status |
|---|---|---|---|---|---|
| R1 | Make finite closure, tail, totality, model scope, \(\Gamma\), and inherited dependencies journal-complete | Added formal density, rational-instance and real-policy domains; common-origin fixed-interval scope; zero-\(K_i\) admissibility; numbered pair-tail, finite-generation, triple-tail, strict-improvement, totality, monotonicity, and robustness results. Quantified one-sided continued-fraction and simultaneous-Dirichlet cap restoration. Split direct three-item claims from conditional parent/resource claims. | Paper §§2–3; `docs/three_item_oracle_note.md` §§1, 7 | `test_generator_matches_bruteforce_small_cutoffs`; `test_second_complexity_tail_inequality`; all witness/verifier tests | RESOLVED |
| R2 | Add strict certificate schema, safe parsing, canonical replay, negative controls, and precise independence language | Added versioned load-bearing schema validation with required/allowed fields, exact lengths/types, uniqueness, SHA-256 form, and unknown-field rejection. Replaced unrestricted frequency `sympify` with an exact grammar limited to rational arithmetic and `sqrt`. Verification reports use package-relative identifiers. Declared canonical-JSON byte identity and same-producer shared-substrate boundary. | `src/jrp3/verify.py`; `src/jrp3/extensions.py`; paper §5; `ASSURANCE.md` | `test_strict_certificate_schema_rejects_reviewed_shapes`; `test_seeded_schema_fuzz_rejects_unknown_and_missing_fields`; `test_verification_reports_are_extraction_path_independent`; numeric/structural controls | RESOLVED |
| R3 | Correct bibliography, expand lineage, audit source use, and calibrate priority/dependency status | Corrected Winter–Van Vuuren, Suemitsu et al., Creemers–Boute, Peng–Wang–Wang, and canonical predecessor metadata; added Roundy, Teo–Bertsimas, Cohen-Hillel–Yedidsion, peer-reviewed Segev context, and the adjacent Creemers–Stephan preprint with an explicit non-match disposition. Added the requested model/policy/constraint/exactness comparison table and field-design sources. | Paper §1.1 and References; `SOURCES.md`; `CITATION_AUDIT.md` | DOI/publisher/SSRN readback recorded in `CITATION_AUDIT.md` | RESOLVED |
| R4 | Calibrate title/abstract/conclusion, robustness, active family, derived percentages, and candidate wording | Retitled as a “Candidate Exact” oracle; removed 42.6709% from abstract/conclusion and package rhetoric; retained only an explicitly denominated 4.6588% descriptive cross-source comparator. Renamed boxes as certified inner radii under simultaneous relative \(H\) perturbation, with fixed/varied/omitted parameters. Retained the stationary calculation solely as a numerical/algebraic discovery guide. | Title, Abstract, §§1, 4.2–4.5, 9–10; `ASSURANCE.md`; `README.md` | Release-wide phrase audit; `analysis/active_envelope_analysis.json` claim boundary | RESOLVED |
| R5 | Repair event closure, units, joint uncertainty, field design, and evidence states | Added three-way event-closure decision (owned event; frozen background calendar plus marginal cost; software-only). Required consistent units, joint uncertainty over all costs/caps/event attribution/calendars, rank/regret/feasibility/service/worst-case outcomes, and a design-adequacy rather than fixed-duration rule. Added assignment, interference, carryover, power/precision, noncompliance, missingness, multiplicity, cost boundary, stopping authority, and RACI. | Paper §§6–8; `LOGISTICS_DEPLOYMENT_PROTOCOL.md` Gates 0–6 and RACI | Protocol phrase/numbering audit; source-use audit for field-design references | RESOLVED |
| R6 | Separate frozen regression fixtures from instance-specific operational portfolios and bind completeness | Replaced hard-coded membership with exhaustive generation across every primitive triple and all four boundary regimes. The v3 artifact binds tolerance, class counts, membership, regrets, threshold, and the closing tail; a separate verifier reconstructs the whole document. All application surfaces mandate regeneration for each fitted instance. | `portfolio.py`; `build_extensions.py`; analysis artifact/receipt; paper §4.4 and §6.3; protocol Gate 2 | complete reconstruction plus load-bearing mutation tests over both 49,981-triple fixtures | RESOLVED |
| R7 | Add accountability, disclosures, and append-only internal-review ledger while preserving Anonymous | Preserved Anonymous as scholarly creator; recorded Ian Pitchford as non-author research director, maintainer, publisher, and correction-routing contact. Added CRediT-style contributions, funding, competing interests, ethics, data/code availability, AI-use disclosure, component licence map, round-one review records, response matrix, and confirmation-review directory. | Paper disclosure sections; `PROVENANCE.md`; `LICENSE*`; `PUBLIC_DOMAIN.md`; `reviews/round-1/`; `reviews/confirmation/` | Manifest and review-record hash verification; public issue route inserted with repository identity | RESOLVED |
| R8 | Reconcile versions, counts, gates, paths, environment, CFF, PDF, and receipts | Advanced mutable identity to v0.3.1 and the deterministic inventory to 21 tests; made preflight package-relative; removed the premature CFF release date; corrected review paths; rebuilt and visually rechecked the PDF; added release-wide consistency and generated-byte gates. Public-identity fields remain unset until their public readback exists. | Whole package; CFF; intake; README/status/receipts; review ledger; scripts; PDF | final ordinary/optimized/fresh-extraction, manifest, PDF, and consistency receipts | RESOLVED SUBJECT TO FINAL FREEZE |

## Devil's Advocate issues

| # | Challenge | Resolution | Location | Status |
|---|---|---|---|---|
| DA-M1 | The finite search might not be total, so “exact” could be only finite evidence | Added Proposition 4 and Theorem 1 with explicit approximation rates, upward cap restoration, intersection lower orders, and stopping quantifiers; retained candidate/external-review boundary | Paper §§3.3–3.6; oracle note §7 | RESOLVED |
| DA-M2 | The verifier could share the producer's blind spots | Exposed shared primitives and same-producer status; strengthened schema, safe grammar, mutations, and canonical extraction tests; did not claim independent reimplementation | Paper §5; `ASSURANCE.md`; verifier/tests | RESOLVED |
| DA-M3 | A selected triplet may not own the common event | Added complete event ownership, conditional frozen-background/marginal-cost treatment, or software-only exclusion | Paper §6.1; protocol Eligibility/Gate 0 | RESOLVED |
| DA-M4 | Holding-cost radii could be read as maximal or operational robustness | Renamed and scoped as conservative certified inner \(H\)-only boxes; listed fixed and omitted variables; required separate joint uncertainty | Paper §4.4; protocol Gate 3 | RESOLVED |
| DA-M5 | The five-policy list could be cherry-picked and transferred | Rebuilt from the full certified enumeration and tail; labelled frozen regression fixture; operational instances regenerate | Portfolio artifact/code/test; paper §6.3 | RESOLVED |
| DA-M6 | The 42.6709% interval rhetoric used a questionable endpoint/basis | Removed it everywhere substantive; retained only the clearly denominated 4.6588% lower-to-preprint-upper separation | Abstract, §§1 and 4.5, Conclusion | RESOLVED |
| DA-M7 | Field recommendations could outrun identification and stakeholder accountability | Added design adequacy, interference, carryover, precision, noncompliance, missingness, multiplicity, RACI, and untested evidence state | Paper §§7–8; deployment protocol | RESOLVED |

## Summary of changes

- Required editorial items addressed: **8/8**.
- Devil's Advocate Major items addressed: **7/7**.
- New deterministic tests: **6**, bringing the suite from 15 to **21**.
- Bibliographic records materially corrected: **4**; foundational/field-design records added and verified: **10**.
- New public-package governance objects: citation audit, response letter, revision tracker, CC0/MIT split licence, and confirmation-review ledger.
- Assurance unchanged where evidence is absent: independent rerun, independent reimplementation, formal verification, external specialist review, editorial peer review, and operational impact remain not established.

The single allowed confirmation review returned Major Revision with no P0 and six consolidated P1 groups. Its reports and decision remain frozen. The subsequent changes are bounded deterministic repairs to representation binding, assurance labels, portfolio completeness, replay-byte evidence, package/PDF consistency, and governance records; `reviews/confirmation/DETERMINISTIC_REPAIR_CLOSURE.md` records the Editor-only closure without claiming a third scientific review.

Sincerely,  
**Anonymous**
