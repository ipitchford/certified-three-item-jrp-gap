# Research extension report: items 1–3

Date: 22 August 2026  
Candidate: `exact-three-item-jrp-applications-v0.3.1-candidate`  
Decision: **PASS_WITH_NOTES after bounded Editor closure; public identity and deployment gates remain**

## Executive judgement

All three requested extensions remained fruitful and have been incorporated into the v0.3 successor. They produce one theorem-level implication, one stronger exact lower-bound witness, and one operationally important robustness result. Further local tuning of the same five-policy family now has sharply diminishing value: the new rational witness is within roughly `2.9e-11` of the family's numerical stationary value, while its certified holding-cost radius is more than four orders of magnitude smaller than the retained v0.2 margin witness.

The strongest defensible research message is therefore not merely “a slightly larger number.” It is:

1. three items provably cross the certified two-item ceiling within the stated candidate-proof boundary;
2. that obstruction propagates to every fixed item count `n >= 3` for the same independent-cap relaxation;
3. the near-active construction explains why the gap occurs; and
4. approaching that construction creates severe coefficient fragility, so every fitted logistics instance must regenerate and verifier-check its own candidate set rather than transfer the synthetic fixture or deploy one nominal schedule.

## 1. Fixed-item monotonicity and the relaxation barrier

Let `Gamma_(n,box)` denote the worst exact-to-relaxed ratio for `n` items under independent frequency caps. Append an item with zero item-specific setup cost, holding coefficient `epsilon > 0`, and a cap that admits some fixed positive frequency. Deleting the appended item from any exact `(n+1)`-item schedule leaves a feasible `n`-item schedule with no greater cost, while the relaxed `n`-item optimum can be extended at additional cost tending to zero with `epsilon`.

Taking `epsilon -> 0` gives the candidate lemma

`Gamma_(n+1,box) >= Gamma_(n,box)`.

Consequently the bundled exact three-item ratio

`7732648297718008589674913778809 / 6731480890380196637385597557508`

is also a lower bound for every fixed item count at least three. It is therefore a barrier to any universal guarantee measured solely against this particular independent-cap relaxation: such an analysis cannot certify a multiplicative constant below the displayed ratio. This does not rule out stronger relaxations or analyses using additional structure.

## 2. Bounded five-policy active-envelope search

With caps `(x,y,1)`, common setup cost one, and zero item-specific setup costs, four primitive policies

`(2,1,1), (2,2,1), (3,2,2), (4,3,2)`

tie exactly on the rational family

`H1 = 2 y^2 / 3`, `H2 = 2/3`,

`H3 = -(4 y^3 - 7 y^2 + 7 y - 2) / (3(y-1))`.

Their common cost is `(3 y^2 - 5)/(3(y-1))`. Equality with the eventual winning policy `(3,3,2)` is controlled by

`18x^2y - 18x^2 - 9xy^2 + 15x - 2y^3 + 8y^2 - 8y - 2 = 0`.

Exact elimination produces the archived degree-22 stationary polynomial. Its unique root in the stored rational isolating interval gives the numerical guide

`y* = 0.7673150396176354748...`,

`x* = 0.6040916335357804026...`,

with family ratio `1.1487291465036805297...`. This is a discovery guide inside one bounded active family, not an exact value of the global three-item constant.

The selected rational point is

`x = 56015/92726`, `y = 153463/200000`,

`H1 = 23550892369/60000000000`, `H2 = 2/3`,

`H3 = 2113788266473847/1396110000000000`.

The exact oracle proves that `(3,3,2)` at scale `92726/168045` is globally optimal for this instance, using 49,981 primitive triples and minimal closing cutoff `S=21`. The exact gap is

`1.1487291464748205845264...`.

This improves the retained v0.2 witness by about `3.67e-7` in absolute ratio and lies about `2.9e-11` below the family's numerical stationary guide. More tuning of the same family is therefore unlikely to change the research conclusion materially.

## 3. Exact robustness chamber and regression portfolio

For fixed caps and a fixed schedule, cost is affine in the holding-cost vector. If the same cap-bound schedule is globally optimal at all eight vertices of a three-dimensional holding-cost box, every competing fixed schedule has nonnegative affine cost difference at every vertex and hence throughout the box.

The package supplies exact oracle certificates for all sixteen vertices of two boxes:

| Witness | Relative simultaneous holding-cost radius | Role |
|---|---:|---|
| Active-envelope headline witness | `292901133283274471191/3039290287366368373970172442382` = `9.637155572...e-11` | strongest certified lower bound |
| Retained v0.2 margin witness | `86013857588/70692800851712719` = `1.216727255...e-6` | substantially more stable stress-test fixture |

The same `(3,3,2)` schedule is certified throughout each corresponding box, conditional on the candidate finite-closure theorem and same-producer verification boundary. These are local coefficient certificates, not evidence of robustness to stochastic demand, lead times, nonlinear tariffs, service constraints, or implementation error.

For each synthetic witness the generated artifact contains five near-tied primitive policies, but those sets are frozen **regression fixtures only**. A fitted logistics instance must regenerate one verifier-checked candidate universe across every certified primitive triple and all boundary regimes under a preregistered exact tolerance, then apply its own calendar and operational-feasibility rules. A nominal policy switch near the active envelope is a sensitivity signal, not a reason to execute orders automatically.

## Quantitative interpretation

- Exact three-item relaxation optimism: `14.8729146475%` relative to the relaxed denominator.
- Equivalent shortfall: `12.9472771655%` relative to the exact optimum.
- Above the producer-side unrefereed two-item upper endpoint: `3.3132383589%`.
- Remaining multiplicative interval to the cited general upper bound: `4.6587762744%`.

These are mathematical ratios on a normalized synthetic instance. They are not savings, service improvements, or field impacts.

## Stop/go judgement

The three extensions have reached a sensible local stopping point.

- **GO:** circulate the frozen v0.3 candidate for unaffiliated mathematical review and clean-room replay.
- **GO:** use both certified fixtures for software regression; for logistics simulation or shadow evaluation, regenerate and verifier-check an instance-specific candidate set under preregistered tolerance and feasibility rules.
- **HOLD:** do not claim the exact three-item or unrestricted constant.
- **HOLD:** do not turn the `14.8729%` ratio into a savings claim.
- **HOLD:** do not publish until immutable identity, archive, site integration, and live-readback gates are separately authorised and passed.

The next mathematically valuable work is qualitatively different: a universal three-item upper certificate, an independent derivation of the active-envelope result, or a search over genuinely different active families. Merely adding more digits or rational refinements to the present five-policy family is no longer a high-value extension.

## Replay result and assurance ceiling

The repaired local suite contains twenty-one deterministic tests, including one-field representation mutations, complete portfolio reconstruction, and path-containment controls. Ordinary Python, optimized Python, and a fresh archive extraction all pass; ordinary/optimized/fresh runs match the 61-file generated ledger, and the extracted copy passed its 140-entry manifest before replay. The package contains three point certificates, sixteen exact robustness-vertex certificates, two holding-box reports, and enumeration/tail-complete regression portfolios. The rebuilt 16-page PDF has zero raw-TeX findings, embedded fonts, and page-by-page visual approval; it is untagged, with the Markdown source retained as the accessible route.

This is a same-producer, solver-independent, anonymous unrefereed candidate. It is not an unaffiliated reproduction, independent reimplementation, formal verification, specialist review, editorial peer review, or operational validation.
