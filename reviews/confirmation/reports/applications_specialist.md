# Applications / Cross-Disciplinary Specialist — Confirmation Review

## Review identity and boundary

- **Frozen candidate:** `exact-three-item-jrp-applications-v0.3.1-candidate`
- **Role:** logistics semantics, implementation transfer, field design, stakeholder ownership, and application-claim calibration
- **Review type:** Evidence Press internal journal-like editorial confirmation; **not** external peer review, unaffiliated specialist review, independent rerun, independent reimplementation, or formal verification
- **Conflicts / limitations:** I reviewed only the configured frozen target and its included round-one record. I did not read another confirmation report or modify the candidate. Mathematical proof and verifier conclusions below are traceability findings; substantive adjudication of those areas belongs to the methodology and domain roles.

## Frozen-target verification

All four required hashes match `FROZEN_TARGET.md` exactly.

| Object | Expected SHA-256 | Observed SHA-256 | Result |
|---|---|---|---|
| `frozen-submission.zip` | `b51486d01b7aaddfad108c10f8ddbc8aa4fdfe27e3dc27d040b64e6a649ecdf3` | `b51486d01b7aaddfad108c10f8ddbc8aa4fdfe27e3dc27d040b64e6a649ecdf3` | PASS |
| `MANIFEST.sha256` | `fa5a3537a362cde4b154fbe69accc453bf813eacf19d73867b6085e60c507199` | `fa5a3537a362cde4b154fbe69accc453bf813eacf19d73867b6085e60c507199` | PASS |
| paper Markdown | `4f5c2d29df62eca54b9f38d95505785acf84f88ef5cb5f4cb876cfbc16cfa6ee` | `4f5c2d29df62eca54b9f38d95505785acf84f88ef5cb5f4cb876cfbc16cfa6ee` | PASS |
| paper PDF | `87f990da25b3cdaa4dfec4c44456ab0840b70a3a3f9dd256e937e8e887a73985` | `87f990da25b3cdaa4dfec4c44456ab0840b70a3a3f9dd256e937e8e887a73985` | PASS |

The manifest has the declared **123 entries**.

## Recommendation

**Major Revision — confidence 5/5.**

The revised paper and `LOGISTICS_DEPLOYMENT_PROTOCOL.md` substantially and thoughtfully repair the round-one applications defects. Event ownership, unit semantics, joint uncertainty, omitted constraints, simulation/shadow/field sequencing, comparator logic, interference, carryover, design adequacy, RACI, stopping authority, and the no-impact evidence ceiling are now explicit in those controlling texts. However, the frozen release package contains contradictory public-facing and machine-facing surfaces that reinstate the two most important transfer errors: the frozen synthetic five-policy set is again described as the logistics handoff, and the holding-cost inner-box contrast is again used to justify that transfer. The same surfaces also retain stale v0.3.0, 15-test, unqualified-title, and premature release-date facts.

Because publication is permitted only when every R1–R8 and DA-M1–DA-M7 item is fully addressed and no P0/P1 remains, the candidate does not meet the configured acceptance rule. The required repair is bounded: synchronize the site, index, CFF, README, and portfolio-purpose text to the already-correct paper/protocol boundary and add deterministic cross-surface regressions. It need not reopen the mathematical proof if no scientific claim or estimand is changed.

## New confirmation findings

### P1-A — Public-facing application artifacts reintroduce the frozen-portfolio transfer and broaden the holding-box interpretation

The controlling paper says the five policies are a **frozen synthetic regression fixture**, requires a newly generated instance-specific candidate set for every fitted operational instance, and says the holding boxes are H-only warnings rather than operational uncertainty evidence (`paper/three_item_jrp_gap_and_logistics.md`, §6.3, especially lines 395–397). The deployment protocol repeats this separation and requires event closure, joint uncertainty, and instance-specific generation (`LOGISTICS_DEPLOYMENT_PROTOCOL.md`, Gate 0, Gate 2, and Gate 3; lines 34–59).

The packaged Evidence Press handoff contradicts that repair:

- `site/papers/certified-three-item-jrp-gap/meta.draft.json`, lines 6–7, says the holding-box comparison quantifies a “robustness cost” and that the logistics handoff “supplies a five-policy portfolio for simulation.”
- The same file, line 34, says the holding-box certificates “support a five-policy logistics portfolio,” and line 68 includes the five-policy portfolio in the operational decision object.
- `site/papers/certified-three-item-jrp-gap/body.md`, line 45, says the four-order contrast is why “the right handoff is a five-policy portfolio.”
- `README.md`, lines 28 and 36, still calls it a five-policy logistics portfolio and says near-tied patterns should be evaluated as that portfolio.
- `analysis/policy_portfolio.json`, line 552, retains the top-level purpose “Exact five-policy handoff for secondary operational evaluation,” even though each nested portfolio correctly says it is a frozen synthetic regression fixture (line 541).

