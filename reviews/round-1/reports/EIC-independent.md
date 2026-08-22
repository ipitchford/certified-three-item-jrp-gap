# Peer Review Report

## Manuscript Information

- **Title**: *An Exact Three-Item Independent-Cap Oracle and a Certified Multi-Item Relaxation-Gap Lower Bound*
- **Manuscript ID**: `exact-three-item-jrp-applications-v0.3.0-candidate`
- **Review Date**: 22 August 2026
- **Review Round**: First-round independent editorial review
- **Submission reviewed**: Frozen v0.3.0 candidate manuscript and its frozen release/assurance materials

---

## Reviewer Information

### Reviewer Role

Editor-in-Chief (independent first-round editorial assessment)

### Reviewer Identity

Editor-in-Chief for an Evidence Press-style research release, with an editorial remit spanning operations research, exact computational certificates, reproducible research packages, and calibrated translation from model evidence to practice. This assessment is from the journal-fit and release-suitability perspective; specialist reviewers should adjudicate the number-theoretic closure, optimisation proof, and software-verification details. No other reviewer report was consulted.

### Review Focus

I assess journal fit, originality and significance, the coherence of the overall argument, value to mathematical and logistics readers, claim calibration, and readiness for Evidence Press release. I also distinguish local candidate circulation from public release approval and assess whether the existing **PASS WITH NOTES** is supportable within that limited boundary.

---

## Overall Assessment

### Recommendation

- [ ] **Accept** — Can be published directly, only minor formatting changes needed
- [ ] **Minor Revision** — Minor revisions needed, no re-review after revision
- [x] **Major Revision** — Substantial revisions needed, re-review required after revision
- [ ] **Reject** — Not suitable for publication in this journal

### Confidence Score

**4/5 — High confidence.** The publication strategy, assurance boundary, and high-level operations-research contribution fall substantially within my remit. I defer to the mathematical and computational specialists on the correctness of the finite-closure, totality, active-envelope, and verifier arguments.

### Summary Assessment

The submission presents a rational three-item independent-cap joint-replenishment instance, an executable finite oracle, and a producer-side certificate for an exact-to-relaxed ratio of (1.1487291464748205845\ldots). It further proposes fixed-(n) monotonicity, a five-policy active-envelope explanation, exact holding-cost boxes, and a deliberately gated logistics evaluation protocol (manuscript lines 10–31 and 222–328). The package is unusually disciplined about separating exact model calculations from independent verification, formal proof, novelty, and field impact (lines 281–292 and 330–363; `ASSURANCE.md`, lines 23–37).

The work is a strong fit for Evidence Press as a transparent research candidate and offers genuine reader value: a mathematically interesting three-item obstruction, reproducible exact fixtures, and a clear example of why a stronger extremal witness can be operationally more fragile. Its principal weakness is that the headline “exact” certification still depends on a general finite-closure and tail argument that the package itself classifies as a candidate proof. The paper is also not yet independently self-contained on the inherited cap-reduction dependency or sufficiently supported for a priority/novelty claim. I therefore support the existing **PASS WITH NOTES for local candidate circulation**, but not an approval for public Evidence Press release. Major revision, specialist adjudication, and a documented re-review are required before release approval.

---

## Strengths

### S1: A clear and potentially important mathematical delta

The manuscript states a fully rational witness, exact relaxed and periodic optimum values, and the resulting ratio in the abstract (lines 10–29), then explains that this exceeds the certified two-item upper endpoint (lines 33–45). If the closure proof withstands specialist scrutiny, this is a substantive rather than cosmetic extension: the two-item constant cannot describe the unrestricted multi-item setting. The result is narrow enough to be testable and important enough to interest exact-optimisation and approximation readers.

### S2: Strong separation of theorem, computation, and discovery guide

The five-policy calculation is presented as an exact family, while its stationary point is explicitly limited to a “discovery guide” rather than promoted to the global three-item constant (lines 192–220). The manuscript likewise distinguishes the exact rational witness from the open upper-certification problem (lines 271–279). This is exemplary claim architecture for computational mathematics.

### S3: Operational implications are conservative and useful

