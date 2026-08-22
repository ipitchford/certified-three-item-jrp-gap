# Peer Review Report

## Manuscript Information

- **Title**: *An Exact Three-Item Independent-Cap Oracle and a Certified Multi-Item Relaxation-Gap Lower Bound*
- **Manuscript ID**: EP-JRP3-v0.3.0-frozen
- **Review Date**: 22 August 2026
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role

Peer Reviewer 2 (Domain)

### Reviewer Identity

Senior operations-research referee specializing in deterministic inventory theory, continuous-time joint replenishment, approximation bounds, and computer-assisted exact optimization.

### Review Focus

This report assesses the manuscript's place in joint-replenishment and relaxation-gap theory: literature coverage, novelty and priority calibration, relationship to the two-item predecessor and general upper bounds, theorem scope, and field-standard terminology. It does not independently validate the software implementation or reproduce the exact arithmetic.

---

## Overall Assessment

### Recommendation

- [ ] **Accept**
- [ ] **Minor Revision**
- [x] **Major Revision**
- [ ] **Reject**

### Confidence Score

**4/5 — high confidence.** The model and theoretical lineage are within my domain; confidence is lower regarding the unreviewed computer-assisted proof objects because this report is not an independent reconstruction.

### Summary Assessment

The manuscript constructs a finite exact oracle for a three-item, continuous-time, common-origin fixed-interval JRP with independent rational frequency caps and gives a producer-certified rational relaxation-gap witness of (1.1487291464748205\ldots). It also derives fixed-item monotonicity, a five-policy active envelope, and local holding-cost robustness boxes. The potential domain contribution is meaningful: if the finite-closure theorem and certificates withstand independent audit, the witness separates the three-item gap from the reported two-item candidate constant and supplies a nontrivial lower barrier against the standard max-frequency relaxation. The paper is unusually disciplined about operational non-transfer and about distinguishing a stationary-family guide from a certified rational point. However, it is not yet journal-ready. The theoretical literature is too thin to support priority calibration; several foundational resource-constrained and approximation papers are absent; two cited records are bibliographically misdescribed; and the two-item comparator is itself an unrefereed producer result. In addition, the policy class, counting-density operator, coefficient domain, and Γ-domain require formal definition, while the core finite-closure result is presented mainly as a compressed sketch referring to a repository note. These are correctable in one substantial revision, but they affect how the principal contribution is understood and therefore require re-review.

---

## Strengths

### S1: A sharply bounded three-item theoretical contribution

The manuscript reports exact rational values for both the relaxation and the fixed-interval optimum, identifies the ((3,3,2)) schedule, and explicitly stops short of claiming the exact three-item constant (manuscript lines 10–31, 157–190, and 271–279). This is a useful contribution form in a field where arithmetic synchronization makes even small instances structurally difficult.

### S2: Structural explanation rather than an isolated numerical witness

Section 4.2 identifies four equalized neighbouring policies, the crossover polynomial with ((3,3,2)), and a stationary guide while correctly stating that the family calculation is not a proof of the global three-item constant (lines 192–220). That distinction substantially strengthens the theoretical narrative.

### S3: Correct separation of lower-bound, upper-bound, and open-constant statements

The manuscript distinguishes the certified candidate lower bound, Segev's general upper guarantee, and the still-open exact three-item and unrestricted constants (lines 222–241 and 271–279). The relaxation-barrier statement is also appropriately limited to analyses measured against the stated relaxation (lines 241–242).

### S4: Strong assurance and application boundaries

The same-producer nature of the checker is disclosed (lines 281–292), and the logistics sections repeatedly distinguish a diagnostic benchmark from field benefit (lines 294–328). The limitations section expressly states that the search does not establish priority and that specialist review and independent rerun are absent (lines 330–338). This is exemplary claim hygiene.

### S5: The robustness result has an operationally honest interpretation

