# Candidate exact three-item JRP gap and logistics handoff

Version `0.3.1-candidate` is an anonymous, unrefereed successor to the Evidence Press release [Certified Two-Item JRP](https://evidencepress.org/releases/certified-two-item-jrp/). It combines a candidate exact three-item independent-cap oracle for common-origin fixed-interval policies with a conservative route from model insight to logistics evaluation.

Public repository: [ipitchford/certified-three-item-jrp-gap](https://github.com/ipitchford/certified-three-item-jrp-gap). The version DOI and Evidence Press release URL are inserted only after their public records pass readback.

## Headline result

For a fully specified rational three-item instance, the package certifies

```text
relaxation value = 12099233027737989052666993 / 3000320647128487500000000
fixed-interval optimum = 50387704513257323196307343 / 10877191205396850000000000
gap ratio        = 7732648297718008589674913778809 / 6731480890380196637385597557508
                 = 1.1487291464748205845...
```

The exact optimum uses primitive multipliers `(3, 3, 2)` and scale `92726/168045`. This lower bound is 3.3132% above the producer-side unrefereed two-item upper endpoint. A monotonicity lemma propagates it to every fixed item count `n >= 3`, subject to the candidate assurance boundary.

The result is a **synthetic, normalized model certificate**. The 14.8729% difference from the relaxation denominator is lower-bound optimism on this instance—not a measured saving, forecast, or service improvement.

## What is new in this successor

- exact three-regime decomposition and finite primitive-triple closure;
- global pair and triple tail certificates;
- three rational gap witnesses: a headline active-envelope point, a less-fragile margin fixture, and a simple audit case;
- an exact five-policy equalisation family, frozen only as a synthetic regression fixture, and a stationary discovery guide with an explicit claim boundary;
- fixed-item monotonicity and a relaxation-analysis barrier for every `n >= 3`;
- two globally certified holding-cost boxes built from sixteen exact vertex certificates;
- a verifier-checked portfolio builder that regenerates an instance-specific candidate set across primitive-triple and boundary regimes;
- stricter certificate verification, structural mutation tests, and exact-input parsing;
- path-independent producer replay under ordinary and optimized Python;
- a source-audited logistics interpretation and staged field-evaluation protocol;
- an Evidence Press article draft and proposed operating-model records.

## Logistics use

The oracle is useful as a **triplet stress test** for three SKUs sharing an ordering, inbound-transport, receiving, or changeover event. It can test whether a max-frequency relaxation is materially optimistic and produce exact regression fixtures for planning software. A fitted logistics instance must regenerate and verifier-check its own candidate set under a preregistered regret tolerance and operational-feasibility rules. The five policies bundled for each synthetic witness are regression fixtures and must not be transferred. The strongest mathematical witness has an extremely small certified inner holding-cost box; the older margin witness is the better robustness fixture.

It is not a dispatch engine. Minimum order quantities, container fill, lead times, stochastic demand, service constraints, pointwise dock or truck capacity, and supplier calendars require an additional operational model or simulation. See `LOGISTICS_DEPLOYMENT_PROTOCOL.md`.

## Reproduce

Python 3.10+ and SymPy 1.14.0 are required.

```bash
python3 -m pip install -e .
./scripts/reproduce.sh
```

The script rebuilds all three point certificates, the sixteen robustness-vertex certificates, two holding-box reports, active-family analysis, and exhaustive policy portfolios; verifies them with the same-producer solver-independent checker; and runs the 21-test deterministic suite. Optimized replay is supported with:

```bash
PYTHONOPTIMIZE=2 ./scripts/reproduce.sh
```

Rebuild the journal-form paper from its Markdown source with Pandoc, KaTeX, and WeasyPrint:

```bash
./scripts/build_paper.sh
python3 scripts/pdf_tex_preflight.py \
  paper/three_item_jrp_gap_and_logistics.pdf
```

## Package map

- `paper/three_item_jrp_gap_and_logistics.md` — integrated research paper.
- `docs/three_item_oracle_note.md` — detailed mathematical derivation.
- `src/jrp3/oracle.py` — discovery and certificate-producing oracle.
- `src/jrp3/verify.py` — solver-independent certificate checker.
- `analysis/active_envelope_analysis.json` — exact equalisation formulas and bounded stationary guide.
- `analysis/policy_portfolio.json` — enumeration- and tail-complete regression portfolios for both strong witnesses; regenerate for real instances.
- `certificates/` — exact witness, vertex, holding-box, and verification JSON.
- `CLAIMS.json` — machine-readable claim and evidence boundaries.
- `LOGISTICS_DEPLOYMENT_PROTOCOL.md` — real-world evaluation route and stop rules.
- `SOURCES.md` — source audit and application literature.
- `ASSURANCE.md` — assurance matrix.
- `INTAKE_AUDIT.md` — review of every supplied source-folder file.
- `reviews/` — frozen round-one reports, response matrix, and confirmation-review records.
- `site/` — Evidence Press authoring handoff and integration records.

## Claim ceiling

This package supplies producer-side exact computation and replay for the bundled instances and a journal-readable candidate theorem for finite closure and totality. The arbitrary-resource interpretation remains conditional on the unrefereed parent cap-reduction result. The PDF is not tagged for accessibility; this Markdown source is the accessible text route. The package does not establish the exact three-item constant, the unrestricted multi-item constant, independent reproduction, formal verification, external specialist or editorial peer review, operational savings, service improvement, adoption, or causal field impact.

Corrections and objections are routed through the public [repository issue tracker](https://github.com/ipitchford/certified-three-item-jrp-gap/issues) and preserved as additive successors; immutable tags and deposits are not silently replaced.