The paper does not convert a synthetic ratio into a savings claim (lines 43–45). Instead, Sections 6–8 frame the oracle as a triplet diagnostic, regression fixture, and policy-set generator, with simulation, shadow operation, field comparison, and stop rules placed downstream (lines 294–328). The distinction between the extremely fragile headline witness and the more stable margin fixture (lines 243–277) is especially valuable to practitioners and benchmark designers.

### S4: Assurance boundaries are unusually candid

The paper openly states that the checker is same-producer and shares utilities, so replay is not independent reimplementation (lines 281–292). The limitations section lists the missing specialist review, unaffiliated rerun, formalisation, priority audit, and field validation (lines 330–338), and the disclosure reiterates the AI and producer-side boundaries (lines 361–363). The frozen `ASSURANCE.md` and `CLAIMS.json` carry these limits into machine-readable release materials rather than leaving them only in prose.

### S5: The release package is structured for scrutiny

The frozen materials expose exact witnesses, three point certificates, sixteen robustness vertices, holding-box verifications, a claims registry, source audit, deployment protocol, replay receipt, and manifest. `REPLAY_RECEIPT.json` records ordinary, optimised, and clean-extraction producer replay (lines 10–34), while `RELEASE_DECISION.md` preserves a public-release HOLD (lines 3–16). That is a credible basis for local circulation and specialist review.

---

## Weaknesses

### W1: The headline exactness rests on a candidate proof linchpin

**Problem**: The title and abstract say “exact oracle,” “closes the infinite complement,” and “certified” (manuscript lines 2 and 10–31), but the paper later acknowledges that the generator and tail theorem remain prose candidate mathematics rather than formal or independently reviewed results (lines 292 and 335–337). The crucial totality step is only sketched in the companion note through asymptotic approximation arguments (`docs/three_item_oracle_note.md`, lines 355–369). If this linchpin fails, the finite certificate does not establish a global optimum over the infinite policy universe.

**Why it matters**: The main contribution, fixed-(n) consequence, robustness boxes, and relaxation barrier all inherit this dependency. A release reader could reasonably read “exact” as a settled theorem rather than a producer-certified candidate conditional on the closure argument.

**Suggestion**: State a formal theorem with every hypothesis and dependency; include a complete proof of the finite-enumeration, tail, and totality claims in the paper or a versioned appendix; make the dependency on the parent cap-reduction theorem explicit; and add a claim-dependency diagram. Until specialist review is complete, qualify the title/abstract with “candidate” or state prominently that global exactness is conditional on the candidate finite-closure theorem. Require re-review after the mathematical specialist’s report is answered.

**Severity**: **Major**

### W2: Novelty and priority positioning are too thin for the strength of the framing

**Problem**: The manuscript says only that a targeted search does not establish novelty or priority (lines 330–337), and `SOURCES.md` lists ten sources while noting that no located work used the same tail or rational witness (lines 5–25). That is honest, but it does not yet locate the contribution comprehensively within exact continuous-time JRP, resource-constrained JRP, integrality-gap constructions, commensurability methods, or arithmetic scheduling.

**Why it matters**: Phrases such as “the third item changes the mathematical frontier” (line 342) and the release’s significance depend on the contribution being genuinely distinct from existing formulations or equivalent constructions. Absence from a targeted search is not enough for a world-leading originality claim.

**Suggestion**: Add a reproducible priority-search appendix covering databases, search strings, dates, backward/forward citation chasing, and equivalent terminology. Include a comparison table against the parent two-item result, Segev’s rounding guarantee, and the nearest exact or arithmetic JRP results, separating what is imported, what is new, and what remains unproved. Calibrate any priority language to the completed search.

**Severity**: **Major**

### W3: The article’s genre and audience contract need sharpening

**Problem**: The title presents a mathematical oracle paper, whereas roughly the final third develops a logistics use case and prospective field-evidence programme (lines 294–328). These sections are thoughtful, but there is no operational dataset, simulation, or field result, and the title does not signal the applied protocol component.

**Why it matters**: Mathematical readers may regard the application material as diluting the proof presentation, while logistics readers may expect applied evidence that the paper explicitly does not supply. This weakens discoverability and makes journal fit less immediate despite the material’s intrinsic value.

