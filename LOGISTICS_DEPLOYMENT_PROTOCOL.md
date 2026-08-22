# From exact certificate to logistics evidence

## Purpose

This protocol turns the three-item oracle into a controlled decision-support experiment. It does not permit direct autonomous ordering. Its job is to identify when a simple relaxation is materially optimistic, generate exact small-instance benchmarks, and decide whether a richer operational evaluation is worth the cost.

## Model-to-operation bridge

| Model term | Defensible operational interpretation | Required validation |
|---|---|---|
| `K0` | Incremental common cost when the closed decision set triggers a joint event: supplier order, inbound shipment, receiving window, line changeover | Finance and operations document event ownership; if other SKUs share the event, condition on a frozen background calendar and use marginal cost or exclude operational use |
| `Ki` | Item-specific ordering, handling, inspection, or setup cost | Activity-based costing separates incremental item cost from sunk overhead |
| `Hi` | Deterministic cycle-stock coefficient, often `h_i d_i / 2` under zero-inventory EOQ conventions | Demand rate and carrying-cost basis are stable enough for the planning horizon |
| `fi` | Long-run periodic replenishment frequency | Periodic scheduling is an admissible planning abstraction |
| cap `f̄i` | Maximum average frequency, or inverse minimum review/reorder interval when that semantics is exact | Constraint owner confirms it is an average/periodic cap, not a pointwise capacity surrogate |
| commensurable periods | Orders can be intentionally aligned on a common calendar | Supplier and internal calendars allow the proposed alignment |

Container capacity, pallet rounding, minimum order quantities, lead-time risk, service levels, stockout penalties, product shelf life, and peak dock capacity do **not** map automatically to independent frequency caps. They belong in the operational layer.

## Eligibility gate

A triplet enters operational analysis only if all are true:

1. **event closure:** the three items own the event economically and calendrically; or the analysis conditions on a versioned exogenous background calendar and uses explicitly marginal event cost; otherwise the triplet is software-only;
2. the data horizon and coverage pass a preregistered adequacy assessment for demand regime, seasonality, receipts, inventory, service, costs, and missingness—there is no fixed month count;
3. the planning horizon is sufficiently stationary for a fixed-interval baseline, with known regime breaks excluded or modelled;
4. decision owners can explain every cap and cost coefficient in consistent time and currency units;
5. the incumbent policy, eligibility rule, candidate-generation tolerance, and comparison metrics are frozen before results are inspected;
6. no safety, regulatory, cold-chain, contractual, pointwise-capacity, minimum-quantity, or supplier-calendar constraint is omitted from the final decision layer;
7. named owners accept the RACI and stopping authority below.

## Staged workflow

### Gate 0 — semantic fit

Document the shared event, every SKU or activity that can share it, the three-item selection rule, all excluded constraints, the decision horizon, and the intended use. Select exactly one event treatment: complete ownership; frozen background calendar plus marginal event cost; or software-only exclusion. Reject the triplet if `K0` is mostly sunk, if demand is dominated by launches or promotions, or if a long-run frequency cap is standing in for a pointwise spacing or capacity constraint.

### Gate 1 — data reconciliation

Reconcile purchase orders, receipts, inventory movements, service failures, expedites, minimum quantities, pack sizes, supplier calendars, and cost ledgers. Freeze a versioned input table and a data-quality report. Do not impute missing service failures as zero.

### Gate 2 — exact stress test

Construct the deterministic stationary model and compare:

- the standard max-frequency relaxation;
- the exact three-item oracle;
- the incumbent periodic plan;
- an **instance-specific** candidate set generated across all pair boundaries, the certified primitive-triple enumeration, and the closed tail.

The candidate set contains all verifier-checked policies within a preregistered exact relative-regret tolerance that also pass calendar feasibility. Record every included policy, the exclusion reason for screened policies, the boundary/tail margin, and the tolerance. The five policies in `analysis/policy_portfolio.json` are frozen regression fixtures for the synthetic witnesses and must not be transferred by default.

Use the v0.2 margin witness as the default software-regression and coefficient-sensitivity fixture. Use the active-envelope witness to test exact arithmetic and the strongest certified lower bound. Its much smaller inner holding-cost box is a warning against transferring the nominal winner into operations.

Trigger further evaluation only if the exact-versus-relaxation difference exceeds a preregistered materiality threshold or changes the accepted policy. Choose among near-tied calendars using the operational simulation rather than false precision in estimated deterministic coefficients. Record all eligible triplets, including null findings.

### Gate 3 — operational simulation or digital twin

