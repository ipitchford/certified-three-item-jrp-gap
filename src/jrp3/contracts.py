from __future__ import annotations


CERTIFICATE_SCHEMA = "jrp3.cap-oracle-certificate.v2"
PROOF_DEPENDENCY = (
    "Global optimality is conditional on the unrefereed candidate finite-closure "
    "and totality theorem bundled with this package."
)
PREDECESSOR_STATUS = (
    "The comparison endpoint comes from an unrefereed producer-side Evidence Press "
    "two-item candidate, not an externally verified exact constant."
)
VERIFICATION_INDEPENDENCE = (
    "The solver-independent verifier is same-producer and shares exact-algebra and "
    "instance-parsing substrate; its replay is not an unaffiliated rerun or independent "
    "reimplementation."
)


def certificate_conclusion(gap_expression: str) -> str:
    return (
        f"For this bundled rational instance, the candidate exact common-origin "
        f"fixed-interval gap ratio is {gap_expression}. It exceeds the comparison "
        "endpoint reported by the unrefereed producer-side two-item candidate, "
        "conditional on the stated candidate proof dependency."
    )