The eight-vertex argument is used to prove a coefficient box rather than presented as sampling, and the paper treats the tiny headline radius as a warning rather than as evidence of practical robustness (lines 243–259 and 306–308). Retaining the stronger and margin witnesses is theoretically and operationally sensible.

---

## Weaknesses

### W1: The theoretical literature and priority audit are inadequate

**Problem**: The introduction moves directly from the Evidence Press predecessor to the new witness (lines 33–45), while the ten-item reference list contains no dedicated related-work synthesis. It omits foundational sources for the exact convex relaxation and resource-feasible power-of-two rounding, including Roundy (1989) and Teo and Bertsimas (2001), and it omits relevant published complexity and recent continuous-time approximation results. More seriously, references 8 and 9 are misdescribed: DOI `10.1016/j.ejor.2022.02.005` is Creemers and Boute, *The joint replenishment problem: Optimal policy and exact evaluation method*, EJOR 302(3):1175–1188, not the title given at line 355; DOI `10.1007/s44176-022-00010-3` is by Lu Peng, Lin Wang, and Sirui Wang, titled *A review of the joint replenishment problem from 2006 to 2022*, in *Management System Engineering* 1:9, not the record described at line 356 and `SOURCES.md` line 20.

**Why it matters**: Without a correct lineage, readers cannot judge whether the second-smallest-pair-complexity tail, exact three-item totality result, or lower-bound family is new. A failed targeted search is appropriately disclaimed, but it cannot substitute for comparison with the field's central formulations and results.

**Suggestion**: Add a substantive related-work section and a comparison table covering model class, policy class, constraint class, exact/approximate status, and contribution. Correct the two records and audit every DOI/title/author/year pair. At minimum discuss Roundy (1989), Teo and Bertsimas (2001), Cohen-Hillel and Yedidsion (2018), Segev's published 2025/2026 continuous-time results, Segev's 2026 resource-constrained arXiv paper, and the two-item Evidence Press candidate. State that priority remains unresolved until a broader specialist search or external review is completed.

**Severity**: **Major**

### W2: Imported candidate results are not calibrated tightly enough at the points of use

**Problem**: The abstract and introduction call the two-item endpoint “certified” and use it to state a 3.3132% improvement (lines 31 and 35–41), while Section 2 imports a “parent cap-reduction theorem” (line 65). The reference list does label the predecessor as a candidate (line 348), but the local prose does not consistently say that its universal two-item upper theorem remains producer-side and unrefereed. Likewise, (5/(6\ln2)) is called the “current general guarantee” (lines 237–241 and 279) without emphasizing that the cited resource-constrained result is arXiv v1 rather than a peer-reviewed publication.

**Why it matters**: The numerical three-item witness can stand as a candidate result on its own, but “breaking the two-item ceiling,” the resource-to-box interpretation, and the interval-contraction metric inherit the epistemic status of external results. Readers need to know which consequences are proved here, imported from a candidate predecessor, or imported from a current preprint.

**Suggestion**: Add a claim-dependency table. Use “producer-certified candidate two-item endpoint” at first use; state exactly which theorem is imported and whether the three-item box lower bound depends on it (it appears not to, whereas the broader resource-reduction interpretation does). Describe Segev's value as the upper bound reported in arXiv:2603.18720v1, checked as of the manuscript date, and avoid implying peer-reviewed consensus.

**Severity**: **Major**

### W3: The model and gap constant are not defined with journal-level precision

**Problem**: The paper writes “\(\operatorname{dens}\)” without defining the asymptotic counting limit (lines 49–56), calls (C^*) an “exact periodic optimum” even though a union of incommensurable fixed-interval streams is not itself periodic (lines 16–22 and 69–77), and introduces Γ only informally (lines 24–29 and 224‒28). It is unclear from the theorem statements whether Γ ranges over rational caps only, rational or real cost coefficients, zero minor setup costs, all common-origin fixed-interval policies, or a wider stationary policy class. Calendar phases are excluded by (T_i\mathbb Z_{\ge0}) but are not named until the limitations (line 338).

