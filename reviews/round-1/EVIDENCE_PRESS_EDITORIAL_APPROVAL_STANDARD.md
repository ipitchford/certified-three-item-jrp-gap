# Evidence Press journal-like editorial approval standard

Status: proposed mandatory release gate  
Applies to: new and materially revised Evidence Press research releases  
Effective date: 22 August 2026

## Purpose

Before an Evidence Press research candidate receives a scientific release decision, it must undergo a journal-like internal review conducted against a frozen submission. The process is designed to find errors, force disciplinary disagreement into the record, and produce an actionable editorial decision. It supplements deterministic integrity and replay gates; it does not replace them.

Model-mediated or producer-coordinated reports must be described as **internal editorial review**. They do not establish unaffiliated specialist review, external peer review, independent reproduction, formal verification, novelty, or correctness.

## Required roles

Each substantive round must include five mutually differentiated reports:

1. **Editor-in-Chief reviewer** — journal fit, significance, claim calibration, and overall release suitability.
2. **Methodology specialist** — design, mathematical/statistical validity, computation, certificate semantics, and reproducibility.
3. **Domain specialist** — disciplinary theory, terminology, literature, novelty and priority boundaries.
4. **Applications or cross-disciplinary specialist** — semantic bridge, practical implications, omitted constraints, and potential misuse.
5. **Devil's Advocate** — strongest counter-argument, hidden assumptions, cherry-picking, alternative explanations, and stakeholder blind spots.

The editor who synthesizes the decision must have all five signed or hashed reports. The synthesizer may arbitrate findings but may not invent criticisms absent from those reports.

## Independence inside the round

- Reviewers receive the same frozen manuscript and declared supplementary package.
- Each reviewer declares role, scope, confidence, and any conflict or limitation.
- Reviewers work independently and must not read or cite other reviewer reports before submitting their own.
- Reviewers do not edit the manuscript. Reports are separate, immutable review objects.
- Overlapping findings are retained when they arise independently, but each report must analyse them from its assigned perspective.

This role separation is an adversarial-diversity control, not evidence of institutional or unaffiliated independence.

## Frozen-target record

The review record must bind:

- manuscript title, version, date, and SHA-256;
- archive name, SHA-256, and manifest result;
- source and PDF paths;
- review round and reviewer-role configuration;
- every report path and SHA-256;
- editorial decision and required-revision identifiers;
- assurance label and unresolved external-review dimensions.

No report may be reused for changed scientific bytes. Formatting-only changes may retain the substantive decision when the editor records why no claim, evidence, conclusion, licence, authorship, or assurance status changed.

## Report requirements

Every standard reviewer report must contain:

- recommendation: Accept, Minor Revision, Major Revision, or Reject;
- confidence from 1 to 5;
- concise overall assessment;
- at least three specific strengths;
- at least three specific weaknesses with location, reason, severity, and remedy;
- section-level comments and answerable author questions;
- dimension scores with an explicit weighted result.

The Devil's Advocate uses the same evidentiary discipline but leads with the strongest counter-argument and classifies issues as Critical, Major, or Minor.

## Editorial decision mapping

| Journal-like decision | Evidence Press scientific gate | Required action |
|---|---|---|
| Accept | `PASS` or `PASS_WITH_NOTES` | Deterministic integrity gates must also pass; retain assurance limits |
| Minor Revision | `HOLD_FOR_REPAIR` until changes are checked, then normally `PASS_WITH_NOTES` | Point-by-point response and editor verification |
| Major Revision | `HOLD_FOR_REPAIR` | Material revision plus one confirmation review against the response matrix |
| Reject | `REJECTED` | Preserve the candidate and negative decision; do not present it as a successful release |

Additional rules:

- Any unresolved Critical Devil's Advocate finding forbids Accept.
- A fatal proof, data, semantic, source, licence, or authorship defect forbids publication regardless of average score.
- Publication identity, DOI, deployment, hashes, and replay cannot override a scientific `HOLD_FOR_REPAIR` or `REJECTED` decision.
- An editorial pass cannot upgrade unassessed external assurance dimensions.

## Revision and confirmation review

When revision is required, the authoring workflow supplies a response matrix containing:

`review item -> author response -> changed file/location -> verification evidence -> resolved?`

Material scientific repair permits one bounded confirmation review. It checks every required item, records residual or newly introduced P0/P1 issues, and issues a new decision. A third model-review round requires a written information-gain proposition identifying a failure mode that reports and deterministic controls have not already adjudicated.

## Evidence Press approval checklist

Release approval requires all applicable rows to pass:

- [ ] frozen submission and manifest recorded;
- [ ] five differentiated reports complete;
- [ ] conflicts, role limits, and confidence disclosed;
- [ ] editorial synthesis traces every required revision to a report;
- [ ] response matrix complete when revisions occurred;
- [ ] confirmation review passed when scientific bytes changed;
- [ ] unresolved objections and disagreements retained;
- [ ] normal, optimized, clean-extraction, citation, licence, PDF, and semantic negative-control gates passed as applicable;
- [ ] public status distinguishes internal editorial review from external specialist or peer review;
- [ ] final Evidence Press decision is `PASS`, `PASS_WITH_NOTES`, `HOLD_FOR_REPAIR`, or `REJECTED`.

## Public wording

Safe wording when the process is model-mediated:

> The candidate passed a structured internal editorial review using differentiated editor, methodology, domain, applications, and adversarial roles. The reports and decision record are included. This process is not unaffiliated specialist review, external journal peer review, independent reproduction, or formal verification.

Use “externally peer reviewed” or “independently reviewed” only when a real external venue or unaffiliated reviewer record supports that status.