This is not harmless shortening. It restores the exact W2/DA-M5 semantic error that R6 was required to remove, and it encourages readers to infer an operational portfolio from H-only synthetic stability fixtures. It also weakens DA-M4's non-maximal, non-operational robustness boundary.

**Required remedy:** Make every public and machine-facing surface say that the included five policies are regression fixtures only. State that every fitted instance requires fresh exhaustive generation across boundary policies, primitive triples, tail closure, preregistered materiality/regret tolerance, and calendar feasibility. Describe the radii as conservative inner boxes under simultaneous relative H perturbation, not as intrinsic or operational robustness. Add a phrase-consistency regression covering the paper, README, site metadata/body, portfolio JSON, narration, and claims index.

### P1-B — Whole-package version, title, test-count, and release-status facts remain inconsistent

R4 and R8 require release-wide candidate wording and no conflicting version, count, date, or status facts. The frozen package still contains:

- `site/papers/certified-three-item-jrp-gap/meta.draft.json`, line 10: version `0.3.0-candidate`, while the frozen target is v0.3.1.
- The same file, line 47: “all fifteen tests,” while `REPLAY_RECEIPT.json` records 19 ordinary, optimized, and clean-extraction tests.
- `AI_INDEX.md`, line 5: the unrecalibrated title *An Exact Three-Item Independent-Cap Oracle and a Certified Multi-Item Relaxation-Gap Lower Bound*, rather than the v0.3.1 “Candidate Exact” title.
- `CITATION.cff`, line 6: `date-released: 2026-08-22`, despite `STATUS.md`, `RELEASE_DECISION.md`, and the site draft stating that no public successor release exists. This exact field was identified in round one and R8 required it to be removed or qualified until release.

These contradictions defeat the claimed release-wide phrase/fact audit and leave R4/R8 only partly addressed.

**Required remedy:** Regenerate all site and agent-facing metadata from the v0.3.1 source of truth; align the title and 19-test receipt; omit `date-released` until a public release exists (or use a CFF-compliant non-release field); and add a deterministic package consistency check for version, title, test/certificate counts, gate count, assurance status, and public-identity state.

### P2-A — The stakeholder/impact boundary remains narrower than the round-one applications request

The RACI is a meaningful improvement and does name operations, finance, procurement, warehouse, service/quality, technology, privacy/security, legal/safety, suppliers, worker representatives, methods leadership, the pilot sponsor, and affected stakeholders (`LOGISTICS_DEPLOYMENT_PROTOCOL.md`, lines 86–98). Outcomes also include workload, overtime, switching, and implementation costs (lines 73–84).

However, the protocol still does not explicitly allocate ownership or measurement for carrier burden, customer-level distributional effects, emissions/waste, sustainability, or contractual renegotiation—the transfer channels named in round-one R3-W5. “Affected stakeholders” is too generic to show who can veto or demand rollback when value is shifted outside the focal organisation.

**Suggested remedy:** Add explicit carrier/logistics-partner, customer, labour, sustainability/environmental, and regulatory rows or impact-boundary fields; record transfer metrics and veto/escalation authority. This is a minor applications completeness issue, not an independent publication blocker.

### P3-A — The paper retains the misleading heading “Robust policy set”

`paper/three_item_jrp_gap_and_logistics.md`, line 395, still labels §6.3 “Robust policy set,” although its text correctly says the included set is a synthetic regression fixture and the operational set is only a candidate set for robustness evaluation.

**Suggested remedy:** Rename the section “Regression fixtures and instance-specific candidate sets.”

## R1–R8 trace

