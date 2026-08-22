from __future__ import annotations

from fractions import Fraction
import json
from math import gcd, lcm
from pathlib import Path
import random
import shutil
import tempfile
import unittest

from jrp3.algebra import exact_compare, q
from jrp3.extensions import (
    ACTIVE_RUNNERS,
    WINNER,
    active_envelope_holdings,
    active_runner_cost,
    active_runner_radius,
    crossover_polynomial,
    verify_holding_box_certificate,
)
from jrp3.model import as_fraction, load_instance
from jrp3.portfolio import DOCUMENT_SCHEMA, verify_policy_portfolio_document
from jrp3.oracle import (
    pair_complexity,
    primitive_triples,
    relaxation_optimum,
    second_pair_complexity,
    solve_exact_cap_oracle,
    triple_policy,
    union_coefficient,
)
from jrp3.verify import verify_certificate


ROOT = Path(__file__).resolve().parents[1]
INSTANCE_PATH = ROOT / "data" / "three_item_gap_witness.json"
CERTIFICATE_PATH = ROOT / "certificates" / "three_item_gap_witness.certificate.json"
STRONG_INSTANCE_PATH = ROOT / "data" / "near_extremal_three_item_gap_witness.json"
STRONG_CERTIFICATE_PATH = ROOT / "certificates" / "near_extremal_three_item_gap_witness.certificate.json"
ACTIVE_INSTANCE_PATH = ROOT / "data" / "active_envelope_three_item_gap_witness.json"
ACTIVE_CERTIFICATE_PATH = ROOT / "certificates" / "active_envelope_three_item_gap_witness.certificate.json"


class OracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = load_instance(INSTANCE_PATH)

    def test_symmetric_nested_instance(self) -> None:
        from jrp3.model import CapInstance, CapItem

        symmetric = CapInstance(
            "symmetric-nested",
            Fraction(1),
            tuple(
                CapItem(f"item-{index + 1}", Fraction(0), Fraction(1), Fraction(1))
                for index in range(3)
            ),
        )
        result = solve_exact_cap_oracle(symmetric)
        self.assertTrue(result.certified)
        self.assertEqual(result.best_cost.value, Fraction(4))
        self.assertEqual(result.gap, q(Fraction(1)))
        self.assertEqual([policy.multipliers for policy in result.policies], [(1, 1, 1)])

    def test_witness_exact_values(self) -> None:
        result = solve_exact_cap_oracle(self.instance)
        self.assertTrue(result.certified)
        self.assertEqual(result.cutoff, 21)
        self.assertEqual(result.enumerated_triples, 49_981)
        self.assertEqual(result.best_cost.kind, "rational")
        self.assertEqual(result.best_cost.value, Fraction(4793, 1035))
        self.assertEqual([policy.multipliers for policy in result.policies], [(3, 2, 2)])
        self.assertEqual(result.gap, q(Fraction(9586, 8355)))

    def test_relaxation_corner(self) -> None:
        relaxation = relaxation_optimum(self.instance)
        self.assertEqual(relaxation.cost, q(Fraction(557, 138)))
        self.assertEqual(relaxation.frequencies, (q(Fraction(3, 5)), q(Fraction(23, 30)), q(1)))

    def test_union_coefficient(self) -> None:
        self.assertEqual(union_coefficient((3, 2, 2)), Fraction(2, 3))
        self.assertEqual(union_coefficient((1, 1, 1)), Fraction(1, 1))
        self.assertEqual(union_coefficient((2, 3, 5)), Fraction(11, 15))

    def test_generator_matches_bruteforce_small_cutoffs(self) -> None:
        for S in range(2, 7):
            bound = (S - 1) ** 2
            brute: set[tuple[int, int, int]] = set()
            for a1 in range(1, bound + 1):
                for a2 in range(1, bound + 1):
                    for a3 in range(1, bound + 1):
                        if gcd(gcd(a1, a2), a3) != 1:
                            continue
                        a = (a1, a2, a3)
                        if second_pair_complexity(a) <= S:
                            brute.add(a)
            self.assertEqual(set(primitive_triples(S)), brute)

    def test_second_complexity_tail_inequality(self) -> None:
        # Exhaustive arithmetic regression over bounded primitive triples. The
        # inequality is homogeneous, so scale x=1 is sufficient.
        S = 7
        r = Fraction(S - 1, S + 1)
        for a1 in range(1, 26):
            for a2 in range(1, 26):
                for a3 in range(1, 26):
                    if gcd(gcd(a1, a2), a3) != 1:
                        continue
                    a = (a1, a2, a3)
                    if second_pair_complexity(a) <= S:
                        continue
                    frequencies = [Fraction(1, x) for x in a]
                    pairs = [(0, 1), (0, 2), (1, 2)]
                    edge = min(pairs, key=lambda ij: pair_complexity(a, *ij))
                    i, j = edge
                    intersection = Fraction(1, lcm(a[i], a[j]))
                    pair_only_union = sum(frequencies, Fraction()) - intersection
                    full_union = union_coefficient(a)
                    self.assertGreaterEqual(full_union, r * pair_only_union)

    def test_fixed_triple_details(self) -> None:
        policy = triple_policy(self.instance, (3, 2, 2))
        self.assertEqual(policy.A, Fraction(2, 3))
        self.assertEqual(policy.B, Fraction(83, 15))
        self.assertEqual(policy.t_min, Fraction(15, 23))
        self.assertEqual(policy.cost.value, Fraction(4793, 1035))

    def test_solver_independent_producer_verifier(self) -> None:
        report = verify_certificate(CERTIFICATE_PATH, instance_path=INSTANCE_PATH)
        self.assertTrue(report["passed"])
        self.assertEqual(report["recomputed_gap"], "9586/8355")

    def test_stronger_witness_and_verifier(self) -> None:
        strong = load_instance(STRONG_INSTANCE_PATH)
        result = solve_exact_cap_oracle(strong)
        self.assertTrue(result.certified)
        self.assertEqual(result.cutoff, 21)
        self.assertEqual(result.best_cost.value, Fraction(23440435983871, 5059579140000))
        self.assertEqual([policy.multipliers for policy in result.policies], [(3, 3, 2)])
        self.assertEqual(
            result.gap,
            q(Fraction(1798701855222341185000, 1565819440747964323563)),
        )
        report = verify_certificate(STRONG_CERTIFICATE_PATH, instance_path=STRONG_INSTANCE_PATH)
        self.assertTrue(report["passed"])

    def test_active_envelope_witness_and_equalisation(self) -> None:
        active = load_instance(ACTIVE_INSTANCE_PATH)
        x, y = active.items[0].cap, active.items[1].cap
        self.assertEqual(tuple(item.H for item in active.items), active_envelope_holdings(y))
        runner_cost = active_runner_cost(y)
        self.assertGreater(crossover_polynomial(x, y), 0)
        for multipliers in ACTIVE_RUNNERS:
            self.assertEqual(triple_policy(active, multipliers).cost.value, runner_cost)
        result = solve_exact_cap_oracle(active)
        self.assertTrue(result.certified)
        self.assertEqual(result.cutoff, 21)
        self.assertEqual([policy.multipliers for policy in result.policies], [WINNER])
        self.assertEqual(
            result.gap,
            q(Fraction(7732648297718008589674913778809, 6731480890380196637385597557508)),
        )
        report = verify_certificate(ACTIVE_CERTIFICATE_PATH, instance_path=ACTIVE_INSTANCE_PATH)
        self.assertTrue(report["passed"])

    def test_holding_box_radii(self) -> None:
        prior = load_instance(STRONG_INSTANCE_PATH)
        active = load_instance(ACTIVE_INSTANCE_PATH)
        prior_rho, _ = active_runner_radius(prior)
        active_rho, _ = active_runner_radius(active)
        self.assertEqual(prior_rho, Fraction(86013857588, 70692800851712719))
        self.assertEqual(
            active_rho,
            Fraction(292901133283274471191, 3039290287366368373970172442382),
        )
        self.assertGreater(prior_rho, active_rho)

    def test_holding_box_certificates(self) -> None:
        for stem in (
            "near_extremal_three_item_gap_witness",
            "active_envelope_three_item_gap_witness",
        ):
            report = verify_holding_box_certificate(
                ROOT / "certificates" / f"{stem}.holding_box.certificate.json"
            )
            self.assertTrue(report["passed"])
            self.assertEqual(report["vertex_count"], 8)

    def test_registered_portfolios_are_enumeration_and_tail_complete(self) -> None:
        portfolio_path = ROOT / "analysis" / "policy_portfolio.json"
        report = verify_policy_portfolio_document(portfolio_path, package_root=ROOT)
        self.assertTrue(report["passed"])
        payload = json.loads(portfolio_path.read_text())
        self.assertEqual(payload["schema"], DOCUMENT_SCHEMA)
        for portfolio in payload["portfolios"]:
            with self.subTest(label=portfolio["label"]):
                instance = load_instance(ROOT / portfolio["instance"])
                result = solve_exact_cap_oracle(instance)
                tolerance = Fraction(portfolio["registered_relative_cost_tolerance"])
                expected = set()
                for multipliers in primitive_triples(result.cutoff):
                    policy = triple_policy(instance, multipliers)
                    relative_regret = policy.cost.expression / result.best_cost.expression - 1
                    if exact_compare(relative_regret, q(tolerance)) <= 0:
                        expected.add(multipliers)
                declared = {
                    tuple(entry["primitive_multipliers"])
                    for entry in portfolio["primitive_triple_policies"]
                }
                self.assertEqual(declared, expected)
                threshold = result.best_cost.expression * (1 + q(tolerance))
                self.assertGreater(exact_compare(result.tail_lower_bound, threshold), 0)
                completeness = portfolio["completeness_certificate"]
                self.assertEqual(completeness["enumerated_primitive_triples"], len(expected) + completeness["excluded_primitive_triple_count"])
                self.assertEqual(len(completeness["boundary_comparators"]), 4)
                self.assertEqual(completeness["included_boundary_policy_count"], 0)
                self.assertEqual(completeness["excluded_boundary_policy_count"], 4)
                self.assertTrue(
                    completeness[
                        "tail_excludes_all_omitted_primitive_policies_within_tolerance"
                    ]
                )
                self.assertTrue(completeness["all_boundary_regimes_classified"])

    def test_policy_portfolio_verifier_rejects_load_bearing_mutations(self) -> None:
        source = json.loads((ROOT / "analysis" / "policy_portfolio.json").read_text())
        mutations: list[tuple[str, dict]] = []

        boundary_cost = json.loads(json.dumps(source))
        boundary_cost["portfolios"][0]["completeness_certificate"]["boundary_comparators"][0]["cost"]["expression"] = "1"
        mutations.append(("boundary-cost", boundary_cost))

        excluded_count = json.loads(json.dumps(source))
        excluded_count["portfolios"][0]["completeness_certificate"]["excluded_primitive_triple_count"] -= 1
        mutations.append(("excluded-count", excluded_count))

        policy_frequency = json.loads(json.dumps(source))
        policy_frequency["portfolios"][0]["primitive_triple_policies"][0]["frequencies"][0] = "1"
        mutations.append(("policy-frequency", policy_frequency))

        purpose = json.loads(json.dumps(source))
        purpose["purpose"] = "operational handoff"
        mutations.append(("purpose", purpose))

        with tempfile.TemporaryDirectory() as directory:
            for label, mutated in mutations:
                with self.subTest(label=label):
                    path = Path(directory) / f"{label}.json"
                    path.write_text(json.dumps(mutated), encoding="utf-8")
                    with self.assertRaises((AssertionError, TypeError, ValueError)):
                        verify_policy_portfolio_document(path, package_root=ROOT)

    def test_mutation_control(self) -> None:
        certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        certificate["true_optimum"]["value"] = "4794/1035"
        certificate["true_optimum"]["expression"] = "4794/1035"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mutated.json"
            path.write_text(json.dumps(certificate), encoding="utf-8")
            with self.assertRaises((AssertionError, TypeError, ValueError)):
                verify_certificate(path)

    def test_structural_mutations_are_rejected(self) -> None:
        certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        mutations = []

        duplicate_pair = json.loads(json.dumps(certificate))
        duplicate_pair["one_pair_oracles"][2]["pair_indices"] = [0, 1]
        mutations.append(duplicate_pair)

        false_tail = json.loads(json.dumps(certificate))
        false_tail["tail_factor_squared"] = "1"
        mutations.append(false_tail)

        false_certified = json.loads(json.dumps(certificate))
        false_certified["candidate_global_optimum_under_stated_proof"] = False
        mutations.append(false_certified)

        with tempfile.TemporaryDirectory() as directory:
            for index, mutated in enumerate(mutations):
                path = Path(directory) / f"mutated-{index}.json"
                path.write_text(json.dumps(mutated), encoding="utf-8")
                with self.assertRaises((AssertionError, TypeError, ValueError)):
                    verify_certificate(path)

    def test_strict_certificate_schema_rejects_reviewed_shapes(self) -> None:
        certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        mutations: list[tuple[str, dict]] = []

        empty_frequencies = json.loads(json.dumps(certificate))
        empty_frequencies["relaxation"]["frequencies"] = []
        mutations.append(("empty-frequencies", empty_frequencies))

        omitted_pair_record = json.loads(json.dumps(certificate))
        omitted_pair_record["one_pair_oracles"].pop()
        mutations.append(("omitted-pair-record", omitted_pair_record))

        duplicate_policy = json.loads(json.dumps(certificate))
        duplicate_policy["optimal_triple_policies"].append(
            json.loads(json.dumps(duplicate_policy["optimal_triple_policies"][0]))
        )
        mutations.append(("duplicate-policy", duplicate_policy))

        malformed_radical = json.loads(json.dumps(certificate))
        malformed_radical["tail_lower_bound"].pop("rational", None)
        malformed_radical["tail_lower_bound"]["expression"] = "sqrt(2"
        mutations.append(("malformed-radical", malformed_radical))

        unknown_field = json.loads(json.dumps(certificate))
        unknown_field["relaxation"]["unchecked_hint"] = "accept"
        mutations.append(("unknown-field", unknown_field))

        wrong_scalar_type = json.loads(json.dumps(certificate))
        wrong_scalar_type["one_pair_oracles"][0]["cutoff_R"] = "5"
        mutations.append(("wrong-scalar-type", wrong_scalar_type))

        contradictory_optimum = json.loads(json.dumps(certificate))
        contradictory_optimum["true_optimum"]["expression"] = "1"
        mutations.append(("contradictory-optimum-expression", contradictory_optimum))

        contradictory_gap = json.loads(json.dumps(certificate))
        contradictory_gap["integrality_gap"]["expression"] = "1"
        mutations.append(("contradictory-gap-expression", contradictory_gap))

        contradictory_decimal = json.loads(json.dumps(certificate))
        contradictory_decimal["integrality_gap"]["decimal"] = "99"
        mutations.append(("contradictory-gap-decimal", contradictory_decimal))

        wrong_assurance = json.loads(json.dumps(certificate))
        wrong_assurance["verification_independence"] = "independently verified"
        mutations.append(("wrong-assurance-label", wrong_assurance))

        exponentiation = json.loads(json.dumps(certificate))
        exponentiation["relaxation"]["frequencies"][0] = "2**8"
        mutations.append(("exponentiation", exponentiation))

        oversized_integer = json.loads(json.dumps(certificate))
        oversized_integer["relaxation"]["frequencies"][0] = "1" * 513
        mutations.append(("oversized-integer", oversized_integer))

        with tempfile.TemporaryDirectory() as directory:
            for label, mutated in mutations:
                with self.subTest(label=label):
                    path = Path(directory) / f"{label}.json"
                    path.write_text(json.dumps(mutated), encoding="utf-8")
                    with self.assertRaises((TypeError, ValueError)):
                        verify_certificate(path)

    def test_seeded_schema_fuzz_rejects_unknown_and_missing_fields(self) -> None:
        certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        rng = random.Random(20260822)
        required_top_level = [
            "instance", "relaxation", "desynchronised_regime", "one_pair_oracles",
            "boundary_cost", "triple_cutoff_S", "optimal_triple_policies",
            "true_optimum", "integrality_gap",
        ]
        mutations: list[dict] = []
        for index in range(24):
            mutated = json.loads(json.dumps(certificate))
            if index % 2:
                del mutated[rng.choice(required_top_level)]
            else:
                mutated[f"unknown_fuzz_field_{index}"] = index
            mutations.append(mutated)
        with tempfile.TemporaryDirectory() as directory:
            for index, mutated in enumerate(mutations):
                path = Path(directory) / f"fuzz-{index}.json"
                path.write_text(json.dumps(mutated), encoding="utf-8")
                with self.assertRaises((TypeError, ValueError)):
                    verify_certificate(path)

    def test_verification_reports_are_extraction_path_independent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            reports = []
            for extraction in ("first", "second"):
                root = Path(directory) / extraction
                (root / "certificates").mkdir(parents=True)
                (root / "data").mkdir()
                (root / "pyproject.toml").write_text("[project]\nname='fixture'\nversion='0'\n")
                certificate_path = root / "certificates" / CERTIFICATE_PATH.name
                instance_path = root / "data" / INSTANCE_PATH.name
                shutil.copyfile(CERTIFICATE_PATH, certificate_path)
                shutil.copyfile(INSTANCE_PATH, instance_path)
                reports.append(verify_certificate(certificate_path, instance_path=instance_path))
            self.assertEqual(reports[0], reports[1])
            self.assertEqual(
                reports[0]["certificate"],
                "certificates/three_item_gap_witness.certificate.json",
            )

    def test_holding_box_verifier_rejects_package_escape(self) -> None:
        source_path = ROOT / "certificates" / "active_envelope_three_item_gap_witness.holding_box.certificate.json"
        payload = json.loads(source_path.read_text(encoding="utf-8"))
        payload["vertices"][0]["instance"] = "../outside.json"
        with tempfile.TemporaryDirectory() as directory:
            path = ROOT / "certificates" / "holding-box-path-escape.mutation.json"
            try:
                path.write_text(json.dumps(payload), encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify_holding_box_certificate(path)
            finally:
                path.unlink(missing_ok=True)

    def test_json_float_inputs_are_rejected(self) -> None:
        with self.assertRaises(TypeError):
            as_fraction(0.1)


if __name__ == "__main__":
    unittest.main()
