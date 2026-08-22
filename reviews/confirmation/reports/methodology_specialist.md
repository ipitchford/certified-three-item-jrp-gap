# Methodology specialist confirmation report

## Review identity, scope, and limitation

- **Target:** `exact-three-item-jrp-applications-v0.3.1-candidate`
- **Role:** methodology/computation specialist for the single Evidence Press confirmation round
- **Review boundary:** frozen candidate, embedded round-one methodology and Devil's Advocate reports, round-one editorial requirements, and the response/revision records only
- **Conflict/independence statement:** I did not read another confirmation report, communicate with another reviewer, edit the candidate, or use a sub-reviewer. This is model-mediated internal editorial evidence. It is not unaffiliated specialist review, journal peer review, independent rerun, independent reimplementation, or formal verification.
- **Confidence:** **5/5** on the code, certificate, replay, portfolio, manifest, and package-consistency findings; **4/5** on the prose totality proof because it has not received unaffiliated number-theoretic review or proof-assistant formalisation.

## Frozen-target verification

All four required hashes match `FROZEN_TARGET.md` exactly.

| Object | Observed SHA-256 | Result |
|---|---|---|
| `frozen-submission.zip` | `b51486d01b7aaddfad108c10f8ddbc8aa4fdfe27e3dc27d040b64e6a649ecdf3` | PASS |
| `MANIFEST.sha256` | `fa5a3537a362cde4b154fbe69accc453bf813eacf19d73867b6085e60c507199` | PASS |
| paper Markdown | `4f5c2d29df62eca54b9f38d95505785acf84f88ef5cb5f4cb876cfbc16cfa6ee` | PASS |
| paper PDF | `87f990da25b3cdaa4dfec4c44456ab0840b70a3a3f9dd256e937e8e887a73985` | PASS |

The manifest contains 123 entries, and a read-only `shasum -a 256 -c MANIFEST.sha256` check passed every entry. The archive has the expected single candidate root and no cache debris in its file list.

## Read-only computation and document checks

- The headline certificate was recomputed directly in ordinary Python and with `PYTHONOPTIMIZE=2`; both runs returned `passed: true`, 49 checks, and exact gap `7732648297718008589674913778809/6731480890380196637385597557508`.
- Four focused regressions passed in a read-only run: reviewed schema mutations, seeded missing/unknown-field mutations, extraction-path-independent verification reports, and registered portfolio enumeration/tail completeness.
- The frozen full-run receipt records 19 tests in ordinary, optimized, and clean-extraction runs (`REPLAY_RECEIPT.json`, ordinary/optimized/clean-extraction blocks). I did not run `scripts/reproduce.sh` in the immutable target because it rewrites generated candidate artifacts.
- `pdfinfo` confirms the frozen PDF title, Anonymous author, A4 format, 15 pages, and 134,549 bytes. The raw-TeX preflight returned zero findings. Extracted text contains the candidate-qualified title, Theorem 1, the 49,981 count, disclosures, and the `Evidence Press unrefereed candidate · v0.3.1` footer. The package's page-by-page visual inspection remains a producer receipt rather than a fresh visual review by this role.
- The Markdown, certificate, verification JSON, replay receipt, and PDF agree on the headline optimum, relaxation, ratio, cutoff `S=21`, 49,981 primitive triples, 15 PDF pages, three point certificates, and sixteen robustness vertices.

## Focused methodology assessment

### Finite closure, totality, exactness, and attainment

The revision supplies the previously missing mathematical chain in the paper itself. Section 2 defines rational instances, real common-origin fixed-interval policies, density, the infimum (C^*), attained relaxation (L), and Γ. Sections 3.1–3.6 then give an exhaustive commensurability partition; exact fixed-pattern optimization; pair-tail closure; the finite second-pair-complexity generator; the global triple tail; strict interior improvement; and the terminating finite oracle. The oracle note §7 expands the one-sided continued-fraction and simultaneous-Dirichlet cap-restoration arguments.