| Item | Status | Confirmation evidence and assessment |
|---|---|---|
| **R1** | **Fully addressed (traceability; specialist correctness deferred)** | The paper now defines the rational instance, real common-origin fixed-interval policy class, density, objective, cap domain, and `Gamma` (§2.1); states pair-tail, finite-generation, triple-tail, strict-interior-improvement, totality, and monotonicity results (§§3.3–3.6, §4.3); and separates direct claims from parent/resource dependencies (§2.2). No application-level scope inflation was found in these controlling sections. |
| **R2** | **Fully addressed (traceability; verifier correctness deferred)** | `src/jrp3/verify.py` enforces required/allowed fields, exact three-frequency length, safe expression grammar, and canonical identifiers; `tests/test_oracle.py` contains the reviewed-shape, seeded-schema-fuzz, extraction-path, and portfolio completeness regressions; `ASSURANCE.md` accurately retains the same-producer/shared-substrate boundary. |
| **R3** | **Fully addressed within the frozen evidence record** | Paper §1.1 and References, `SOURCES.md`, and `CITATION_AUDIT.md` correct the named logistics records, separate peer-reviewed and preprint uses, add field-design sources, and state that targeted search is not proof of novelty. The application sources are used to motivate design requirements, not to validate this oracle. |
| **R4** | **Partly addressed** | The paper title/abstract/conclusion, §4.2, §4.4, and §4.5 correctly use candidate wording, inner H-only radii, discovery-guide status, and a carefully denominated 4.6588% comparator. But `AI_INDEX.md` retains the unqualified old title, while site metadata reuses intrinsic “robustness cost” rhetoric. See P1-A/P1-B. |
| **R5** | **Partly addressed** | The controlling paper §§6–8 and protocol Gates 0–6 now supply event closure, consistent units, joint uncertainty, omitted-constraint handling, comparator logic, design adequacy, assignment, interference, carryover, precision/power, noncompliance, missingness, multiplicity, cost boundary, RACI, and stopping authority. The site handoff does not carry these repairs and instead revives the synthetic-portfolio transfer. See P1-A. |
| **R6** | **Partly addressed** | `scripts/build_extensions.py` enumerates all 49,981 primitive triples per witness at `S=21`, applies the `1/1,000,000` relative tolerance, records minimum excluded regret, boundary comparators, threshold, and tail exclusion; `tests/test_oracle.py::test_registered_portfolios_are_enumeration_and_tail_complete` checks membership and tail closure. The paper/protocol correctly require per-instance regeneration. The site, README, and portfolio top-level purpose contradict that semantics. See P1-A. |
| **R7** | **Fully addressed** | `PROVENANCE.md`, paper disclosures, `ASSURANCE.md`, `CLAIMS.json`, licences, and the frozen round-one record preserve Anonymous scholarly authorship, identify the maintainer/correction-routing role, disclose AI/funding/conflicts, and keep internal editorial review distinct from external specialist/peer review and independent reproduction. Confirmation remains pending rather than pre-credited. |
| **R8** | **Partly addressed** | `REPLAY_RECEIPT.json` and core records consistently report v0.3.1, 19 tests, three point certificates, sixteen vertices, 123 manifest entries, seven gates, path-independent JSON, and a 15-page PDF. The site metadata remains v0.3.0/15 tests, `AI_INDEX.md` has the old title, and `CITATION.cff` claims a release date before release. See P1-B. |

## DA-M1–DA-M7 trace

| Item | Status | Confirmation evidence and assessment |
|---|---|---|
| **DA-M1** | **Fully addressed (traceability; proof correctness deferred)** | Paper §§2–3.6 make the finite search, tail, totality, domains, quantifiers, cap restoration, and dependency boundary explicit; candidate/external-audit limits remain visible in §5 and §9. |
| **DA-M2** | **Partly addressed** | The paper §5, `ASSURANCE.md`, and `CLAIMS.json` correctly label the verifier as same-producer and preserve every external-assurance dimension as not assessed. However, the old unqualified title in `AI_INDEX.md` and unqualified exact/certified site one-line metadata violate the required release-wide candidate wording. See P1-B. |
| **DA-M3** | **Fully addressed under the round-one editorial arbitration** | A positive-`Ki` witness or field case was not mandatory if claims were narrowed. Paper §4.4 fixes/varies/omits the H-box parameters; §§6–8 classify the witnesses as synthetic, require joint uncertainty before operational comparison, and keep field value untested. |
| **DA-M4** | **Partly addressed** | Paper §4.4 correctly says “certified inner radii,” H-only, conservative, non-maximal, and non-operational. The site metadata/body again use the four-order comparison as the reason for a five-policy logistics handoff and omit the inner/non-maximal boundary. See P1-A. |
| **DA-M5** | **Partly addressed** | The generated portfolio now records exhaustive primitive-triple membership, boundary comparators, the next exclusion margin, and tail exclusion, while paper/protocol require fitted-instance regeneration. The public handoff nevertheless calls the frozen five the logistics portfolio. See P1-A. |
| **DA-M6** | **Fully addressed** | The 42.6709% metric is removed from the abstract/conclusion and substantive package rhetoric. Paper §4.5 retains only a formula-defined 4.6588% descriptive comparison and explicitly denies certified interval-contraction status. |
| **DA-M7** | **Fully addressed** | Paper §§6–9, `LOGISTICS_DEPLOYMENT_PROTOCOL.md`, `CLAIMS.json`, `STATUS.md`, and site impact metadata consistently state that no field result, plan change, savings, service improvement, net value, or causal impact has been established. The future evidence ladder distinguishes mechanism, feasibility, association, and causal evidence. |

