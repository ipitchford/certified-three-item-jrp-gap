# Editor-in-Chief Confirmation Review

## Submission and review boundary

- **Candidate:** `exact-three-item-jrp-applications-v0.3.1-candidate`
- **Review:** one permitted confirmation round after the v0.3.0 Major Revision decision
- **Role:** Editor-in-Chief — editorial sufficiency, response traceability, claim ceiling, journal fit, and release suitability
- **Recommendation:** **Major Revision**
- **Confidence:** **5/5** on the release decision
- **Conflict/limitation statement:** I reviewed only the frozen v0.3.1 target and the round-one reports and synthesis packaged inside it. I did not read another confirmation-review report, communicate with another reviewer, modify the candidate, or treat this model-mediated review as external peer review. My mathematical assessment is an editorial logic audit, not a proof-assistant formalisation, unaffiliated specialist audit, or independent reimplementation.

The manuscript is a strong fit for Evidence Press and the revised mathematical argument is materially better than v0.3.0. I found no new P0 contradiction in the theorem, witness, or representative replay evidence. The frozen release package is nevertheless not acceptable as submitted: several round-one P1 requirements remain only partly addressed, and the package contains new or residual P1 conflicts in its public-facing metadata, certificate conclusions, application handoff, and PDF receipt. Under the configured rule that every R1–R8 and DA-M1–DA-M7 item must be fully addressed and no P0/P1 may remain, public release must stay on `HOLD_FOR_REPAIR`.

## Frozen-target and deterministic checks

All four required hashes matched `FROZEN_TARGET.md` before substantive review:

| Object | Recorded SHA-256 | Reviewer result |
|---|---|---|
| `frozen-submission.zip` | `b51486d01b7aaddfad108c10f8ddbc8aa4fdfe27e3dc27d040b64e6a649ecdf3` | MATCH |
| `MANIFEST.sha256` | `fa5a3537a362cde4b154fbe69accc453bf813eacf19d73867b6085e60c507199` | MATCH |
| paper Markdown | `4f5c2d29df62eca54b9f38d95505785acf84f88ef5cb5f4cb876cfbc16cfa6ee` | MATCH |
| paper PDF | `87f990da25b3cdaa4dfec4c44456ab0840b70a3a3f9dd256e937e8e887a73985` | MATCH |

The manifest contains 123 entries and passed `scripts/manifest.py --check` before and after reviewer-side tests. Five representative tests passed in 62.652 seconds: active-envelope witness/equalisation, strict-schema negative controls, extraction-path identity, exhaustive registered-portfolio primitive enumeration/tail closure, and both holding-box verifiers. The certificate and analysis SHA-256 values in `REPLAY_RECEIPT.json` lines 52–62 match the frozen files. The five round-one report hashes and editorial-decision hash also match `reviews/round-1/REVIEW_RECORD.json` lines 16–63.

The PDF has 15 A4 pages, embedded fonts, and zero findings from the supplied raw-TeX preflight. Page-by-page visual review nonetheless found the literal text `qquadH3` inside the Section 4.2 display on PDF page 8 (source equation at `paper/three_item_jrp_gap_and_logistics.md` lines 290–293). PDF text extraction independently finds the same token. This contradicts the frozen statement that all pages passed visual QA in `REPLAY_RECEIPT.json` lines 64–71. It demonstrates why the visual gate cannot be inferred from the raw-TeX scanner.

## Editorial assessment

### Journal fit and significance

The paper now has a coherent primary contribution: a candidate exact oracle for rational three-item independent-cap, common-origin fixed-interval policies; a producer-certified bundled lower-bound witness; a finite-generation and tail architecture; and a carefully bounded logistics research protocol. The rational ratio and the `(3,3,2)` mechanism are specific, auditable, and potentially significant within exact joint-replenishment and relaxation analysis. The paper appropriately leaves the exact three-item and unrestricted constants open (`paper/three_item_jrp_gap_and_logistics.md` lines 421–429).