**Why it matters**: These choices determine whether the result is a relaxation gap, an integrality gap, or a gap within a restricted policy class. They also govern whether the monotonicity lemma and comparison with Segev's model are exactly like-for-like.

**Suggestion**: Formally define the counting density, admissible instance class, policy class, common origin/zero phase, coefficient domain, and Γ supremum. Prefer “common-origin fixed-interval optimum” or define “periodic policy vector” explicitly. Use “relaxation gap” consistently unless an integer formulation is supplied. State why Segev's upper theorem applies to precisely this subclass.

**Severity**: **Major**

### W4: The core finite-closure theorem is too compressed in the manuscript

**Problem**: Section 3 gives the key triple-tail inequality in one paragraph and sends the full derivation to `docs/three_item_oracle_note.md` (lines 119–133). The paper does not present a numbered totality theorem with complete hypotheses, nor a formal finite-enumeration lemma, boundary-closure proposition, or proof that a fully commensurable incumbent eventually lies strictly below the boundary value. The holding-box and active-family results are similarly described without formal proposition statements (lines 192–259).

**Why it matters**: The finite-closure theorem, rather than the witness digits, is the likely durable theoretical contribution. A journal reader must be able to audit its logical scope from the manuscript or a stable formal appendix, not by following repository-internal paths.

**Suggestion**: Promote the finite-enumeration lemma, triple-tail theorem, oracle-totality theorem, fixed-(n) monotonicity lemma, and holding-box vertex principle to numbered results with explicit assumptions and proofs. Move the complete mathematical arguments into the paper or a citable immutable supplement; retain code as verification evidence rather than the location of essential theorem text.

**Severity**: **Major**

### W5: The interval-contraction metric is nonstandard and overly prominent

**Problem**: The abstract and Section 4.5 emphasize a 42.6709% reduction of a “multiplicative interval” (lines 31 and 279). This is a bespoke comparison whose denominator begins at an unrefereed two-item candidate endpoint and ends at a current arXiv upper bound.

**Why it matters**: The percentage may be arithmetically correct, but prominence in the abstract can read as a field-level advance metric stronger than the underlying assurance warrants.

**Suggestion**: Define the formula explicitly, call it an interval-contraction diagnostic, and move it out of the abstract. Lead instead with the exact lower bound, its fixed-(n) consequence, and the open gap to the reported general upper bound.

**Severity**: **Minor**

---

## Detailed Comments

### Title & Abstract

- The title is accurate if “oracle” means an exact terminating method over the explicitly defined common-origin fixed-interval class. Add that class to the abstract.
- The abstract is information-dense but tries to carry theorem, active-set, robustness, interval-contraction, and deployment claims simultaneously (lines 8–31). Remove the bespoke 42.6709% metric and reduce the logistics protocol to one sentence.
- Replace “exact periodic optimum” with a term that does not imply the union schedule is periodic in the incommensurable regimes.

### Introduction

- The “third item matters” motivation is clear and the arithmetic mechanism is well explained (lines 33–45).
- The comparison is presently internal to an Evidence Press research sequence. Add the field-level question: how does an exact fixed-(n) oracle complement published approximation schemes, complexity results, and resource-constrained rounding?
- “The third stream creates a qualitatively new coordination geometry” (line 43) is plausible within the stated partition structure, but should not double as a novelty claim without the related-work audit.

### Literature Review / Theoretical Framework

- There is no actual literature-review section. The references are divided between a sparse mathematical lineage and applied examples, with insufficient synthesis of the convex-relaxation tradition.
- The appropriate framework is the Roundy/Teo–Bertsimas convex-relaxation and rounding lineage, followed by modern continuous-time alignment and resource-constrained approximation results. The manuscript should explain exactly where its fixed-(n) exact analysis enters this framework.
- The Evidence Press two-item result is a direct predecessor, not a substitute for peer-reviewed field literature. Its candidate status should be adjacent to each dependent claim.

### Model and Theorem Scope

