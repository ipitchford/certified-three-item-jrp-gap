# Confirmation Review — Domain Specialist

## Review identity and boundary

- **Candidate:** `exact-three-item-jrp-applications-v0.3.1-candidate`
- **Role:** joint-replenishment domain specialist
- **Round:** one permitted confirmation review after Major Revision
- **Scope:** model class, JRP terminology, common-origin fixed-interval interpretation, boundary regimes, two-item lineage, fixed-item/resource extensions, literature/priority calibration, and consistency between conclusions and proof/certificate status
- **Conflict/limitation:** no conflict known. This is model-mediated, producer-coordinated **internal editorial review**, not unaffiliated specialist review, independent reproduction, formal verification, or journal peer review. I reviewed only the frozen package and its included round-one record. I did not use the other confirmation reports or externally re-verify literature metadata.
- **Confidence:** **4/5**

## Frozen-target verification

All four required hashes match `FROZEN_TARGET.md` exactly:

| Object | Expected and observed SHA-256 | Result |
|---|---|---|
| `frozen-submission.zip` | `b51486d01b7aaddfad108c10f8ddbc8aa4fdfe27e3dc27d040b64e6a649ecdf3` | MATCH |
| package `MANIFEST.sha256` | `fa5a3537a362cde4b154fbe69accc453bf813eacf19d73867b6085e60c507199` | MATCH |
| paper Markdown | `4f5c2d29df62eca54b9f38d95505785acf84f88ef5cb5f4cb876cfbc16cfa6ee` | MATCH |
| paper PDF | `87f990da25b3cdaa4dfec4c44456ab0840b70a3a3f9dd256e937e8e887a73985` | MATCH |

The 123-entry package manifest also passes a read-only `shasum -a 256 -c MANIFEST.sha256` check. I did not run rebuilding scripts because they would mutate the frozen target; replay assessment therefore uses the frozen receipt plus read-only inspection of the implementation, verifier, tests, and generated records.

## Domain assessment

### Model and terminology

The revised paper now defines a rational-data instance, real positive periods, nonnegative item-specific setup coefficients, positive holding coefficients, positive rational frequency caps, the long-run counting density, the exact infimum, the relaxation, and the rational-instance supremum `Gamma_(n,box)` (paper §§2.1–2.2). “Common-origin fixed-interval policy” is the right term for the explicitly restricted class: item `i` acts on `T_i Z_{>0}`, every stream has phase zero, and an incommensurable union is not incorrectly called globally periodic. This is narrower than several policy classes called periodic JRP in the literature, but the limitation is now visible in the abstract, model, logistics gate, and limitations.

Zero `K_i` is admissible by definition and is highlighted rather than hidden. That boundary choice is mathematically important for the strongest witness and fixed-item monotonicity. It does reduce immediate operational representativeness, but the editorial arbitration allowed claim narrowing instead of requiring a positive-`K_i` witness, and the main paper now treats the result as a synthetic model stress fixture.

### Boundary regimes and exact-oracle claim

The commensurability relation is an equivalence relation, so the three partitions in paper §3.1 and oracle note §2 are exhaustive. The fully commensurable reduction to primitive triples and `A/t + Bt`, the one-pair closures, the three-singleton closure, the pair tail, the second-smallest-pair-complexity generator, and the global triple tail are coherently connected (paper Propositions 1–4 and Theorem 1; oracle note §§3–7). The cap-restoring one-sided approximation arguments address the most important closure concern. The strict-interior result gives the quantified stopping event needed for totality. I found no new domain-level counterexample or scope mismatch in this chain.

The code mirrors the claimed finite objects: `primitive_triples` generates the declared second-complexity set; the verifier independently reconstructs the reduced-ratio generator, boundary minima, finite optimum, and tails; the small-cutoff brute-force and bounded tail regression test the source-to-encoding bridge. This remains same-producer evidence and does not prove the prose totality theorem independently, a boundary stated correctly in paper §5 and `ASSURANCE.md`.

