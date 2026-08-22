# Peer Review Report

## Manuscript Information

- **Title:** An Exact Three-Item Independent-Cap Oracle and a Certified Multi-Item Relaxation-Gap Lower Bound
- **Manuscript ID:** Evidence Press JRP3 v0.3.0 frozen submission
- **Review Date:** 22 August 2026
- **Review Round:** First-round review

## Reviewer Information

### Reviewer Role

Peer Reviewer 1 (Methodology)

### Reviewer Identity

Exact-optimisation and computational-proof reviewer with expertise in finite enumeration, exact algebraic certificates, adversarial verifier testing, and reproducible mathematical software.

### Review Focus

I assess whether the exact optimisation design closes the infinite schedule space, whether the finite generator and tail arguments support the claimed oracle, and whether the certificate, mutation-control, and replay boundaries are strong enough for an Evidence Press release. Literature priority and operational impact are outside this report except where they affect claim scope.

## Overall Assessment

### Recommendation

- [ ] **Accept**
- [ ] **Minor Revision**
- [x] **Major Revision**
- [ ] **Reject**

### Confidence Score

**4/5 — High confidence.** The exact optimisation, enumeration, and reproducibility questions are within my expertise. A specialist in simultaneous Diophantine approximation should additionally audit the totality argument.

### Summary Assessment

The manuscript constructs a three-item independent-cap joint-replenishment oracle by partitioning commensurability regimes, optimizing each fixed pattern exactly, enumerating primitive triples under a second-pair-complexity cutoff, and bounding the omitted tail. It reports a rational witness with exact gap (1.1487291464748205845\ldots), then derives fixed-item monotonicity and vertex-certified holding-cost boxes. Methodologically, the package is unusually explicit: rational inputs, exact radical comparisons, finite certificate fields, mutation tests, and candid assurance limits are all valuable. In a read-only reviewer-side run, all 15 bundled tests passed and the 108-file manifest verified; this confirms functional replay on the producer's recorded environment, not theorem correctness or independence. The principal weakness is that the global oracle depends on generator, tail, and especially termination arguments that remain candidate prose rather than a complete journal-level proof or independently checked formalisation. The checker also shares core algebra with the solver, while path-dependent generated reports and incomplete certificate-schema validation weaken the reproducibility claim. These are serious but fixable assurance gaps rather than evidence that the numerical witness is wrong. I therefore recommend major revision and re-review before Evidence Press approval.

## Strengths

### S1: Correct decomposition of the infinite policy space

The commensurability relation is used to produce three exhaustive regimes, with explicit attention to closures and accidental extra rational relations (manuscript §3.1, lines 69–77). This is the right organising principle and prevents boundary optima from falling outside the audit.

### S2: Exact fixed-pattern optimisation

For a primitive triple, the manuscript reduces the objective to (A_{\mathbf a}/t+B_{\mathbf a}t), derives the cap floor (t_{\min}), and identifies the exact rational-or-radical minimizer (manuscript §3.2, lines 79–113). The implementation mirrors this calculation using rational `Fraction` values and exact `ScaleCost` comparisons (`src/jrp3/oracle.py`, lines 362–414), avoiding floating-point decisions in the certified optimum.

### S3: Structurally appropriate finite cutoff

The second-smallest reduced pair complexity addresses a real failure of naive coordinate-box truncation. The supplement proves a finite component bound and the generator is checked against brute force for cutoffs (S=2,\ldots,6) (`docs/three_item_oracle_note.md`, lines 240–291; `tests/test_oracle.py`, lines 84–96). This is much stronger evidence than merely searching a large cube.

### S4: Explicit global-tail margin for the bundled witness

The paper reports the boundary value, minimal closing cutoff (S=21), 49,981 enumerated triples, and the strict omitted-tail comparison (manuscript §4.1, lines 157–168). The verifier recomputes pair minima, triple minima, cutoff minimality, tail values, and the exact gap (`src/jrp3/verify.py`, lines 225–307).

### S5: Honest assurance and robustness boundaries