- Define “\(\operatorname{dens}\)” as an asymptotic counting density and state existence for the policy sets considered (lines 49–56).
- State whether caps and all cost coefficients must be rational for oracle input, and whether Γ is a supremum over rational-data instances or the corresponding real closure.
- Clarify the role of (K_i=0). The headline witness uses zero minor setup costs (lines 139–155); this is admissible in the stated model but should be highlighted because some JRP conventions assume strictly positive minor costs.
- The monotonicity proof (lines 224–230) is convincing as a supremum/epsilon argument once the instance class is fixed. State the choice of (f_0), the unchanged max-frequency term, and the limiting ratio explicitly.

### Exact Finite Closure

- The partition of three commensurability classes is correct and well motivated (lines 69–77).
- The fixed-triple reduction (A/t+Bt) and cap-bound optimum are standard and clearly presented (lines 79–113).
- The second-smallest pair-complexity cutoff appears to be the manuscript's main structural novelty. Give its finite-generation lemma and component bound in the paper, not only in the oracle note.
- Distinguish an exact totality theorem from an efficiency theorem. The supplementary note does so; the main manuscript should make the same point in a formal theorem statement.

### Results and Consequences

- The rational witness, boundary threshold, and exact winner are reported transparently (lines 137–190).
- The active-envelope family is useful explanatory evidence, and the warning that its stationary point is not globally optimal is correctly placed (lines 192–220).
- State the theorem dependency for Γ's upper inequality. Segev's arXiv paper explicitly bounds cost relative to the same max-frequency convex relaxation for resource-constrained instances, but the manuscript should show the independent-cap embedding and cite the exact theorem/formulation.
- The holding-box vertex logic is valid for a fixed cap-bound winner because every fixed competitor's cost difference is affine in (H); state this quantification over all fixed schedules in the proposition.

### Discussion, Applications, and Limitations

- The logistics role is appropriately conservative and should be retained as a bounded implications section (lines 294–328).
- The limitations are unusually strong and accurately identify synthetic-instance, policy-class, verification, novelty, and operational boundaries (lines 330–338).
- The conclusion's opening phrase “changes the mathematical frontier” (line 342) should be softened until the literature/priority audit and specialist proof review are complete. “Changes the producer-certified lower-bound frontier within this research sequence” would be accurate now.

### References

- Correct references 8 and 9 as detailed in W1.
- Add publication years consistently. Schulz and Telha appeared in *Operations Research* 72(3) in 2024 (online 2022); Segev's pairwise-alignment article is in *Management Science* 71(5), 2025 (online 2024).
- Distinguish peer-reviewed articles, arXiv preprints, SSRN working papers, and Evidence Press candidate packages in the bibliography.

### Missing Key References