**Suggestion**: Either (a) retain one integrated Evidence Press release but add a subtitle and an early evidence-state map that distinguishes theorem candidate, producer replay, proposed benchmark use, and untested field value; or (b) publish the mathematical article with the deployment protocol as a clearly linked companion artifact. In either case, state the intended primary readership and contribution hierarchy in the introduction.

**Severity**: **Minor**

### W4: Publication accountability is incomplete

**Problem**: The scholarly creator is Anonymous, while Ian Pitchford is described as research director, intended maintainer, and publisher but not scholarly author (`PROVENANCE.md`, lines 3–19; manuscript lines 361–363). The package does not provide a corresponding research guarantor, conflict-of-interest declaration, funding statement, or a detailed contribution taxonomy for the human and AI work.

**Why it matters**: A journal-like approval process needs a named party accountable for corrections, source custody, responses to reviewers, and conflict management even if scholarly authorship remains anonymous. This is particularly important when the publisher, research director, and AI-assisted producer workflow are closely connected.

**Suggestion**: Before release, add a responsible guarantor/corresponding contact, CRediT-style contribution statement, funding and competing-interest declarations, AI-use statement tied to concrete tasks, and an explicit statement that agent-role review is editorial-agent review rather than unaffiliated human peer review. Record reviewer conflicts and recusals in a separate review ledger.

**Severity**: **Major for release governance; minor for mathematical content**

### W5: Frozen release records contain avoidable internal inconsistencies

**Problem**: The main replay receipt reports fifteen tests and three point certificates (`REPLAY_RECEIPT.json`, lines 10–34), but `INTAKE_AUDIT.md` still says the successor “now passes 12 tests” (line 18), and `README.md` says the replay script “rebuilds both certificates” (line 49) despite the package describing three point certificates, sixteen vertices, and two holding-box reports elsewhere. The manuscript calls the field programme “six escalating gates” (line 324), while `LOGISTICS_DEPLOYMENT_PROTOCOL.md` numbers Gate 0 through Gate 6, including scale and monitoring (lines 31–68), which is seven named gates.

**Why it matters**: These are not mathematical defects, but release-grade evidence packages depend on exact cross-document consistency. Small stale counts reduce confidence in higher-stakes metadata.

**Suggestion**: Run a release-wide consistency check for test counts, certificate counts, gate counts, version labels, and status wording. Make a single machine-readable release summary the source for generated prose counts where practical.

**Severity**: **Minor**

---

## Detailed Comments

### Journal Fit

The submission fits Evidence Press well as a certificate-first, transparently bounded research release. It combines an exact-computation candidate with source provenance, replay artifacts, a claim ledger, and a deliberately non-promotional application route. Its fit with a conventional operations-research journal would be less clear unless the mathematical proof were fully self-contained and the logistics protocol were shortened or separated. For Evidence Press, the hybrid format is defensible if the release page makes the evidence-state hierarchy unmistakable.

The existing local **PASS WITH NOTES** is supportable for frozen candidate circulation because the package passes producer replay and openly lists its missing assurance dimensions (`STATUS.md`, lines 3–30; `ASSURANCE.md`, lines 20–37). It is not supportable as final release approval. The existing public-release **HOLD** is the correct state until the journal-like review is completed, author responses are verified, immutable identity/integrity gates pass, and the remaining review status is accurately described.

### Originality

The apparent originality lies in the second-smallest-pair-complexity finite closure, the rational three-item witness beyond the two-item ceiling, the exact five-policy active family, and the comparison between extremality and coefficient robustness. Those contributions are sufficiently specific to warrant review rather than desk rejection. However, the current source search establishes only a plausible novelty case, not priority. Release prose should avoid world-first or definitive-frontier language until the specialist literature review is complete.

### Significance

If correct, the three-item lower bound and monotonic propagation materially alter what can be claimed for the max-frequency relaxation at every fixed (n\ge3) (lines 222–241). The result is significant within a focused exact/approximation JRP community, and the exact fixtures have durable software-testing value. The broader logistics significance remains prospective, but the paper handles this appropriately by classifying operational value as untested (line 328). I would describe the impact as strong within a subfield, with credible cross-disciplinary benchmark potential rather than established practice-changing impact.

### Structural Coherence