The manuscript clearly states that the checker is same-producer and that shared provenance prevents it from constituting independent verification (manuscript §5, lines 281–292). The holding-box result uses a sound fixed-schedule affinity/vertex argument and explicitly limits the box to holding-cost perturbations (manuscript §4.4, lines 243–259; §6.3, lines 306–308).

## Weaknesses

### W1: The global totality proof is not yet journal-complete

**Problem:** The main manuscript compresses the triple-tail theorem to one paragraph and delegates the derivation to a package note (manuscript §3.4, lines 119–133). The supplementary termination argument asserts (O(q^{-2})), (O(q^{-3/2})), and \(\Omega(q^{-1})\) perturbation/saving rates without stating constants, constructing the required one-sided or simultaneous approximants in full, or treating every cap-binding configuration explicitly (`docs/three_item_oracle_note.md`, lines 355–369). The paper itself labels the finite generator and tail as requiring specialist audit (lines 330–337).

**Why it matters:** The exact lower bound is global only if every omitted commensurable pattern and every boundary regime is covered. This theorem is the single linchpin connecting a finite 49,981-pattern search to an infinite-domain optimum.

**Suggestion:** Add a self-contained theorem-proof appendix with quantified lemmas for pair-tail closure, triple-tail closure, and finite termination. Spell out cap-feasibility restoration and all rational/irrational boundary cases. Have a number-theory/OR specialist independently check the proof, or formalise the generator and tail inequalities in a proof assistant.

**Severity:** **Major**

### W2: Producer replay is not an independent certificate validation

**Problem:** The checker reimplements the high-level enumeration but imports the same `ScaleCost`, `exact_compare`, rational conversion, and instance model used by the discovery solver (`src/jrp3/verify.py`, lines 13–16). Both implementations were produced in the same workflow. The manuscript acknowledges this correctly (lines 281–292), but the release has no second-language/CAS reconstruction or unaffiliated rerun (lines 330–337).

**Why it matters:** A shared error in algebraic sign comparison, input semantics, or the underlying tail theorem can pass both solver and checker. Passing the bundled test suite establishes internal consistency, not an independent proof.

**Suggestion:** Make approval require either (a) an unaffiliated implementation that reads only the public instance and certificate specification, preferably using a distinct language/CAS, or (b) a line-by-line independent mathematical audit plus a separate minimal verifier. Preserve producer replay as its own assurance layer rather than renaming it.

**Severity:** **Major**

### W3: Clean replay is functional but not location-independent or byte-reproducible

**Problem:** The replay script rebuilds certificates but does not run a manifest comparison after generation (`scripts/reproduce.sh`, lines 1–21). The extension builder passes absolute `Path` objects into verification (`scripts/build_extensions.py`, lines 199–214), and reports serialize `str(certificate_path)` (`src/jrp3/verify.py`, lines 309–318; `src/jrp3/extensions.py`, lines 205–216). Consequently, 18 frozen robustness reports contain the producer's original absolute successor path rather than a package-relative path. The pre-replay 108-file manifest passes, but regeneration in a different extraction directory changes those report bytes.

**Why it matters:** The receipt's “clean-extraction replay passed” is valid as a functional statement, but it does not yet establish canonical regenerated artifacts. Path leakage also reduces portability and complicates third-party checksum comparison.

**Suggestion:** Serialize repository-relative identifiers, add a clean temporary-directory test, and compare all regenerated declared artifacts with the manifest or a separately frozen expected-output manifest after replay. State explicitly whether the reproducibility target is functional equality, semantic equality, or byte identity.

**Severity:** **Major**

### W4: Certificate-schema and mutation controls are incomplete

**Problem:** The manuscript says certificate fields are mandatory and structural mutations are rejected (manuscript §5, lines 283–290), but the verifier parses declared relaxation frequencies with unrestricted `sp.sympify` and checks them through `zip` without enforcing exactly three entries (`src/jrp3/verify.py`, lines 216–223). An empty frequency list therefore vacuously passes that particular check. Several descriptive fields and nested shapes are not schema-validated. The mutation suite covers one altered optimum and three structural changes only (`tests/test_oracle.py`, lines 188–223).

**Why it matters:** The core cost is still recomputed, so this does not overturn the witness. It does mean the certificate format is less strict and less safe for untrusted public inputs than the prose suggests.