The manuscript also substantially improves its evidence hierarchy. The model, density, policy class, rational instance domain, and imported dependencies are explicit (`paper/...md` lines 67–105); Propositions 1–4 and Theorem 1 place finite closure and totality in the paper (`paper/...md` lines 138–221); and the applications sections distinguish a synthetic benchmark from field value (`paper/...md` lines 383–419). I found no counterexample to the proof chain in this editorial audit. Its status must remain **candidate theorem**, because external mathematical audit and formalisation remain absent.

### Claim ceiling

The strongest supportable release statement remains:

> An anonymous, unrefereed, producer-side candidate supplies exact finite replay and a candidate proof that the bundled rational instance has the stated common-origin fixed-interval optimum and lower-bound ratio. It does not determine the exact three-item constant, establish novelty or priority, provide independent reproduction or formal verification, or show operational benefit.

The manuscript and `ASSURANCE.md` generally preserve that ceiling. Several generated and public-facing artifacts do not, which is a release blocker rather than a reason to reject the mathematical candidate.

## Trace of required revisions R1–R8

| ID | Confirmation finding | Exact evidence and rationale |
|---|---|---|
| **R1** | **Fully addressed** | The paper defines counting density, rational instances, real common-origin fixed-interval policies, caps, signs, `C*`, `L`, and `Gamma` at lines 67–105. Propositions 1–4 and Theorem 1 cover pair closure, finite generation, triple tail, strict interior improvement, termination, and exact returned value at lines 138–221. Fixed-item monotonicity is stated and proved at lines 310–329. Imported parent claims are separated at lines 54–65 and 103–105. The proof remains a candidate pending external audit, but that is now disclosed rather than omitted. |
| **R2** | **Partly addressed** | Strict load-bearing schema validation, exact three-entry frequencies, safe expression grammar, unknown-field rejection, and exact recomputation appear in `src/jrp3/verify.py` lines 19–245 and 444–574. Negative controls and extraction-path identity appear in `tests/test_oracle.py` lines 220–336. However, the CLI still says `Independently verify` (`src/jrp3/verify.py` line 578), the test remains named `test_independent_verifier` (test line 129), and generated certificates use unqualified `The exact three-item gap` conclusions (`certificates/active_envelope_three_item_gap_witness.certificate.json` line 14). These conflict with the solver-independent/same-producer boundary in `ASSURANCE.md` lines 24–34 and with the response's claim of complete independence-language repair. |
| **R3** | **Partly addressed** | The manuscript now has a related-work/dependency table and distinguishes peer-reviewed context, preprint, parent candidate, and present proof (`paper/...md` lines 54–65). `SOURCES.md` and `CITATION_AUDIT.md` record corrected Winter–Van Vuuren, Suemitsu, Creemers–Boute, and Peng–Wang–Wang metadata and a targeted priority protocol. Residual incompleteness remains: paper references 3 and 4 omit the publication years requested in round one (`paper/...md` lines 441–443), and the adjacent Creemers–Stephan 2026 source explicitly identified for inspection in `reviews/round-1/reports/R2-domain.md` lines 178–184 is neither included nor dispositioned in `SOURCES.md` lines 5–16. Public certificate/site comparisons also say `certified two-item upper endpoint` without keeping the parent's unrefereed producer status adjacent. |
| **R4** | **Partly addressed** | The paper title says `Candidate Exact`; the abstract and conclusion preserve the unrefereed boundary; the denominator table is explicit (`paper/...md` lines 45–52); the active-family stationary point is a discovery guide (`paper/...md` lines 280–308); and the boxes are named certified inner holding-cost radii with fixed/varied/omitted scope (`paper/...md` lines 331–347). But the response's claimed release-wide removal is false: `results.json` line 50 and `RESEARCH_EXTENSION_REPORT.md` lines 85–93 retain `42.670888...%` without the required displayed formula/corrected endpoint audit; certificates say `The exact three-item gap`; and `site/.../meta.draft.json` lines 4–7 uses an unqualified promotional title/abstract and intrinsic four-order `less stable` language. |
| **R5** | **Fully addressed** | Event closure has the required three-way treatment in the paper (`paper/...md` lines 383–390) and protocol (`LOGISTICS_DEPLOYMENT_PROTOCOL.md` lines 20–36). Joint uncertainty, simulation outcomes, design adequacy, assignment/interference/carryover/power/noncompliance/missingness/multiplicity/stopping authority, RACI, and evidence states appear in protocol lines 57–113 and paper lines 399–419. No field or savings claim is made. |
| **R6** | **Partly addressed** | The main paper and protocol correctly separate frozen regression fixtures from instance-specific candidate generation (`paper/...md` lines 391–397; protocol lines 42–55). `analysis/policy_portfolio.json` records all 49,981 primitive triples, five included, minimum excluded regret, all boundary minima, threshold, and a closing tail. The regression test verifies primitive membership and tail closure (`tests/test_oracle.py` lines 190–218), although it does not explicitly assert each boundary minimum exceeds the portfolio threshold. More importantly, stale package surfaces still transfer the five synthetic policies operationally: `RESEARCH_EXTENSION_REPORT.md` lines 83 and 99–100 directs their use in logistics simulation/shadow evaluation; `site/.../body.md` line 45 calls the five-policy portfolio the right handoff; and `site/.../meta.draft.json` lines 7, 31–35, and 68 says the release supplies that portfolio for simulation. |
| **R7** | **Fully addressed, with post-decision sealing still procedural** | Anonymous scholarly creation and Ian Pitchford's non-author maintenance/correction role are explicit in `PROVENANCE.md` lines 3–23 and paper lines 469–483. Funding, competing interests, ethics, data/code availability, contributions, and AI use appear in paper lines 461–483. Round-one reports, hashes, decision, response, and assurance boundary are preserved under `reviews/round-1/`. The present confirmation report and final residual-issue ledger necessarily have to be sealed after this decision; that procedural future step is not a defect in the frozen pre-review target. |
| **R8** | **Partly addressed** | Core v0.3.1 files consistently report 19 tests, three point certificates, 16 vertices, seven Gates 0–6, 123 manifest entries, and a 15-page PDF (`README.md` lines 40–61; `REPLAY_RECEIPT.json` lines 12–71). However, `site/.../meta.draft.json` still declares version `0.3.0-candidate` and 15 tests (lines 10 and 44–47); `CITATION.cff` line 6 declares `date-released` while `STATUS.md` lines 7–9 says no public release; `README.md` lines 57–60 embeds a workstation-specific `/Users/admin/...` command; `reviews/round-1/REVIEW_RECORD.json` lines 56–60 names a nonexistent `editorial/EDITORIAL_DECISION_ROUND_1.md` path even though the matching file sits at the round-one root; and PDF page 8 visibly renders `qquadH3` despite the all-pages-pass receipt. `RESEARCH_EXTENSION_REPORT.md` lines 107–109 also describes receipts/PDF checks as future work although those objects are already frozen. |