## Applications and field-design assessment

### Event ownership and closure

The revised protocol now gives the required three-way decision: complete economic/calendar ownership; a versioned frozen background calendar with marginal common-event cost; or software-only exclusion (`LOGISTICS_DEPLOYMENT_PROTOCOL.md`, Eligibility and Gate 0). It also requires analysts to list every SKU/activity sharing the event and rejects sunk `K0` or invalid cap proxies. This closes the main semantic gap in the controlling protocol. Any background-calendar implementation must still occur in the operational layer; the exact three-stream certificate itself is not evidence that the conditioned model was implemented correctly.

### Unit semantics and omitted constraints

The bridge distinguishes `K0`, `Ki`, deterministic cycle-stock `Hi`, long-run periodic `fi`, and average-frequency caps; it requires consistent time/currency units and names non-equivalent pointwise capacity, minimum-quantity, service, lead-time, transport, shelf-life, and calendar constraints. Paper §7 and protocol Gates 0–3 prevent those features from being silently encoded as independent caps. The H mapping remains an EOQ convention, not a generally identified operational coefficient.

### Regression-to-application transfer and uncertainty

The generated portfolio is strong producer-side regression evidence: both witnesses include exactly five policies inside the declared tolerance, record 49,976 excluded enumerated policies, the minimum excluded regret, four boundary comparators, and a strict tail above the portfolio threshold. This supports the narrow regression-fixture claim. It does not support carrying those five patterns to new data. The paper/protocol understand that distinction, but the site/README/portfolio-purpose text does not; P1-A must be repaired.

Gate 3 now requires an empirically or expert-elicited joint uncertainty set over all common, minor, and holding costs, caps, event attribution, and calendars, with rank, regret, feasibility, service, and worst-case reporting. It expressly refuses to use the H-only boxes as operational uncertainty.

### Simulation, shadow, and field sequence

The sequence is appropriate: semantic closure, data reconciliation, exact stress test, operational simulation/digital twin, shadow operation, bounded concurrent pilot, and monitored scale. The protocol no longer treats six months or two cycles as portable minima. It requires the horizon to cover warm-up, carryover, seasonality, rare service failures, and the precision needed for the decision.

### Comparator and design adequacy

Eligibility freezes the incumbent policy and comparison metrics; Gate 2 compares the relaxation, exact oracle, incumbent periodic plan, and a fresh instance-specific set; Gate 5 requires a preregistered concurrent comparison, cost/service estimands, precision or power, non-inferiority and safety stops, and a full cost boundary. A before/after association is explicitly denied causal status. This is adequate as a prospective design gate, not evidence that any particular future design is valid.

### Interference, carryover, noncompliance, and stopping

Gate 5 requires an assignment unit, interference graph/exposure map, warm-up/carryover rules, override/noncompliance handling, missingness/attrition, multiplicity, and named stopping authority. The RACI assigns stop/rollback responsibility to the operations owner and accountability to the pilot sponsor, while minimum stop rules cover service, stockouts/safety, omitted-constraint infeasibility, overrides, net-cost failure, and drift. This substantially meets the round-one design requirement.

### No-impact evidence ceiling

The controlling scientific and assurance records remain disciplined: `STATUS.md` says operational impact is not assessed; `CLAIMS.json` marks logistics use as proposed and denies validation, adoption, net value, and causal impact; `ASSURANCE.md` records no plan change, field outcome, avoided loss, or implementation cost; the protocol classifies operational value as untested. The stale site portfolio rhetoric does **not** make a savings claim, but it does prematurely prescribe which synthetic policies should cross into application and must be corrected before release.

## Acceptance condition

The present Major Revision recommendation can be cleared without a new scientific claim if the candidate is revised additively and deterministic checks demonstrate all of the following:

1. every site, README, portfolio, index, and narration surface agrees that the bundled five are synthetic regression fixtures only;
2. every application surface requires event closure, an instance-specific regenerated set, joint uncertainty, omitted-constraint simulation, and design-adequate comparison before operational use;
3. every robustness surface states H-only, certified inner, non-maximal, and non-operational;
4. v0.3.1, 19 tests, the Candidate Exact title, and pre-release/public-identity state agree across the full package;
5. `date-released` is absent until an actual public release exists; and
6. the P2 stakeholder-transfer gap is either repaired or explicitly recorded as a non-fatal residual note.

Until those conditions are met, R4, R5, R6, R8, DA-M2, DA-M4, and DA-M5 are not fully closed and publication must remain `HOLD_FOR_REPAIR`.