**Suggestion:** Introduce a versioned JSON Schema or equivalent explicit validator; enforce exact list lengths, required keys, types, uniqueness, and safe expression grammar everywhere; remove raw `sympify` on certificate text; and add property-based mutation/fuzz tests for truncation, duplication, unknown fields, malformed radicals, and omitted records.

**Severity:** **Major**

### W5: The stationary-family certificate does not reconstruct its own elimination

**Problem:** The manuscript describes an “exact elimination” yielding a stationary point (manuscript §4.2, lines 192–220), while the build script hard-codes the degree-22 polynomial and then uses numerical `nroots` to report the relevant point (`scripts/build_extensions.py`, lines 32–41 and 98–120). It exactly counts roots in the declared interval, but it does not regenerate the resultant or provide an exact stationarity/substitution certificate tying that polynomial to the objective.

**Why it matters:** The authors correctly label this calculation a discovery guide, so the certified rational lower bound is unaffected. Nonetheless, “exact elimination” currently has weaker replay semantics than the phrase suggests.

**Suggestion:** Generate and factor the resultant symbolically from the declared equations, record removable factors and admissibility conditions, and certify the sign/branch conditions in the isolating interval. Otherwise relabel the reported stationary point as a reproducible numerical guide.

**Severity:** **Minor**

## Detailed Comments

### Title & Abstract

- The title accurately identifies the independent-cap and lower-bound scope.
- The abstract is commendably explicit about absent peer review and operational validation (lines 10–31). Until W1 is resolved, consider “candidate exact oracle” or “conditional on the finite-closure theorem” next to the global-optimum wording; the YAML status line alone may be missed.
- “Certified” should continue to refer to the frozen instance calculation under the stated candidate-proof boundary, not to external theorem certification.

### Introduction and Model

- The distinction between relaxation optimism and realised savings is excellent (lines 43–45).
- The independent-cap input scope is clear (lines 47–65). For a stand-alone paper, state the imported parent cap-reduction theorem and its hypotheses more fully rather than relying only on the predecessor release.
- Define explicitly which asymptotic density notion is used and note that the common origin contributes zero density; this would eliminate a minor foundational ambiguity in equation (1).

### Exact Finite Closure / Research Design

- The three-regime design is appropriate and appears exhaustive.
- The fixed-triple and one-pair subproblems are aligned with the objective and cap constraints.
- The triple-tail inequality itself has a plausible and coherent chain in the supplement: retain the least-complex pair, bound the other two intersections, and scale frequencies. I found no counterexample in the bundled bounded regression. The remaining issue is proof completeness and totality, not an identified numerical contradiction.
- The generator test against brute force only reaches (S=6), whereas the certificate uses (S=21). The mathematical lemma can bridge that gap, but an independently generated (S=21) count or formal generator proof would materially strengthen assurance.

### Results / Exact Witness

- Exact fractions, the winning multiplier, cap-bound scale, enumeration count, boundary threshold, and runner margin are all reported (lines 137–190).
- The near-tie is correctly treated as fragility rather than as evidence of a uniquely robust operational policy.
- The monotonicity argument (lines 222–241) is concise and appears valid: deleting the appended item weakly lowers exact cost, while the relaxation incurs a vanishing (\varepsilon/f_0) term. Specify the chosen new cap and (f_0) in theorem notation to make quantifiers fully explicit.

### Robustness Analysis

- The eight-vertex argument is stronger than sampling and is logically appropriate because every fixed feasible schedule has affine holding-cost dependence (lines 243–259).
- The verifier checks cap-boundedness only at vertices; add the one-line affine inequality showing this property throughout the box. The vertex conditions imply it, but an explicit statement would close the presentation.
- The reported radii are local (H)-box certificates only; the manuscript consistently avoids extending them to cap, demand, or service uncertainty.

### Software, Certificates, and Reproducibility