## Trace of Devil's Advocate Major items

| ID | Confirmation finding | Exact evidence and rationale |
|---|---|---|
| **DA-M1** | **Fully addressed** | The complete candidate logic chain is now in numbered paper results, including boundary closures, finite generator, tail, strict improvement, and totality (`paper/...md` lines 138–221). External specialist/formal assurance remains visibly open (`paper/...md` lines 421–429). |
| **DA-M2** | **Partly addressed** | Shared primitives and same-producer status are correctly disclosed (`paper/...md` lines 369–381; `ASSURANCE.md` lines 24–34), and schema/mutation/path controls improved. Residual `independent` CLI/test naming and unqualified generated certificate conclusions prevent a release-wide pass. No independent rerun/reimplementation/formalisation was added, and none may be inferred from this confirmation review. |
| **DA-M3** | **Fully addressed under the round-one arbitration** | No positive-`Ki` or field witness was required if applications were narrowed. The paper identifies zero item costs and the synthetic, tuned family (`paper/...md` lines 223–278), limits the boxes to `H`, and makes operational use conditional on event closure, fitted inputs, joint uncertainty, and downstream evaluation. |
| **DA-M4** | **Partly addressed** | The paper and assurance ledger now call the quantities conservative certified inner simultaneous-relative-`H` radii, not maximal or operational regions (`paper/...md` lines 331–347; `ASSURANCE.md` line 15). The public site draft reintroduces the stronger interpretation that the headline witness is simply `more than four orders of magnitude less stable` and uses that as the reason for a five-policy operational handoff (`site/.../meta.draft.json` line 7; `body.md` line 45). |
| **DA-M5** | **Partly addressed** | Exact primitive membership, excluded regret, boundary comparators, and tail are frozen, and the main protocol requires per-instance regeneration. The stale `RESEARCH_EXTENSION_REPORT.md` and site draft still transfer the synthetic five, and the portfolio test does not explicitly bind/assert the boundary comparator exclusion against the threshold. |
| **DA-M6** | **Partly addressed** | The 42.6709% rhetoric is gone from the paper abstract/conclusion, but remains in `results.json` line 50 and `RESEARCH_EXTENSION_REPORT.md` line 91, contrary to `RESPONSE_TO_REVIEWERS.md` lines 20 and 35. Neither retained occurrence displays the required formula and endpoint-direction audit. |
| **DA-M7** | **Fully addressed** | Logistics is explicitly a proposed protocol. Operational value is `untested`; shadow evidence is feasibility, uncontrolled comparisons are associations, and causal claims require a defensible concurrent design and independent methodological review (`paper/...md` lines 411–419; protocol lines 61–71 and 111–113). |