The argument generally proceeds well from model and regime partition to finite closure, witness, implications, assurance, and applications. The principal structural gap is that the headline theorem’s proof burden is split between a concise paper section and a companion note, while the application discussion receives substantial space. A theorem/dependency table near the end of Section 2 and a compact result table in Section 4 would help readers distinguish: exact finite identity, candidate global closure, derived monotonicity, local holding-box implication, and proposed operational use.

### Title & Abstract

The title is technically precise about the independent-cap oracle and lower bound, but “Exact” and “Certified” are stronger than the current specialist-review state. The YAML status line (line 5) helps only if it is visibly rendered in all public formats. The abstract is information-rich and admirably includes limitations, but it tries to carry the theorem, active-family explanation, interval comparison, robustness result, application protocol, and assurance disclaimer in one paragraph. Shorten it and move the logistics handoff into a second labelled paragraph or evidence-state sentence. Clarify that there are sixteen vertex certificates across two eight-vertex boxes.

### Introduction

The introduction explains the third-item mechanism clearly (lines 33–45), especially the distinction between relaxation optimism and realised savings. It should also state the precise research question and contribution list, identify which theorem is inherited from the parent release, and provide a more conventional paragraph positioning the work against the nearest literature.

### Literature Review / Theoretical Framework

The references are relevant but sparse for a release making a potentially frontier-changing claim. The source-use notes are an excellent audit practice, yet they are not a substitute for a systematic novelty assessment. Bring the core mathematical comparison into the manuscript rather than leaving it largely in `SOURCES.md`, and distinguish the exact integrality-gap object from Segev’s algorithm-class guarantee at first mention, not only later.

### Methodology / Research Design

The three commensurability regimes and fixed-pattern cost reduction are communicated accessibly (lines 67–133). The paper needs a more explicit theorem/proof presentation for the finite generator, triple tail, and totality step, including cap-boundary cases and the role of the inherited cap-reduction theorem. The software architecture and mutation checks are useful corroboration but should remain secondary to the mathematical proof. I ask the mathematical specialist to scrutinise the approximation argument used to show finite termination and the exact scope of “all periodic schedules.”

### Results / Findings

The exact fractions, primitive multipliers, cutoff, and enumerated count are reported clearly (lines 135–190). The active-envelope result is well calibrated as a family-specific guide (lines 192–220), and the robustness comparison is one of the paper’s strongest findings (lines 243–277). Add a single table comparing the audit, margin, and headline witnesses by ratio, winner, cutoff, margin, robustness radius, and intended role. This would be more useful than repeating long decimals across multiple sections.

### Discussion

Sections 6–8 are unusually responsible about external validity. They specify omitted operational features (lines 310–320), downstream evaluation gates, outcomes, and stop conditions (lines 322–328). The discussion should nevertheless make explicit that no claim is made about how often the three-item obstruction occurs in real SKU triplets. A distributional study over representative instances is an important future-research item and would help distinguish an extremal theoretical phenomenon from a common planning risk.

### Conclusion

The conclusion accurately separates model certainty from operational uncertainty (lines 340–344). Until the central proof has passed specialist review, “The exact third item changes the mathematical frontier” should be softened to “The candidate demonstrates a three-item obstruction, conditional on the finite-closure theorem,” or reserved for the post-review version. The rest of the conclusion is appropriately bounded.

### References

The publisher-linked DOI correction and source-use audit are strengths. Complete the bibliographic metadata for reference 9, standardise venue/volume/page/year information, and pin all “current” comparisons to a cited version and access date. The successor should reproduce the exact statement and status of any theorem inherited from the parent, rather than asking readers to infer it from the predecessor release.

---

## Questions for Authors

1. Will you provide a fully self-contained proof, or a frozen proof appendix, for the finite generator, triple tail, and totality theorem—including the cap-feasibility details in the rational-approximation step—and identify exactly which claims remain conditional after specialist review?
2. What precise theorem is imported from the two-item parent to reduce arbitrary nonnegative resource systems to independent caps, and what assurance status does that inherited theorem have? Can the successor state it explicitly enough to be reviewed without relying on the release webpage?
3. What reproducible novelty/priority search has been conducted for equivalent three-item integrality-gap constructions and arithmetic closure methods, and how will the release distinguish “not found” from a priority claim?
4. Who will act as the accountable research guarantor and corresponding contact, respond to reviewer comments, disclose conflicts and funding, and own corrections while scholarly authorship remains Anonymous?