I found the logic coherent. Proposition 2 bounds every generated coordinate by ((S-1)^2). Proposition 3 correctly retains the least-complex pair and bounds the other two intersections, after which frequency scaling yields the stated tail. Proposition 4 provides a fully commensurable policy strictly below the boundary minimum, so the tail factor's convergence to one forces finite termination. Theorem 1 then excludes omitted triples and all boundary regimes and establishes attainment by an enumerated primitive triple. The strict numerical tail margin in the headline certificate also excludes an omitted tie. No new mathematical P0 contradiction or counterexample was identified.

### Verifier, schema, parser, and negative controls

The revision materially improves shape validation: exact list lengths, canonical pair coverage, duplicate rejection, required/allowed fields, safe identifiers, rational tokens, and the reviewed malformed shapes are enforced (`src/jrp3/verify.py`, especially lines 26–245; `tests/test_oracle.py`, lines 253–333). Canonical certificate identifiers are package-relative. The paper and assurance ledger correctly disclose the same-producer shared algebra/parser substrate.

However, the verifier does not bind all duplicated exact representations. `_validate_expression_payload` parses `expression` but does not compare it with an accompanying `rational`; `_parse_expr` then prefers `rational` (`src/jrp3/verify.py`, lines 67–79 and 275–278). The main verification similarly constructs the declared optimum from `kind`/`value` and the gap from `_parse_expr` (`src/jrp3/verify.py`, lines 535–558). In a read-only in-memory control, changing `integrality_gap.expression` to `999` passed schema validation while the verifier continued to read the unchanged rational value. The public object can therefore be internally contradictory and still receive a passing report.

The expression parser prevents arbitrary identifiers and obvious code injection, but it has no input-length, nesting, integer-size, or operation budget and accepts `**` because `*` is allowed by the character filter. That is a residual resource-exhaustion surface for untrusted public certificates.

### Generator, tail, and portfolio completeness

The reduced-ratio generator and tail code mirror the written proof, and the bounded brute-force generator test plus the direct 49,981-policy runs are meaningful producer-side evidence. `scripts/build_extensions.py` now actually constructs the two five-policy fixtures by enumerating all primitive triples at the certified cutoff and requiring the tail to lie above the registered tolerance threshold (`policy_portfolio`, lines 165–253). The resulting artifact's observed values are coherent: five included, 49,976 excluded, next enumerated regret well above (10^{-6}), all boundary minima far above threshold, and the omitted tail above threshold.

The completeness artifact is nevertheless only partly verifier-bound. `test_registered_portfolios_are_enumeration_and_tail_complete` recomputes primitive membership, compares the declared multiplier set, checks the recomputed tail against the recomputed threshold, checks one enumeration count, and trusts a Boolean (`tests/test_oracle.py`, lines 190–218). It does not verify the recorded boundary comparator costs/regrets, minimum excluded regret, included/excluded counts, stored threshold, policy costs/frequencies/regrets, winner/optimal-policy fields, or that every boundary class is outside tolerance. Those fields can be corrupted without that named regression failing. This falls short of R6's requirement for a verifier-checked completeness object, even though I found no evidence that the frozen five-policy membership itself is wrong.

### Replay, paths, receipts, manifest, and PDF consistency

Ordinary/optimized exact recomputation is sound for the headline certificate, and all current manifest entries pass. The 44-artifact ordinary/optimized byte-identity claim is recorded, but the hash lists or an aggregate comparison receipt are not shipped. More importantly, `scripts/reproduce.sh` rebuilds artifacts and runs tests but performs no manifest/expected-output comparison after generation (lines 7–21). `REPLAY_RECEIPT.json` explicitly records only `manifest_entries_checked_before_replay` for the clean extraction (lines 35–41). The extraction-path test compares one point-verification report across two temporary roots, not the complete generated artifact set (`tests/test_oracle.py`, lines 315–332). Thus clean-extraction functional replay is evidenced, but post-regeneration byte identity with the frozen package is not.