## New and residual issue register

### P0 — Critical

**None identified.** I found no internal arithmetic contradiction, failed representative verifier/test, counterexample to the stated tail inequality, or evidence that the bundled rational witness is numerically false. This is not an external proof validation.

### P1 — Major

1. **P1-1: Release surfaces contradict the accepted application and claim boundary.** The main paper/protocol say the five bundled policies are synthetic regression fixtures and must be regenerated per fitted instance, while the site draft and research-extension report still recommend them for logistics simulation/shadow use. The same stale surfaces retain the disputed 42.6709% metric and use unqualified `exact three-item gap` / `certified upper endpoint` wording. This reopens R4, R6, DA-M4, DA-M5, and DA-M6.

2. **P1-2: Whole-package identity and status reconciliation failed.** The package mixes v0.3.1/19-test records with a v0.3.0/15-test site metadata object, marks an unreleased candidate `date-released`, embeds a workstation path in the public replay instructions, and records a wrong editorial-decision path. This is an unresolved R8 package-integrity gate.

3. **P1-3: The frozen PDF visual receipt is false as stated.** PDF page 8 contains visible `qquadH3`; `pdftotext` confirms the token, while the receipt says all 15 pages passed. The paper PDF must be rebuilt, visually rechecked, rehashed, and propagated through the manifest/archive before release.

4. **P1-4: Same-producer verification is still labelled independent in executable/public artifacts.** `src/jrp3/verify.py` line 578 and test line 129 contradict the declared assurance boundary, while generated certificate conclusions can be read as establishing the exact three-item constant rather than an exact bundled-instance ratio conditional on the candidate theorem. This is an unresolved R2/DA-M2 assurance-language gate.

### P2 — Minor

1. **P2-1: Source-response closure is incomplete.** Add the missing publication years/metadata for the Schulz–Telha and Segev pairwise-alignment references, and include or explicitly disposition the Creemers–Stephan adjacent source requested in round one.