---

## Minor Issues

### Language / Grammar

- Manuscript line 324: reconcile “six escalating gates” with Gate 0 through Gate 6 in `LOGISTICS_DEPLOYMENT_PROTOCOL.md`.
- Manuscript line 342: qualify “changes the mathematical frontier” until the candidate theorem has passed specialist review.
- Consider replacing repeated “current” in relation to Segev’s bound with “as of 22 August 2026, arXiv v1” so the statement cannot silently become stale.

### Citation Format

- Reference 9 lacks the fuller journal/volume/page metadata supplied for most other journal articles.
- Add access/version information for the 2026 arXiv result and ensure every numerical comparison uses the same frozen version.
- State the parent cap-reduction theorem directly with a precise citation locator.

### Figures and Tables

- Add a witness-comparison table covering all three exact fixtures and their roles.
- Add a compact claim-dependency or evidence-state figure. It would materially clarify which consequences depend on the candidate finite-closure theorem.

### Layout and Release Metadata

- Ensure the “Unrefereed candidate; producer-side exact replay” status is visibly rendered in the PDF and HTML, not merely stored in front matter.
- Update `INTAKE_AUDIT.md` from 12 to 15 tests or explicitly label the 12-test count as an earlier v0.2 audit state.
- Update `README.md` line 49 so the certificate count matches the replay receipt and package map.
- Reconsider `date-released` in `CITATION.cff` while the package is explicitly not released; omit or replace it according to the chosen CFF policy until a public release exists.

---

## Dimension Scores

These uncalibrated scores are ordinal editorial signals, not venue-acceptance probabilities.

| Dimension | Score (0–100) | Descriptor | Notes |
|---|---:|---|---|
| Originality (20%) | 83 | Strong | A specific three-item obstruction, novel-looking closure architecture, and useful robustness insight; priority search remains incomplete. |
| Methodological Rigor (25%) | 59 | Weak | Exact arithmetic and replay are strong, but the global theorem rests on a candidate proof linchpin not yet fully adjudicated or self-contained. |
| Evidence Sufficiency (25%) | 71 | Adequate | Rich producer-side certificates and release records support local circulation; no unaffiliated rerun, specialist validation, or exhaustive novelty audit. |
| Argument Coherence (15%) | 84 | Strong | Clear chain from model to witness to implications, with a manageable but important split between paper and companion proof note. |
| Writing Quality (15%) | 86 | Strong | Precise, readable, and unusually careful about assurance; the abstract is dense and the hybrid genre needs clearer signalling. |
| Literature Integration (optional) | 64 | Adequate | Relevant core sources and excellent source-use boundaries, but insufficient breadth for priority positioning. |
| Significance & Impact (optional) | 81 | Strong | Strong subfield significance if correct; field impact is properly unclaimed and remains prospective. |
| **Weighted Average** | **74.6** | **Minor-revision numerical band; Major Revision editorial decision** | The numerical aggregate is overridden by the single-linchpin status of the global closure proof and release-accountability requirements. |

---

## Recommendation to Peer Reviewers

- **Mathematical optimisation/number-theory specialist**: test the finite-enumeration lemma, triple-tail factor, totality argument, cap-boundary cases, and fixed-(n) monotonicity; determine whether “exact global optimum” is fully justified.
- **Computational verification specialist**: examine oracle/verifier independence, shared primitives, mutation coverage, manifest/replay claims, and whether certificates verify theorem hypotheses rather than merely recomputing outputs.
- **Logistics/application specialist**: assess whether the operational mappings, eligibility gates, portfolio handoff, outcome set, and stop rules are realistic and whether any prose still invites an unwarranted transfer from synthetic mechanism to field benefit.
- **Editorial synthesizer**: preserve the distinction between (i) local candidate circulation, (ii) Evidence Press editorial-agent review, (iii) unaffiliated human specialist review, and (iv) public release approval. A role-based sub-agent process must not be relabelled as independent external peer review.
