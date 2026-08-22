# Evidence Press integration handoff

This directory is an authoring handoff. It contains the reserved version DOI and deterministic release routes, but it does not treat those values as evidence of public availability; the production integration must replace preparation-state assurance fields only after exact asset and canonical readback.

## Proposed public identity

- slug: `certified-three-item-jrp-gap`
- work ID: `ep-work:certified-three-item-jrp-gap`
- attempt ID: `ep-attempt:certified-three-item-jrp-gap`
- lineage: `joint-replenishment-exact-certification-programme`
- parent: `certified-two-item-jrp`
- creator: Anonymous

## Required before build integration

1. create and verify the public successor repository;
2. freeze a commit and immutable candidate tag;
3. reserve and then publish the Zenodo version DOI only after asset verification;
4. replace every null identity field in `meta.draft.json` with real URLs;
5. copy the record to `papers/certified-three-item-jrp-gap/meta.json`;
6. append the proposed work-attempt and lineage records below to the current site ledgers;
7. generate content-versioned art, narration transcript, and synthetic audio from the frozen text;
8. run catalogue, operating-model, protocol, build, publication-integrity, visual, and live readback gates;
9. preserve the two-item page and historical tag unchanged.

## Ledger patch files

- `WORK_LEDGER_RECORD.draft.json` — prospective attempt record.
- `METHOD_LINEAGE_RECORD.draft.json` — parent-child programme record.

These are proposed objects, not evidence that the ledgers or public site have been updated.