Add empirical demand variation, lead-time distributions, order rounding, minimum quantities, transport brackets, service requirements, supplier calendars, and pointwise capacity. Before comparative results are inspected, register a joint uncertainty set over `K0`, every `Ki`, every `Hi`, caps, event attribution, and calendars, with empirical or expert-elicitation provenance. Report candidate rank stability, deterministic and simulated regret, feasibility, service, and worst-case outcomes. The oracle's holding-cost boxes vary only `H` and are not a substitute for this joint analysis. The exact oracle is a lower-dimensional benchmark inside this stage, not the final controller.

### Gate 4 — shadow deployment

Run the candidate policy without executing orders. The horizon must pass a design-adequacy test for warm-up, carryover, seasonality, rare service failures, and the precision needed for go/no-go decisions; no fixed cycle count is sufficient by itself. Review exceptions with planners and warehouse, procurement, finance, and service owners.

### Gate 5 — bounded field pilot

If authorised, use a preregistered randomized, switchback, cluster, stepped, or otherwise defensible concurrent comparison. The protocol must specify the assignment unit; interference graph and exposure mapping; warm-up and carryover; horizon and seasonality; precision or power for cost and service estimands; override/noncompliance handling; missingness and attrition; multiplicity; full cost boundary; safety/service stopping rules; and named stopping authority. A before/after result without a defensible counterfactual is a field association, not a causal effect.

### Gate 6 — scale and monitor

Scale only after service non-inferiority and positive net value are supported within the registered context. Monitor demand regime, supplier behaviour, cost coefficients, policy exceptions, and model drift; define automatic review and rollback conditions.

## Outcomes

Primary decision outcomes:

- approved-plan change rate;
- total landed cost and bounded regret relative to incumbent;
- inventory value and working capital;
- fill rate or other service measure;
- stockouts, backorders, lost sales, and expedites;
- container or vehicle utilisation;
- receiving workload peaks, overtime, and schedule adherence;
- human planning, integration, certification, monitoring, and switching costs.
- customer/service guardrails, carrier and supplier compliance, worker workload and safety, and environmental outcomes such as emissions or waste where material.

## Accountability and RACI

| Decision or evidence object | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| event closure and operating semantics | operations analyst | operations owner | procurement, warehouse, finance | service owner |
| incremental costs and units | finance analyst | finance owner | operations, procurement | data/engineering |
| data lineage and implementation | data/engineering | technology owner | planners, privacy/security | operations owner |
| supplier/calendar feasibility | procurement | procurement owner | supplier, warehouse | operations owner |
| service and safety constraints | service/quality | service owner | operations, legal/safety | all pilot staff |
| carrier and supplier effects | procurement/logistics | operations owner | carriers, suppliers, warehouse | finance, service owner |
| worker workload, safety, and labour impacts | operations/people lead | operations owner | affected workers or representatives, legal/safety | pilot sponsor |
| customer and service impacts | service/quality | service owner | customer-facing teams, operations | pilot sponsor |
| sustainability measures and trade-offs | sustainability analyst | sustainability owner | logistics, finance, procurement | pilot sponsor |
| privacy, contractual, labour, and regulatory compliance | legal/compliance | accountable legal owner | privacy, labour representatives, procurement, data/engineering | affected stakeholders |
| field identification and analysis | methods lead independent of implementation where feasible | pilot sponsor | operations, data, worker representatives | publisher |
| go/no-go, stop, and rollback | operations owner | pilot sponsor | finance, service, procurement, methods lead | affected stakeholders |

The Evidence Press publisher owns publication and correction routing, not an operational go-live decision.

## Minimum stop rules

Stop or roll back if any of the following occurs:

- service falls beyond the preregistered non-inferiority margin;
- stockouts, safety events, or expedites cross their limits;
- omitted constraints invalidate more than the allowed proportion of candidate events;
- planners override the candidate for unmodelled reasons above the registered threshold;
- total certification and implementation cost erases the bounded benefit;
- input drift moves the triplet outside the validated parameter region.

## Evidence states

An exact synthetic certificate supports a **model mechanism**. A shadow comparison supports implementation feasibility. A measured real setting without identification supports a **field association**. A causal impact claim requires the preregistered design, interference treatment, joint uncertainty, noncompliance/attrition handling, costs, and independent methodological review. These states must never be collapsed. Design requirements are informed by Bojinov, Simchi-Levi, and Zhao (`10.1287/mnsc.2022.4583`), Holtz et al. (`10.1287/mnsc.2020.01157`), and Ibanez and Staats (`10.1287/educ.2019.0197`); those sources do not validate any future deployment automatically.