R8 also has visible cross-document drift. `site/papers/certified-three-item-jrp-gap/meta.draft.json` remains `0.3.0-candidate` and says fifteen tests (lines 10 and 47), while the frozen candidate is v0.3.1 with nineteen tests. Its public-facing abstract also drops the paper's `candidate exact oracle` qualification. `CITATION.cff` sets `date-released: 2026-08-22` even though the package states that no successor release exists. `RESEARCH_EXTENSION_REPORT.md` still says final replay/PDF receipts “will be frozen” and “remain” gates after those receipts were frozen. The README embeds a workstation-specific preflight path (`/Users/admin/.agents/...`), and the environment record omits the requested locale and dependency hashes/strong lock. These facts contradict the response's claim that all mutable package identity, counts, paths, CFF facts, and receipts were reconciled.

## Trace of round-one requirements

| Item | Status | Exact evidence and confirmation judgment |
|---|---|---|
| **R1** | **fully addressed** | Paper §2.1 and §§3.1–3.6; oracle note §§7. Definitions, finite generation, pair/triple tails, strict improvement, totality, attainment, scope, and imported dependencies are now explicit. No new P0 mathematical defect found. |
| **R2** | **partly addressed** | Strict shape and reviewed mutations are implemented in `src/jrp3/verify.py` and `tests/test_oracle.py`; same-producer wording is prominent. Exact duplicate representations are not cross-bound, the parser lacks resource bounds, and fresh-extraction byte identity is not verified after replay. |
| **R3** | **fully addressed** | Paper §1.1 and References; `SOURCES.md`; `CITATION_AUDIT.md`. Corrected metadata, source-status boundaries, dependency table, and calibrated targeted priority protocol are present. This role did not independently revisit external sources. |
| **R4** | **partly addressed** | The paper title, abstract, §§4.2–4.5, limitations, and conclusion correctly use candidate, inner-radius, stationary-guide, and descriptive-comparator boundaries. The shipped site metadata still uses stale/unqualified v0.3.0 language, so the release-wide criterion fails. |
| **R5** | **fully addressed** | Paper §§6–8 and `LOGISTICS_DEPLOYMENT_PROTOCOL.md` Gates 0–6 supply event closure, unit semantics, joint uncertainty, design adequacy, evidence states, stop rules, and RACI. Operational value remains untested. |
| **R6** | **partly addressed** | `scripts/build_extensions.py`, `analysis/policy_portfolio.json`, paper §6.3, protocol Gate 2, and the portfolio regression establish the actual finite membership route. The claimed completeness object is not fully schema- or verifier-bound, especially for boundary and exclusion-margin fields. |
| **R7** | **fully addressed for the frozen pre-confirmation target** | `PROVENANCE.md`, paper disclosures, `ASSURANCE.md`, licences, and `reviews/round-1/` preserve Anonymous, identify correction/accountability roles, disclose AI/funding/interests, and call review internal. Confirmation reports and synthesis must be appended after this round as a process step. |
| **R8** | **partly addressed** | Four frozen hashes, 123-entry current manifest, 15-page PDF, raw-TeX preflight, ordinary/optimized recomputation, and canonical machine-readable certificate paths pass. Site metadata, test count, release date, future-tense receipts, environment closure, README path, and post-replay equality remain inconsistent or incomplete. |

## Trace of Devil's Advocate Major items