- Reviewer-side execution with `PYTHONDONTWRITEBYTECODE=1` passed all 15 tests in 57.272 seconds, and `scripts/manifest.py --check` passed all 108 entries. This is a same-package, same-platform rerun and must not be recorded as unaffiliated independent reproduction.
- Exact input rejection of JSON floats is appropriate. Extend the same strictness to every nested certificate field.
- `requirements-lock.txt` pins direct mathematical dependencies but provides no hashes, wheel provenance, or complete environment lock. A container/Nix/uv lock or equivalent cross-platform recipe would improve reproducibility.
- Rename test `test_independent_verifier`; “solver-independent producer verifier” matches the manuscript's assurance boundary.

### Statistical Reporting Adequacy

Not applicable. This is a theoretical/computational exact-optimisation paper, not a sampled empirical study. Effect sizes, confidence intervals, power, missing-data procedures, and statistical assumption tests do not apply. The reported percentages are deterministic transformations of exact rational quantities and should remain labelled as model metrics.

### Discussion, Limitations, and Conclusion

- The limitations section is unusually strong and correctly lists specialist audit, independent rerun, formalisation, and field-validation gaps (lines 330–338).
- The conclusion mostly stays within the evidence (lines 340–344). “Certified candidate ratio” is acceptable only if the assurance ledger remains attached and the release page avoids shortening it to “certified exact constant.”

## Questions for Authors

1. Can the authors supply a fully quantified termination proof covering all cap-binding boundary configurations, including the exact one-sided/simultaneous approximation lemmas used in `docs/three_item_oracle_note.md` lines 355–369?
2. What artifact will constitute genuinely independent approval: an unaffiliated rerun of this code, a separately written verifier, a formal proof of the tail/generator, or a specified combination of these?
3. Is the intended clean-replay criterion functional success, semantic equality of recomputed certificates, or byte-identical regeneration? How will the absolute-path fields be canonicalised and checked after replay?
4. Can the degree-22 stationary polynomial be regenerated from the active-family equations, with resultant factors and admissible-branch conditions recorded rather than supplied as a hard-coded polynomial?

## Minor Issues

### Terminology

- Replace “independent verifier” in the CLI/test naming with “solver-independent producer verifier.”
- In `src/jrp3/extensions.py` lines 83–90, the docstring says “concavity then fills the whole box”; the implemented proof and manuscript use fixed-schedule **affinity**, which is the more precise term.

### Certificate Presentation

- Add a compact table in the manuscript giving all three pair-boundary cutoffs and optima; these currently appear only in the supplement for the margin witness.
- Give the exact rational robustness radii in an appendix or direct certificate reference, not only decimal approximations in the paper.

### Reproduction Metadata

- Record CPU architecture, command durations, locale, and dependency hashes in a machine-readable environment receipt.
- Avoid absolute local paths in public JSON artifacts and provenance fields unless explicitly marked noncanonical.

## Dimension Scores

These scores are ordinal review aids, not calibrated acceptance probabilities.

| Dimension | Score (0–100) | Descriptor | Notes |
|---|---:|---|---|
| Originality (20%) | 82 | Strong | Novel three-item exact-certificate construction and active-envelope obstruction |
| Methodological Rigor (25%) | 64 | Adequate | Strong exact finite computation; central totality proof and certificate validation need substantial strengthening |
| Evidence Sufficiency (25%) | 62 | Adequate | Exact bundled evidence is strong, but globality depends on one not-yet-independently-audited proof chain |
| Argument Coherence (15%) | 84 | Strong | Clear separation of theorem, computation, applications, and open obligations |
| Writing Quality (15%) | 86 | Strong | Precise, readable, and unusually well calibrated |
| Literature Integration (optional) | Not scored | R2 focus | Outside this methodology review |
| Significance & Impact (optional) | Not scored | R3 focus | Outside this methodology review |
| **Weighted Average** | **73.4** | **Minor-revision numerical band; Major Revision recommendation** | The unresolved global-proof and independent-assurance gates override the aggregate score and require re-review |

## Final Methodology Judgment

The frozen package provides credible producer-side evidence for the stated rational witness and a promising candidate proof of globality. It is not yet a journal-grade independent certification of the infinite-domain optimum. Evidence Press approval should require resolution of W1–W4 and a methodology re-review; W5 may remain a clearly labelled discovery-only calculation if the wording is narrowed.