- Robin Roundy (1989), “Rounding Off to Powers of Two in Continuous Relaxations of Capacitated Lot Sizing Problems,” *Management Science* 35(12):1433–1442, [doi:10.1287/mnsc.35.12.1433](https://doi.org/10.1287/mnsc.35.12.1433). This is foundational for the resource-feasible rounding and convex-relaxation lineage.
- Chung-Piaw Teo and Dimitris Bertsimas (2001), “Multistage Lot Sizing Problems via Randomized Rounding,” *Operations Research* 49(4):599–608, [doi:10.1287/opre.49.4.599.11222](https://doi.org/10.1287/opre.49.4.599.11222). This supplies the randomized-rounding development used in current resource-constrained comparisons.
- Tamar Cohen-Hillel and Liron Yedidsion (2018), “The Periodic Joint Replenishment Problem Is Strongly NP-Hard,” *Mathematics of Operations Research* 43(4):1269–1289, [doi:10.1287/moor.2017.0904](https://doi.org/10.1287/moor.2017.0904). This is needed to calibrate the exact-oracle contribution against known complexity.
- Danny Segev (2025; print issue 2026), “Improved Approximation Guarantees for Joint Replenishment in Continuous Time,” *Mathematics of Operations Research* 51(2):1683–1712, [doi:10.1287/moor.2024.0635](https://doi.org/10.1287/moor.2024.0635). This published paper belongs in the modern theoretical lineage alongside the pairwise-alignment paper.
- Stefan Creemers and Tim Stephan (2026), “Special Cases of the Joint Replenishment Problem (JRP): A Mathematical Analysis,” SSRN 6674418, [doi:10.2139/ssrn.6674418](https://doi.org/10.2139/ssrn.6674418). This is an adjacent current preprint about exact special-case structure; inspect and distinguish its stochastic/can-order policy class rather than treating its presence or absence as proof about novelty.

---

## Questions for Authors

1. What is the exact domain of Γ\(_{n,\square}\): rational or real coefficients, rational or real caps, zero or strictly positive minor setup costs, and common-origin fixed-interval policies or a wider stationary class?
2. Which claims in this manuscript are logically independent of the unrefereed two-item predecessor, and which depend on its cap-reduction theorem or universal two-item upper endpoint?
3. Can the authors supply a model-by-model comparison showing that Segev's (5/(6\ln2)) theorem bounds the same relaxation ratio for this independent-cap subclass, including the relevant theorem and preprint version?
4. What literature-search protocol was used for the second-smallest-pair-complexity tail and three-item exact oracle, and will the authors commission a broader specialist priority review before asserting a new field frontier?

---

## Minor Issues

### Terminology

- Use “relaxation gap” consistently. Reserve “integrality gap” for a clearly specified integer/LP or integer/conic formulation.
- Define “cap-bound” on first use in Section 4.2 or 4.4.
- Clarify whether “primitive multipliers” are labelled by item and whether item permutations are counted separately in the 49,981 total.

### Citation Format

- The reference list mixes initials, article metadata, preprints, and candidate releases without consistent years or venue details (lines 346–357).
- Correct the Creemers–Boute and Peng–Wang–Wang records before release.
- Give the accessed version/date for arXiv:2603.18720 because “current” is time-sensitive.

### Presentation

- Consider a compact table comparing the audit, margin, and headline witnesses: ratio, exact winner, margin, robustness radius, and recommended use.
- Define the 3.3132%, 4.6588%, and 42.6709% denominators once in a notation box rather than repeating prose descriptions.

---

## Dimension Scores

These uncalibrated scores are ordinal assessments for editorial synthesis, not venue-acceptance probabilities.

| Dimension | Score (0–100) | Descriptor | Notes |
|---|---:|---|---|
| Originality (20%) | 66 | Adequate | Potentially strong fixed-(n) exact contribution, but priority has not been established and field positioning is incomplete. |
| Methodological Rigor (25%) | 58 | Weak | Exact design is promising, but core totality arguments are compressed or external to the manuscript and remain same-producer. |
| Evidence Sufficiency (25%) | 55 | Weak | Exact certificates support the bundled instance internally; independent reconstruction and adequate scholarly triangulation are absent. |
| Argument Coherence (15%) | 74 | Adequate | The mathematical narrative is coherent, but imported candidate claims and policy-class definitions interrupt the warrant chain. |
| Writing Quality (15%) | 82 | Strong | Clear, disciplined prose with excellent assurance boundaries; some promotional and over-dense passages remain. |
| Literature Integration (R2 focus) | 52 | Weak | Sparse theoretical lineage, no synthesis section, foundational omissions, and two incorrect source descriptions. |
| **Weighted Average** | **64.85** | **Major Revision** | The contribution merits revision, but literature, scope, and theorem-presentation defects are release-level gates. |

---

## Domain Recommendation Rationale

I recommend **Major Revision**, not rejection. The candidate appears to contain a potentially valuable exact small-(n) result, and its assurance boundaries are substantially better than typical computer-assisted submissions. The required changes are nevertheless foundational for scholarly interpretation: the paper must repair and deepen its literature base, define its model and gap constant precisely, classify every imported result by evidence status, and place the complete core theorem in the citable manuscript or immutable supplement. A revised version should undergo specialist re-review before Evidence Press approval.
