# Peer Review Report

## Manuscript Information

- **Title**: An Exact Three-Item Independent-Cap Oracle and a Certified Multi-Item Relaxation-Gap Lower Bound
- **Manuscript ID**: Evidence Press exact-three-item-jrp-applications-v0.3.0-candidate
- **Review Date**: 22 August 2026
- **Review Round**: Round 1

---

## Reviewer Information

### Reviewer Role

Peer Reviewer 3 (Applications / Cross-disciplinary Perspective)

### Reviewer Identity

Operations-research and supply-chain implementation scholar specializing in inventory-policy translation, simulation-to-field handoffs, and operational experiment design. I approach the exact mathematics as an informed outsider and focus on whether the stated logistics uses remain valid after costing, feasibility, human decision-making, and field-identification constraints enter.

### Review Focus

Model-to-logistics semantics; realism of frequency caps and cost mappings; interpretation of holding-cost robustness; use of the five-policy portfolio; field-evaluation design; implementation feasibility; affected stakeholders; and the risk that exact synthetic findings could be mistaken for operational recommendations.

---

## Overall Assessment

### Recommendation

- [ ] **Accept**
- [ ] **Minor Revision**
- [x] **Major Revision**
- [ ] **Reject**

### Confidence Score

**4/5 — high confidence.** The operational translation and field-evaluation issues are within my expertise; I defer to the mathematical and software reviewers on the tail theorem and exact-oracle implementation.

### Summary Assessment

This manuscript presents an exact three-item deterministic joint-replenishment oracle, a certified synthetic relaxation-gap witness, and a staged proposal for using the oracle as a logistics diagnostic rather than an ordering controller. From an applications perspective, its strongest achievement is epistemic discipline: it repeatedly distinguishes a model mechanism from operational savings, labels the holding-cost boxes as local, and requires simulation, shadow operation, and prospective comparison before any value claim. The model-to-operation table and stop rules are unusually thoughtful for a mathematical paper. However, three release-gating ambiguities remain. First, a selected triplet may not be closed under the shared event: excluded SKUs can change both the event calendar and the defensible allocation of the common cost. Second, the bundled five-policy portfolio is witness-specific and should not be presented as the near-optimal portfolio for a newly fitted operational instance. Third, the field protocol gives no minimum design for interference, carryover, assignment unit, statistical precision, or horizon adequacy; “two representative cycles” is not a defensible universal minimum. The one-parameter holding-cost box also cannot stand in for joint uncertainty in costs, caps, demand, and calendars. These are repairable without new field results, but they require substantive clarification and re-review. I therefore recommend Major Revision before Evidence Press approval.

---

## Strengths

### S1: Clear separation of mathematical and operational evidence

The abstract expressly denies operational savings and field validation (manuscript lines 31–31), Section 8 classifies operational value as **untested** (lines 322–328), and the conclusion states that exact arithmetic cannot settle semantics or implementation value (lines 340–344). This reduces a common and consequential risk: readers interpreting a 14.87% relaxation gap as a 14.87% saving opportunity.

### S2: Credible first-pass semantic gate

The deployment protocol maps each mathematical term to a candidate operational meaning and a named validation obligation (protocol lines 7–18). It also rejects pointwise capacity, minimum order quantities, and nonlinear freight as automatic frequency-cap interpretations. The eligibility gate requires data reconciliation, coefficient ownership, a frozen comparator, and preservation of safety and contractual constraints (lines 20–29). These are appropriate foundations for bounded decision support.

### S3: Operationally responsible interpretation of near ties

The manuscript does not overcelebrate the unique nominal minimizer. It reports that four policies differ by only about \(1.75\times10^{-10}\) in the synthetic objective (lines 183–190), distinguishes the headline and margin witnesses (lines 261–277), and proposes carrying near-tied policies into simulation for service, workload, feasibility, and sensitivity criteria (lines 306–308). This is a valuable bridge from exact optimization to robust decision-making.

### S4: Strong staged evidence ladder and stop logic

The protocol separates exact stress testing, digital-twin simulation, shadow deployment, bounded field pilot, and monitored scaling (protocol lines 31–68). It records null triplets, requires preregistration, and lists service, expedites, workload, planner effort, integration cost, drift, and rollback criteria (lines 70–96). The explicit distinction between mechanism, feasibility, association, and causal impact is exemplary.

---

## Weaknesses

### W1: The three-SKU unit may not be closed under the common event

**Problem**: Section 6.1 asks analysts to select three SKUs sharing a supplier order, container, receiving session, inspection batch, or changeover and then estimate \(K_0\) (manuscript lines 294–300). In most real systems, those events are also shared by other SKUs. Their replenishment epochs can create “free” alignment opportunities for the selected triplet, while allocating the whole common event cost to three SKUs can overstate their incremental cost. The current semantic-fit gate does not require event closure or specify a background calendar.