| Item | Status | Confirmation judgment |
|---|---|---|
| **DA-M1** | **fully addressed** | The finite search is now connected to an explicit totality/attainment theorem in paper §§3.3–3.6 and oracle note §7. Candidate/external-audit limits remain visible. |
| **DA-M2** | **partly addressed** | Shared-provenance limits are disclosed and schema/mutations are stronger, but contradictory exact representations can pass and the CLI/test still contain independent-verifier wording. No independence dimension may be upgraded. |
| **DA-M3** | **fully addressed** | Paper §6.1 and protocol Eligibility/Gate 0 require owned-event, frozen-background/marginal-cost, or software-only treatment. |
| **DA-M4** | **fully addressed** | Paper §4.4 and protocol Gate 3 call the boxes conservative certified inner (H)-only regions, not maximal or operational robustness. |
| **DA-M5** | **partly addressed** | Actual primitive-triple membership is exhaustive at the registered tolerance and operational regeneration is mandated, but the boundary/exclusion completeness fields are not fully verifier-bound. |
| **DA-M6** | **fully addressed** | The 42.6709% rhetoric is absent from substantive successor materials; §4.5 gives only the explicitly denominated 4.6588% descriptive cross-source comparator. |
| **DA-M7** | **fully addressed** | Paper §7–8 and the protocol add omitted-constraint, identification, stakeholder, RACI, and evidence-state boundaries; no field impact is claimed. |

## New issues

### P0 critical

None found.

### P1 major

1. **Certificate representations are not internally bound.** A false `expression` can coexist with a correct `rational`/`value` and still pass. Remedy: define one authoritative exact representation or enforce equality among every present exact field; validate any retained decimal/minimal-polynomial field according to its declared status; add single-field contradiction mutations.
2. **Clean-extraction replay does not establish the declared byte-identity target.** The frozen receipt checks the manifest only before replay, and `reproduce.sh` has no post-generation manifest/expected-output gate. Remedy: from a clean extraction, preserve expected output hashes, run ordinary and optimized replay, and compare every declared generated artifact after each run; ship the per-file or aggregate hash receipt.
3. **Portfolio completeness is not fully verifier-bound.** Primitive membership and the tail inequality are checked, but boundary exclusion, next-policy margin, stored thresholds/counts, and policy payloads are not. Remedy: add a strict portfolio schema and a dedicated verifier that recomputes the entire completeness certificate and rejects mutations of every load-bearing field.
4. **R8 whole-package identity and release facts remain inconsistent.** The site draft is v0.3.0/15 tests, `CITATION.cff` asserts a release date before a successor release exists, and other shipped records retain stale future-tense/path/environment facts. Remedy: reconcile all public/draft records, remove the premature CFF release date, replace workstation paths with portable commands, record locale and dependency hashes/strong lock, rerun the PDF/replay gates, and rebuild the manifest/archive.

### P2 minor

1. **Residual independence terminology:** `src/jrp3/verify.py` describes the CLI as “Independently verify,” and `tests/test_oracle.py` retains `test_independent_verifier`, despite the round-one instruction to use “solver-independent producer verifier.” Rename both and retain the surrounding assurance disclaimer.
2. **Parser availability hardening:** the allowed-character filter has no size/depth/operation bounds and permits exponentiation via `**`. Replace generic `parse_expr` ingestion with a small bounded grammar/AST evaluator or enforce strict limits and disallow operations outside rational arithmetic plus square root.

### P3 editorial

1. `RESPONSE_TO_REVIEWERS.md` thanks the “five independent reports.” To avoid collision with fixed Evidence Press assurance terminology, say “five separately conducted internal role reports” or equivalent.

## Recommendation

**Major Revision — confidence 5/5.** The core candidate mathematics and headline finite computation are not rejected: R1/DA-M1 are now credibly addressed, the exact witness recomputes in ordinary and optimized mode, and I found no new P0 scientific defect. Acceptance is nevertheless barred by multiple new P1 issues and by R2, R4, R6, and R8 remaining only partly addressed. The Evidence Press state should remain `HOLD_FOR_REPAIR`.

The necessary repairs are targeted verifier/replay/metadata controls rather than a new scientific claim. They should be closed by deterministic regression, post-regeneration hash evidence, and editor verification; a third full model-mediated scientific review is not warranted unless the mathematical statement, proof, evidence set, or conclusion changes.