2. **P2-2: Portfolio boundary exclusion is recorded but not directly regression-asserted.** Extend `test_registered_portfolios_are_enumeration_and_tail_complete` to recompute each desynchronised/one-pair minimum and assert it exceeds the registered threshold, binding the artifact's `boundary_comparators` rather than only primitive enumeration and tail.

3. **P2-3: The response package does not answer the suggested revisions individually or provide the requested old/new page map or redline.** Compare `EDITORIAL_DECISION_ROUND_1.md` lines 348–362 with `RESPONSE_TO_REVIEWERS.md` lines 13–45. This does not invalidate the traced P0/P1 repairs by itself, but it weakens editorial completeness.

### P3 — Editorial

1. Rename the stale `AI_INDEX.md` title at line 5 to the v0.3.1 title.
2. Replace the remaining `concavity` docstrings with `affinity` in `src/jrp3/extensions.py` lines 83–90 and 151–152.
3. Fill or retire the blank `reviews/round-1/RESPONSE_MATRIX_TEMPLATE.md`; the filed response letter currently performs the matrix function, while the template still shows every item `pending`.

## Evidence-layer separation

| Layer | What this package supports | What it does not support |
|---|---|---|
| **Candidate theorem** | A journal-readable, producer-authored finite-closure/totality argument and fixed-item consequences | External proof correctness, formal verification, or the exact global three-item constant |
| **Finite replay** | Matching frozen hashes, 123-entry manifest, exact rational certificates, recorded ordinary/optimized/fresh-extraction replay, and five passing representative reviewer-side tests | Independence from shared algebra, theorem assumptions, or producer workflow |
| **Imported facts** | Audited metadata and bounded use of a parent Evidence Press candidate, an arXiv-v1 comparator, and peer-reviewed context | Automatic correctness of imported candidate/preprint results, exhaustive novelty, or priority |
| **Internal editorial review** | Five frozen round-one role reports, synthesis, response traceability, and this confirmation report | Unaffiliated specialist review or journal peer review |
| **External assurance** | None established for rerun, reimplementation, formal verification, specialist review, or editorial peer review | Any use of `independent`, `externally verified`, or `peer reviewed` for the present workflow |
| **Field evidence** | A prospective eligibility/simulation/shadow/pilot protocol with RACI and stop rules | A real logistics instance, savings, service improvement, feasibility, adoption, causal effect, or net value |

## Decision and acceptance conditions

**Decision recommendation: Major Revision / `HOLD_FOR_REPAIR` (confidence 5/5).** Reject is not warranted: the mathematical candidate remains specific, potentially important, and producer-side replay is internally coherent. Accept and Minor Revision are not warranted under the configured confirmation standard because four P1 groups remain and R2, R3, R4, R6, R8, DA-M2, DA-M4, DA-M5, and DA-M6 are not fully addressed across the immutable package.

Minimum acceptance conditions are:

1. reconcile every public/machine surface to v0.3.1, 19 tests, candidate wording, correct parent/preprint status, and an instance-specific operational portfolio route;
2. remove or correctly recompute/formulate the 42.6709% field everywhere;
3. replace unqualified independent/exact-global certificate and CLI language with the recorded solver-independent producer boundary;
4. repair PDF page 8, rerun preflight plus genuine page-by-page visual QA, and freeze new Markdown/PDF/manifest/archive hashes;
5. correct CFF release status, public replay paths, review-record paths, and the stale research-extension/site records;
6. rerun ordinary and optimized replay, semantic negative controls, manifest/archive extraction, portfolio boundary/tail checks, and cross-document phrase/version/count gates.

Because these corrections are primarily claim-surface, metadata, and rendering repairs, they should be resolved through deterministic regression and exact editorial readback. They must not be treated as accumulating external mathematical assurance, and a third model-mediated scientific review is not automatically justified without the required information-gain proposition.