**Why it matters**: The mathematical oracle prices the union of exactly three event streams. Applying it to a nonclosed subset changes the economic object, so even a perfectly estimated triplet can diagnose an artefact of cost allocation or omitted-event interference.

**Suggestion**: Add a mandatory **event-closure test**. Either (a) require that the triplet is the complete set controlling the event, (b) condition analysis on a frozen exogenous background event calendar and estimate marginal event cost, or (c) label the result software-only and prohibit operational interpretation. Report the proportion of shared events initiated by nonselected SKUs and sensitivity to defensible \(K_0\) allocation rules.

**Severity**: **Major**

### W2: The registered five-policy portfolio is synthetic, not instance-specific

**Problem**: Gate 2 directs a new operational analysis to compare “the registered five-policy portfolio in `analysis/policy_portfolio.json`” (protocol lines 41–50). That file contains policies constructed around the two synthetic witnesses, not an \(\varepsilon\)-near-optimal set recalculated from the fitted triplet. The same multipliers may be infeasible, dominated, or irrelevant under empirical coefficients and calendars.

**Why it matters**: This conflates two defensible but distinct uses: frozen regression fixtures for software assurance, and candidate policies for a specific operational decision. The latter must be generated from the actual fitted instance.

**Suggestion**: Split Gate 2 into (i) **software regression**, using the frozen v0.2 and active-envelope fixtures, and (ii) **instance-specific policy generation**, retaining every oracle policy within a preregistered absolute or relative regret tolerance after cap and calendar checks. The operational simulation should receive only the second set, with the frozen five patterns optionally added as diagnostic controls.

**Severity**: **Major**

### W3: The robustness certificate varies only holding costs

**Problem**: Section 4.4 proves a mathematically valid box in \((H_1,H_2,H_3)\) while keeping \(K_0\), \(K_i\), caps, demand semantics, and calendars fixed (manuscript lines 243–259). Section 6.3 cautions that this is local coefficient stability (lines 306–308), but the deployment protocol does not prescribe the broader uncertainty analysis needed before policy comparison.

**Why it matters**: In practice, event-cost allocation and cap semantics may be less stable than holding rates. Correlated changes in demand and carrying cost also invalidate an independent-coordinate interpretation of \(H_i\). The exact box therefore cannot quantify operational robustness.

**Suggestion**: Require a joint, empirically justified uncertainty set over \(K_0,K_i,H_i,\bar f_i\), background-event attribution, and calendar feasibility. Report policy rank, regret, feasibility frequency, service metrics, and worst-case outcomes across that set. Name the certified box “holding-cost rank stability for the synthetic fixture” wherever it enters the handoff.

**Severity**: **Major**

### W4: Field duration and identification are under-specified

**Problem**: The protocol permits entry with “at least six months” of data (line 25), calls for shadow operation over “at least two representative cycles” (lines 58–60), and allows a randomized, stepped, or otherwise defensible concurrent pilot (lines 62–64). It does not define the experimental unit, interference among triplets sharing suppliers or docks, carryover/washout, warm-up inventory, power or precision, seasonality coverage, noncompliance estimand, or multiplicity across outcomes and selected triplets.

**Why it matters**: Replenishment policies have inventory-state carryover and network interference. A short or SKU-level comparison can bias cost and service estimates even when assignment is randomized. Six months and two cycles are not portable quality thresholds.

**Suggestion**: Replace fixed minimum durations with a design-adequacy gate: enough preperiods and policy cycles to cover forecast regimes and estimate the preregistered service margin and net-value estimand at target precision. Require an assignment/interference map, warm-up and carryover rules, intention-to-treat handling of overrides, a sample-size or simulation-based precision analysis, and cluster or switchback randomization where shared resources prevent independent assignment.

**Severity**: **Major**

### W5: Stakeholder ownership is incomplete

**Problem**: The paper assigns the bridge jointly to operations, procurement, finance, warehouse, and service stakeholders (lines 310–320). Suppliers, carriers, frontline workers, customers, IT/security, sustainability owners, and—where regulated goods are involved—quality/regulatory teams are not explicitly included. The protocol measures planner effort but not distributional workload, supplier burden, emissions, waste, or contractual renegotiation.

**Why it matters**: A lower-cost calendar may shift peaks or risk to another organization, workforce, or customer group. Such transfers can produce false “net value” and undermine implementation.

**Suggestion**: Add a stakeholder/RACI and impact-boundary table. At minimum, identify cost and risk transfers to suppliers, carriers, labor shifts, customers, IT operations, and environmental metrics; require signed ownership for overrides, incidents, and rollback.

