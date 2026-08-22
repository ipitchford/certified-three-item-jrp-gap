# Agent index

## Identity

- Title: *A Candidate Exact Three-Item Independent-Cap Oracle: A Certified Rational Relaxation-Gap Lower Bound and Logistics Handoff*
- Version: `0.3.1-candidate`
- Version DOI: `10.5281/zenodo.22057665` (reserved before sealing; verify public status separately)
- Repository: `https://github.com/ipitchford/certified-three-item-jrp-gap`
- Evidence Press route: `https://evidencepress.org/releases/certified-three-item-jrp-gap/`
- Creator: Anonymous
- Status: unrefereed PASS_WITH_NOTES identity-bearing candidate; DOI reserved and repository public, but release/deposit/page readback not yet complete at sealing
- Parent: `https://evidencepress.org/releases/certified-two-item-jrp/`

## Fast verification route

1. Read `STATUS.md` and `CLAIMS.json`.
2. Inspect `data/active_envelope_three_item_gap_witness.json` and retain `data/near_extremal_three_item_gap_witness.json` as the margin fixture.
3. Inspect `analysis/active_envelope_analysis.json` and `analysis/policy_portfolio.json`.
4. Run `./scripts/reproduce.sh`.
5. Compare witness, vertex, and holding-box verification JSON with `ASSURANCE.md`.
6. Read `docs/three_item_oracle_note.md` for the generator, tail, monotonicity, active-envelope, and vertex arguments.
7. Read `LOGISTICS_DEPLOYMENT_PROTOCOL.md` before making any applied claim.

## Claim boundary

The exact finite outputs are producer-side evidence within a stationary periodic three-item model. They are not independent verification, the exact global constant, a real-company saving, or permission to execute replenishment decisions.