### Two-item predecessor, fixed item count, and resource extension

The three-item generator, tails, totality argument, rational witness, and fixed-`n` monotonicity are correctly presented as direct successor claims, independent of the predecessor proof (paper §2.2). The appended-item argument in paper §4.3/oracle note §9 is sound for the declared rational-instance supremum: deleting the added zero-setup item cannot increase the old exact cost, while a rational positive frequency below the old relaxed maximum makes the added relaxed holding cost tend to zero. Thus the candidate lower bound propagates to each fixed `n >= 3` within the same independent-cap class.

The broader arbitrary-resource-row reading is consistently conditional on the predecessor's unrefereed cap-reduction argument, and no arbitrary-row executable oracle is claimed. The `5/(6 ln 2)` value is identified as an algorithmic comparator from Segev's arXiv v1 resource-constrained preprint rather than as the determined gap or certificate input. These are appropriate dependency boundaries.

### Literature and priority

The corrected records in the paper, `SOURCES.md`, and `CITATION_AUDIT.md` are internally aligned for the cited Roundy, Teo–Bertsimas, Cohen-Hillel–Yedidsion, Segev, Creemers–Boute, Peng–Wang–Wang, and applications/field-design sources. The priority protocol records dates, routes, object-level and equivalent-form queries, tracing, exclusions, and the calibrated result “targeted search found no match.” The paper does not turn that absence into proof of novelty or priority and limits its conclusion to the known producer-side lower-bound frontier.

The domain repair is not complete, however: round-one R2 and editorial R3 asked for a model-by-model comparison table covering model class, policy class, constraints, exact/approximate status, and contribution. Paper §1.1 supplies a short synthesis plus a claim-dependency table, but not that requested comparison. The adjacent Creemers–Stephan special-cases preprint specifically flagged by R2 is also not discussed or dispositioned. This does not refute the result, but it leaves R3 only partly addressed.

## Trace of required revisions R1–R8

| Item | Status | Confirmation evidence and judgement |
|---|---|---|
| **R1** | **Fully addressed** | Paper §§2–3 gives formal domains, density, common-origin policy scope, numbered pair/generator/triple/strict-improvement/totality results and proofs; oracle note §§1–7 gives the same dependency chain. The direct three-item theorem is separated from conditional parent/resource claims. |
| **R2** | **Fully addressed** | Paper §5 and `ASSURANCE.md` retain same-producer/shared-substrate language. `verify.py` enforces a strict versioned schema and restricted exact-expression grammar; `test_oracle.py` contains structural mutation, fuzz, and extraction-path regressions. Frozen ordinary, optimized, and clean-extraction receipts report 19 tests, with 44 JSON artefacts byte-identical between modes. This is producer consistency, not independence. |
| **R3** | **Partly addressed** | Bibliographic corrections, source-status labels, dependency table, source-use audit, and a calibrated priority protocol are present (paper §1.1 and References; `SOURCES.md`; `CITATION_AUDIT.md`). The specifically required model/policy/constraint/exactness comparison table is absent, and the R2-flagged adjacent Creemers–Stephan preprint is neither compared nor dispositioned. |
| **R4** | **Partly addressed** | The main paper is well calibrated: “candidate exact,” fixed/varied/omitted robustness variables, nonmaximal inner radii, stationary guide only, and no 42.6709% headline (title, Abstract, §§4.2–4.5, 9–10). But `RESEARCH_EXTENSION_REPORT.md` §Quantitative interpretation still calls 42.6708886811% a reduction of the predecessor interval, and `results.json` still emits `predecessor_interval_reduction_percent`, contradicting the response's claimed package-wide removal. |
| **R5** | **Fully addressed** | Paper §§6–8 and `LOGISTICS_DEPLOYMENT_PROTOCOL.md` add event ownership/frozen-background/software-only closure, consistent-unit mappings, joint uncertainty, simulation outcomes, design adequacy, field-identification requirements, stop authority, RACI, and an untested operational evidence state. |
| **R6** | **Partly addressed** | `analysis/policy_portfolio.json`, `build_extensions.py`, and `test_registered_portfolios_are_enumeration_and_tail_complete` bind all 49,981 enumerated triples, a `10^-6` tolerance, exclusion margin, boundary comparators, and a closing tail for both frozen fixtures. Paper §6.3 correctly requires fitted-instance regeneration. Yet `README.md` §What is new, `RESEARCH_EXTENSION_REPORT.md` §§3/Stop-go, the portfolio `purpose`, and site draft metadata continue to offer the frozen five as a logistics/simulation handoff. That conflicts with the required regression-fixture/instance-specific split. |
| **R7** | **Fully addressed** | Paper disclosures, `PROVENANCE.md`, licences, public correction route, and round-one ledger preserve Anonymous as creator, Ian Pitchford as non-author maintainer/correction router, and internal review as non-external evidence. Confirmation remains pending rather than falsely recorded as complete. |
| **R8** | **Partly addressed** | Version, 19-test count, three point certificates, sixteen vertex certificates, seven gates, 15-page PDF, hashes, manifest, and replay modes are aligned. However, the unresolved R4/R6 narrative contradictions defeat whole-package semantic consistency, and `README.md` §Reproduce still ships a workstation-specific `/Users/admin/...` command despite the absolute-path removal requirement. |