**Severity**: **Minor**

---

## Detailed Comments

### Assumption Audit

- **Explicit assumptions**: The deterministic stationary, periodic, rational-cap abstraction is stated clearly (manuscript lines 47–65), and omitted stochastic and quantity constraints are acknowledged (lines 310–318). The operational protocol must test these assumptions rather than merely document them.
- **Implicit assumptions**: The handoff currently presumes that a chosen triplet economically owns the shared event and that the frozen synthetic neighbours are relevant candidates for a fitted triplet. Neither premise follows from the exact certificate; W1 and W2 propose observable gates.
- **Paradigmatic assumptions**: The mathematical objective treats relevant costs as additive and decision rights as downstream. An operational evaluation should also test cost/risk transfers, endogenous planner and supplier responses, and whether the policy changes the data-generating process used to estimate its coefficients.

### Title & Abstract

- The title accurately foregrounds the exact mathematical contribution and does not promise logistics savings.
- The abstract’s assurance boundary is strong (lines 29–31). Add one phrase stating that the five policies are **synthetic witness policies**, not a universal operational shortlist.
- “A conservative logistics handoff” is fair only if W1–W4 become explicit release gates rather than optional good practice.

### Introduction and Model-to-Operation Semantics

- The manuscript correctly explains that the percentage is relaxation optimism, not realized saving (lines 43–45).
- The \(H_i/f_i\) mapping should spell out the quantity relationship behind \(H_i=h_i d_i/2\): constant deterministic demand, instantaneous or otherwise specified replenishment, cycle stock without safety stock, and consistent time/currency units. The protocol currently says “often” (line 13), which is cautious but not auditable.
- A hard minimum time between successive orders and a maximum long-run average frequency are not generally equivalent outside a periodic policy. The cap owner should certify which constraint is actually enforced and the operational layer should recheck every generated calendar.
- Add the event-closure test in W1 before any triplet is treated as a logistics instance.

### Results and Robustness

- The contrast between the stronger but fragile headline fixture and the less-fragile margin fixture is an excellent application lesson (manuscript lines 247–277).
- Present the robustness box with a short “fixed / varied / omitted” table. This would prevent the impressive phrase “proves—not samples—the whole box” (line 245) from being read as a broader uncertainty claim.
- The portfolio’s relative tolerance of 0.0001% is computationally clear but operationally far below plausible parameter error. For fitted instances, choose the tolerance by decision materiality and simulation precision rather than inheriting this synthetic threshold.

### Logistics Role and Deployment Protocol

- The diagnostic and software-regression roles are credible (lines 294–304).
- Reframe “robust policy set” as “candidate set for robustness evaluation”; the current candidates are nominally near-tied, not yet robust.
- Define “material exact-relaxation gap,” “bounded regret,” “positive net value,” “representative cycle,” and each allowed stop-rule proportion before deployment. Require uncertainty intervals and a cost-accounting boundary, not only point estimates.
- Record rejected and ineligible triplets as well as eligible null findings. Otherwise, the semantic-fit gate itself can create selection bias in the reported application landscape.

### Field-Evidence Programme

- The evidence-state ladder (manuscript lines 322–328; protocol lines 94–96) should remain prominent in any Evidence Press release page.
- Add a minimum preregistration schema: unit of assignment; estimand; comparison policy; interference graph; carryover/warm-up; horizon rationale; precision target; noninferiority margin; override/noncompliance treatment; missingness and attrition; multiplicity; cost boundary; and stopping authority.
- A shadow comparison establishes more than technical executability only when overrides and infeasibilities are logged with reasons. Separate policy infeasibility, planner disagreement, and data/integration failure.

### Conclusion

- The final assurance statement is appropriately conservative (lines 340–344).
- Change “construct near-optimal policy sets” (line 342) to “construct **instance-specific deterministic candidate sets**.” Near-optimality under the synthetic objective is not service feasibility or operational robustness.

### References

- Reference 6 uses the wrong title. The journal record gives T. S. Winter and J. H. van Vuuren, “A Practical Method for Joint Inventory Replenishment under Supplier Constraints,” *SAJIE* 36(2), 1–16 (2025), DOI 10.7166/36-2-3194.
- Reference 7 has the wrong title and volume. The publisher record gives “Integration of sales, inventory, and transportation resource planning by dynamic-demand joint replenishment problem with time-varying costs,” *Computers & Industrial Engineering* **188**, 109922 (2024), not volume 190.
- Reference 8 has the wrong title and incomplete bibliographic data. It is S. Creemers and R. Boute, “The joint replenishment problem: Optimal policy and exact evaluation method,” *European Journal of Operational Research* 302(3), 1175–1188 (2022), DOI 10.1016/j.ejor.2022.02.005.

---

## Cross-Disciplinary Reading Recommendations

1. I. Bojinov, D. Simchi-Levi, and J. Zhao, “[Design and Analysis of Switchback Experiments](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4583),” *Management Science* 69(7), 3759–3777. Directly relevant to policy carryover and time-based randomization when a dock, supplier, or site cannot run simultaneous independent treatments.
2. D. Holtz et al., “[Reducing Interference Bias in Online Marketplace Experiments Using Cluster Randomization](https://pubsonline.informs.org/doi/10.1287/mnsc.2020.01157),” *Management Science* (2024). Although from marketplace experimentation, its interference logic transfers to SKU clusters sharing orders, transport, and capacity.
3. M. R. Ibanez and B. R. Staats, “[Field Experiments in Operations Management](https://pubsonline.informs.org/doi/pdf/10.1287/educ.2019.0197),” *INFORMS Tutorials in Operations Research* (2019). Provides a practical field-design checklist covering treatment, implementation, partners, behavior, and identification.
4. A. Tschan et al., “[Data-Driven Inventory Control and Integrated Employee Involvement for Special Buys at ALDI SÜD Germany](https://pubsonline.informs.org/doi/10.1287/inte.2024.0182),” *INFORMS Journal on Applied Analytics* (2025). Useful for connecting optimization, simulation, controlled comparison, seasonal effects, implementation, and employee workload.
5. L. Wang and H. Chen, “[Optimization of a Stochastic Joint Replenishment Inventory System with Service Level Constraints](https://doi.org/10.1016/j.cor.2022.106001),” *Computers & Operations Research* 148, 106001 (2022). Offers a complementary operational policy class where service constraints and stochastic demand are part of the optimization rather than downstream checks.

---

## Questions for Authors

1. Under what observable condition is a selected three-SKU group considered closed with respect to the common event, and how will \(K_0\) be estimated when other SKUs also trigger or join that event?
2. Will the software generate an instance-specific near-optimal portfolio for every fitted triplet? If not, what justifies transferring the five synthetic patterns into an empirical simulation?
3. What is the intended unit of assignment for the bounded field pilot—SKU triplet, supplier, receiving location, calendar period, or another cluster—and how will shared-resource interference and inventory-state carryover be handled?
4. Which joint parameter-uncertainty set will Gate 3 use, and what empirical evidence will determine its bounds and dependence structure?

---

## Minor Issues

### Language / Terminology

- Define “bounded regret” in protocol line 75, including its comparator and whether the bound is deterministic, simulated, or statistical.
- Replace “robust policy set” with “candidate policy set for robustness evaluation” unless robustness has actually been established under the operational model.
- State all time and monetary units in the fitted-instance schema; normalized synthetic frequencies are not directly calendar periods.

### Citation Format

- Correct References 6–8 as detailed above and synchronize `SOURCES.md` with the manuscript bibliography.
- Give volume, issue, and page/article information consistently for every journal article.

### Figures and Tables

- Add one compact table separating: certified mathematical inputs, operationally estimated inputs, omitted operational features, and the evidence state reached at each gate.
- A small diagram showing triplet closure versus a triplet embedded in a larger shared-event cluster would materially clarify W1.

---

## Dimension Scores

These uncalibrated rubric scores are ordinal review aids, not venue-acceptance probabilities.

| Dimension | Score (0–100) | Descriptor | Notes |
|---|---:|---|---|
| Originality (20%) | 84 | Strong | Novel exact mechanism plus unusually explicit applications boundary. |
| Methodological Rigor (25%) | 66 | Adequate | Exact work appears carefully packaged, but the applied evaluation protocol lacks closure, interference, carryover, and precision requirements. |
| Evidence Sufficiency (25%) | 60 | Adequate | Strong synthetic certificate evidence; deliberately no field evidence; practical literature and validation design remain limited. |
| Argument Coherence (15%) | 84 | Strong | The model-to-evidence logic is clear, with some slippage between frozen fixtures and instance-specific candidates. |
| Writing Quality (15%) | 88 | Strong | Precise, readable, and exceptionally cautious; a few operational terms need definitions. |
| Literature Integration (optional) | 70 | Adequate | Appropriate initial operational sources, but field-experiment and interference literature should be integrated. |
| Significance & Impact (optional) | 78 | Strong | High value as a benchmark and warning about relaxation optimism; operational influence depends on the proposed revisions. |
| **Weighted Average** | **74.1** | **Minor Revision by numeric rubric; Major Revision release-gate recommendation** | Major Revision is driven by correctable but consequential application-transfer defects requiring re-review. |

**Weighted calculation**: \(0.20(84)+0.25(66)+0.25(60)+0.15(84)+0.15(88)=74.1\).