## Trace of Devil's Advocate items DA-M1–DA-M7

| Item | Status | Confirmation evidence and judgement |
|---|---|---|
| **DA-M1** | **Fully addressed** | Paper Propositions 1–4 and Theorem 1 state the finite-generation, boundary, tail, strict-improvement, stopping, and attainment chain with quantifiers; oracle note §§4–7 supplies the detailed derivation. External audit remains openly absent. |
| **DA-M2** | **Fully addressed** | Schema/parser/mutation/path controls are materially strengthened, while paper §5, `ASSURANCE.md`, and `CLAIMS.json` explicitly deny independent rerun/reimplementation/formalisation. No assurance upgrade is made from shared-substrate agreement. |
| **DA-M3** | **Fully addressed** | The editorially permitted resolution was claim narrowing rather than a positive-`K_i` witness. Paper §§4.4, 6–9 confines the boundary witness to synthetic stress/regression use and requires event closure and joint operational uncertainty. |
| **DA-M4** | **Fully addressed** | Paper §4.4 calls the boxes conservative certified inner radii under simultaneous relative `H` perturbation, lists fixed/varied/omitted inputs, and denies maximal-chamber or operational-uncertainty meaning. |
| **DA-M5** | **Partly addressed** | The frozen fixture's enumeration/tail completeness is now machine-regressed and the paper requires fitted-instance regeneration. Residual package/site language nevertheless tells readers to carry or simulate the fixed five-policy portfolio, so the transfer risk remains. |
| **DA-M6** | **Partly addressed** | The main paper removes 42.6709% from abstract/conclusion and retains only the explicitly denominated 4.6588% cross-source comparator. The challenged 42.6709% “predecessor interval reduction” survives in `RESEARCH_EXTENSION_REPORT.md` and `results.json`, contrary to the response. |
| **DA-M7** | **Fully addressed** | Paper §§7–8 and the deployment protocol state that field value is untested and require semantic closure, instance-specific generation, omitted-constraint simulation, assignment/interference/carryover/precision planning, noncompliance/missingness/multiplicity controls, RACI, and stopping authority. |

## Confirmation findings

### P1 — Residual claim-calibration failure (R4 / DA-M6 / R8)

The response says the 42.6709% metric was removed from package rhetoric and everywhere substantive (`RESPONSE_TO_REVIEWERS.md`, R4 and DA-M6). It remains as “Reduction of the predecessor lower-to-upper interval: 42.6708886811%” in `RESEARCH_EXTENSION_REPORT.md` §Quantitative interpretation and as `predecessor_interval_reduction_percent` in `results.json`. The original endpoint-direction objection is therefore still present on shipped human- and machine-readable surfaces. This is a release-blocking residual Major issue, although it does not invalidate the exact three-item certificate.

**Required remedy:** delete the metric from all package and site surfaces, or provide its exact endpoint formula, use correctly directed certified endpoints, and label it a non-theorem descriptive cross-source diagnostic everywhere. The response/status matrix must then say what was actually done.

### P1 — Residual frozen-portfolio transfer risk (R6 / DA-M5 / R8)

The main paper correctly says the five policies are frozen regression fixtures and that each fitted instance must regenerate an exhaustive candidate set (paper §§4.4 and 6.3). But `README.md` calls them a “five-policy logistics portfolio”; `RESEARCH_EXTENSION_REPORT.md` says real logistics evaluation should carry the small portfolio and explicitly gives a GO for using “the five-policy portfolio” in simulation/shadow evaluation; `analysis/policy_portfolio.json` describes an operational handoff; and the site draft promotes a five-policy logistics portfolio. These release-facing statements reintroduce the exact transfer error the repair was meant to eliminate.

**Required remedy:** reserve the frozen five solely for regression of the two synthetic instances. Every application-facing surface must say that a fitted instance regenerates and verifier-checks its own policy set under a preregistered tolerance and operational feasibility rules.

### P2 — Incomplete literature-comparison deliverable (R3)

The source audit and priority calibration are materially improved, but the required comparison table across model class, policy class, constraint class, exact/approximate status, and contribution is absent. The adjacent Creemers–Stephan special-cases preprint identified in R2 is also not discussed or explicitly excluded. This is a Minor scholarly-positioning defect, not evidence of prior art by itself.

### P2 — Two-item predecessor status is internally inconsistent

Paper §1 and `SOURCES.md` describe an exact/narrow two-item interval and use its producer-certified unrefereed upper endpoint. In contrast, oracle note §Result says the predecessor reports “the exact two-item independent-cap constant,” and the site body says Evidence Press certified “the exact two-item cap constant.” The three-item crossing deduction only needs the upper endpoint, so the mathematics survives, but priority/dependency language does not yet satisfy a single calibrated claim ceiling.

**Required remedy:** use one formulation throughout: an unrefereed producer-side two-item candidate with the exact interval/endpoint actually established by its immutable record; distinguish interval, endpoint, and exact constant.

### P3 — Remaining editorial/portability cleanup

- `README.md` §Reproduce contains a user-specific absolute path despite R8's portability requirement.
- The Schulz–Telha and pairwise-alignment bibliography entries still omit explicit years even though R2 asked for consistent years.
- Oracle note §1 uses `Z_{>=0}` while the paper defines epochs with `Z_{>0}`. Density and cost are unchanged, but one convention should be used.

## Recommendation

### **Major Revision** — confidence **4/5**

The core domain and mathematical repairs are substantial, and I found no new P0 scientific defect in the common-origin model, boundary partition, totality argument, fixed-item monotonicity, or certificate linkage. Acceptance is nevertheless unavailable under the confirmation rule because R3, R4, R6, and R8 are not fully addressed and two residual P1 issues remain on release-facing human- and machine-readable surfaces. The appropriate Evidence Press state remains **`HOLD_FOR_REPAIR`**.

The required next work is bounded: reconcile the package-wide interval metric, frozen-portfolio semantics, predecessor status, and literature comparison, then apply deterministic phrase/metadata/manifest checks. Because these repairs should not alter the theorem, instance, certificate, evidence set, or conclusion, they are suitable for editorial verification rather than a third substantive scientific review unless the repair changes scientific bytes or claims.
