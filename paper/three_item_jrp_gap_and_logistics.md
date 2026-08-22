---
title: "A Candidate Exact Three-Item Independent-Cap Oracle: A Certified Rational Relaxation-Gap Lower Bound and Logistics Handoff"
author: "Anonymous"
date: "22 August 2026"
status: "Unrefereed candidate; producer-side exact replay"
---

# Abstract

We construct a candidate exact oracle for common-origin fixed-interval policies in the continuous-time three-item joint replenishment problem under rational item-specific frequency caps. The oracle partitions real period vectors by commensurability, solves all boundary closures exactly, enumerates fully commensurable primitive triples using a second-smallest pair-complexity cutoff, and closes the infinite complement with a quantified global tail theorem. A totality proposition proves that the stopping inequality is eventually reached; the proof and every dependency are included below. A bundled rational instance has relaxed value

\[
L=\frac{12099233027737989052666993}{3000320647128487500000000}
\]

and exact common-origin fixed-interval optimum

\[
C^*=\frac{50387704513257323196307343}{10877191205396850000000000}
\]

at primitive multipliers \((3,3,2)\) and scale \(92726/168045\). Consequently,

\[
\Gamma_{3,\square}\ge
\frac{C^*}{L}
=\frac{7732648297718008589674913778809}{6731480890380196637385597557508}
=1.1487291464748205845\ldots.
\]

This is 3.3132% above the producer-certified, unrefereed upper endpoint reported by the two-item predecessor. A monotonicity lemma propagates the independent-cap lower bound to every fixed item count \(n\ge3\), and the witness is a barrier to universal rounding analyses measured only against this relaxation. The broader resource-constrained interpretation is conditional on the predecessor's unrefereed cap-reduction argument. An exact five-policy equalisation family explains the witness; eight-vertex oracle certificates prove two explicit certified inner boxes under simultaneous relative holding-cost perturbation. We also define a conservative logistics handoff: the oracle is proposed as a three-SKU stress test and software benchmark, followed by semantic validation, simulation, shadow operation, and a design-adequate field comparison. No operational saving, independent reproduction, formal verification, external specialist review, or journal peer review is claimed.

# 1. Why the third item matters

Joint replenishment couples otherwise familiar inventory cycles through a common setup or ordering event. The standard convex relaxation replaces the exact density of the union of replenishment epochs by the largest individual frequency. For two items, the producer-side unrefereed parent Evidence Press candidate reported a narrow interval around

\[
\gamma=1.111889\ldots
\]

for the worst exact-to-relaxed gap under independent caps. The natural next question was whether that value survived when a third stream could align with either of two others.

It does not. The third stream creates a qualitatively new coordination geometry: all three periods may be commensurable, exactly one pair may be commensurable, or all may be pairwise incommensurable. The strongest witness exploits a \((3,3,2)\) calendar. The exact policy deliberately slows one capped stream until it aligns with another; the max-frequency relaxation prices the shared event too optimistically because it does not account for the arithmetic structure needed to realize those frequencies simultaneously.

This is a model result. In a normalized synthetic instance, the relaxation denominator is 14.8729146475% below the exact cost, or 12.9472771655% when expressed as a proportion of the exact optimum. Neither number is a realized saving. They measure the optimism of one lower bound under one exact stationary model.

| Quantity | Exact definition | Value | Interpretation |
|---|---|---:|---|
| exact/relaxed ratio | \(C^*/L\) | \(1.1487291464748206\ldots\) | certified bundled-instance ratio |
| relaxation-denominator gap | \((C^*-L)/L\) | 14.8729% | optimism of this lower bound, not savings |
| exact-denominator gap | \((C^*-L)/C^*\) | 12.9473% | same difference under another denominator, not regret |
| preprint-upper separation | \((U-C^*)/C^*\), \(U=5/(6\ln2)\) | 4.6588% | descriptive cross-source comparator |

## 1.1 Related work and claim dependencies

Roundy's power-of-two rounding, Teo and Bertsimas's randomized rounding, and later approximation work establish the classical rounding context, but they do not provide this three-item finite oracle. Cohen-Hillel and Yedidsion establish strong NP-hardness for the periodic JRP. Segev's peer-reviewed continuous-time work improves unconstrained approximation theory; a separate 2026 resource-constrained preprint reports the \(5/(6\ln2)\) comparator used here. Creemers and Boute provide exact evaluation for a stochastic can-order policy class. Creemers and Stephan's 2026 SSRN preprint exactly characterises can-order policies after removing one of holding, major-order, or minor-order cost. Both are adjacent but study different policy/state objects from this deterministic common-origin fixed-interval independent-cap gap oracle. Peng, Wang, and Wang survey stochastic, dynamic, resource-constrained, and joint-delivery extensions. The source search protocol and exact metadata receipts are archived in `SOURCES.md` and `CITATION_AUDIT.md`.

| Work | Model and policy class | Constraint/cost class | Exact or approximate | Relation to this candidate |
|---|---|---|---|---|
| Agent collective and Pitchford (2026), parent candidate | two-item deterministic common-origin fixed intervals | independent caps; conditional arbitrary-resource reduction | producer-side candidate interval and endpoint | imported comparison and model lineage; not independent confirmation |
| Schulz and Telha (2024) | two-item deterministic JRP | classical setup/holding structure | hardness/arithmetic complexity | explains why exact low-item analysis is nontrivial |
| Roundy (1989); Teo and Bertsimas (2001) | capacitated lot-sizing/JRP rounding | resource-feasible rounding classes | approximation | classical relaxation and rounding lineage |
| Cohen-Hillel and Yedidsion (2018) | periodic JRP | classical deterministic JRP | strong NP-hardness | complexity context, not the present fixed-item oracle |
| Segev (2025/2026) | continuous-time JRP | unconstrained approximation | approximation guarantees | peer-reviewed context; no present exact certificate |
| Segev (2026 arXiv v1) | resource-constrained continuous-time JRP | power-grid policy class | algorithmic upper guarantee | source of \(5/(6\ln2)\), not a gap-certificate input |
| Creemers and Boute (2022) | stochastic demand, stationary/generalised can-order policies | major/minor orders, holding, backlog/lost-sales extensions | exact policy evaluation within its stochastic model | distinct state and policy object |
| Creemers and Stephan (2026 SSRN) | can-order policies over finite/infinite horizons | special cases with one cost component removed | exact special-case characterisation | adjacent zero-cost structure, but no independent-cap triple tail or present witness |
| This candidate | three-item deterministic common-origin fixed intervals | rational independent frequency caps | candidate exact oracle plus finite replay | triple generator/tail, rational lower-bound witness, and bounded logistics protocol |

| Object used in this paper | Source and status | Dependency |
|---|---|---|
| three-item finite generator, tails, totality, rational witness | this unrefereed candidate | direct proof plus producer replay |
| two-item cap endpoint and arbitrary-resource cap reduction | Agent collective and Pitchford predecessor, unrefereed Evidence Press candidate | conditional comparison/extension only |
| \(5/(6\ln2)\) resource-constrained upper comparator | Segev, arXiv:2603.18720v1 | external preprint; not part of certificate |
| continuous-time approximation context | Segev, *Mathematics of Operations Research* and *Management Science* | peer-reviewed context |
| periodic JRP hardness | Cohen-Hillel and Yedidsion, *Mathematics of Operations Research* | peer-reviewed context |
| applied logistics and field-design requirements | cited case, stochastic/dynamic, and experimental-design literature | protocol motivation; no validation of this oracle |

# 2. Model, policy class, and dependency boundary

## 2.1 Feasible rational instances and real policies

A three-item independent-cap instance is

\[
I=(K_0,(K_i,H_i,\bar f_i)_{i=1}^3),
\]

where every displayed coefficient is rational, \(K_0>0\), \(K_i\ge0\), \(H_i>0\), and \(\bar f_i>0\). Zero item-specific setup costs are allowed. A feasible **common-origin fixed-interval policy** is a real period vector \(T\in\mathbb R_{>0}^3\) with frequencies \(f_i=1/T_i\le\bar f_i\); item \(i\) acts at epochs \(T_i\mathbb Z_{>0}\). The word “periodic” below always means fixed-interval item policies, not that an incommensurable union has a finite common period.

For a locally finite event set \(A\subset(0,\infty)\), define

\[
\operatorname{dens}(A)=\lim_{x\to\infty}\frac{\#(A\cap(0,x])}{x}
\]

when the limit exists. For a finite union of arithmetic progressions used here it exists: a single stream has density \(1/T_i\); two streams have intersection density zero when their period ratio is irrational, and otherwise form a common lattice. Inclusion–exclusion therefore gives the union density exactly.

The long-run objective is

\[
F_I(T)=K_0\,\operatorname{dens}\!\left(\bigcup_{i=1}^3T_i\mathbb Z_{>0}\right)
+\sum_{i=1}^3\left(\frac{K_i}{T_i}+H_iT_i\right).
\]

Let \(C^*(I)=\inf_T F_I(T)\) over feasible common-origin fixed-interval policies. The relaxation value is the attained minimum

\[
L(I)=\min_{0<f_i\le\bar f_i}
\left[K_0\max_i f_i+\sum_i\left(K_if_i+\frac{H_i}{f_i}\right)\right].
\]

For \(n\ge1\), define \(\Gamma_{n,\square}=\sup_I C^*(I)/L(I)\) over rational \(n\)-item independent-cap instances with the same sign conditions. The three-item theorem below proves that \(C^*(I)\) is attained by a fully commensurable policy and that the oracle terminates for every such three-item input.

## 2.2 Imported and independent claims

The executable theorem in this paper is restricted to independent caps. Its three-item finite generation, boundary tails, global tail, witness, and fixed-\(n\) monotonicity do not use the predecessor's proof. The interpretation for arbitrary nonnegative linear resource rows is conditional on the parent Evidence Press candidate's cap-reduction argument, and the two-item comparison is conditional on its producer-certified, unrefereed endpoint. The resource-constrained upper comparator \(5/(6\ln2)\) is reported in Segev's arXiv v1 preprint; it is not used to certify the lower bound.

# 3. Finite closure and totality theorem

## 3.1 Exhaustive commensurability partition

Define \(i\sim j\) exactly when \(T_i/T_j\in\mathbb Q\). This is an equivalence relation, so three items have precisely three partition types: one class of size three; one class of size two and a singleton; or three singletons. The boundary calculations below use closures because a minimizer of a nominal one-pair or desynchronised expression can accidentally acquire extra rational relations. Such an accident only lowers the true union cost and is handled by the fully commensurable comparison.

## 3.2 Fixed primitive triples

In the fully commensurable regime write \(T_i=a_it\), where \(\mathbf a\in\mathbb Z_{>0}^3\) is primitive. Inclusion–exclusion gives

\[
u(\mathbf a)=\sum_i\frac1{a_i}
-\sum_{i<j}\frac1{\operatorname{lcm}(a_i,a_j)}
+\frac1{\operatorname{lcm}(a_1,a_2,a_3)}.
\]

With

\[
A_{\mathbf a}=K_0u(\mathbf a)+\sum_i\frac{K_i}{a_i},\qquad
B_{\mathbf a}=\sum_iH_ia_i,
\]

the pattern cost is \(A_{\mathbf a}/t+B_{\mathbf a}t\), subject to

\[
t\ge t_{\min}(\mathbf a)=\max_i\frac1{a_i\bar f_i}.
\]

It is attained at \(t^*_{\mathbf a}=\max\{\sqrt{A_{\mathbf a}/B_{\mathbf a}},t_{\min}(\mathbf a)\}\). Thus every fixed-pattern comparison is rational or a comparison of quadratic radicals.

## 3.3 Pair and desynchronised boundaries

The three-singleton boundary is

\[
M_0=\sum_i\min_{0<f_i\le\bar f_i}
\left[(K_0+K_i)f_i+\frac{H_i}{f_i}\right].
\]

For a one-pair pattern \((i,j)\), write \(T_i=qt\), \(T_j=pt\), \(\gcd(p,q)=1\), and let \(k\) be the singleton. In variables \(x=1/t\) and \(y=1/T_k\), its closure cost is the minimum of

\[
\left[K_0\frac{p+q-1}{pq}+\frac{K_i}{q}+\frac{K_j}{p}\right]x
+\frac{H_iq+H_jp}{x}
+(K_0+K_k)y+\frac{H_k}{y},
\]

with \(x\le\min(q\bar f_i,p\bar f_j)\) and \(y\le\bar f_k\). The variables separate and each term has an exact capped EOQ minimum.

**Proposition 1 (pair tail and finite pair closure).** If a reduced pair has \(p+q\ge R+1\), then its closure cost is at least \(\sqrt{R/(R+1)}M_0\). Moreover, for each item pair a finite \(R\) makes the best enumerated pair no larger than this tail.

*Proof.* Its intersection density is \((f_i+f_j)/(p+q)\), so the pair-plus-singleton union is at least \(R/(R+1)\) times \(f_1+f_2+f_3\). The item-specific frequency-linear coefficients are nonnegative. Scaling all frequencies down by \(\sqrt{R/(R+1)}\) preserves the upper caps and balances the linear and reciprocal terms, proving the bound. For totality, take a minimizer of the separated expression defining \(M_0\). If some period ratio is rational, charging the true pair intersection at the same vector makes that pair closure strictly cheaper because \(K_0>0\). Otherwise a one-sided continued-fraction convergent changes one period upward by \(O(q^{-2})\), preserving its cap, while creating an intersection of order \(\Omega(q^{-1})\). On a fixed compact neighbourhood the separated cost is Lipschitz, so the positive \(K_0\) intersection saving dominates for large \(q\). Hence some finite pair pattern has cost \(<M_0\); the tail factor increases to one, so a finite closing \(R\) exists. ∎

Let \(M_\partial\) be the minimum of \(M_0\) and the three finitely closed one-pair boundary minima.

## 3.4 Finite primitive-triple generator

For a primitive triple define

\[
\sigma_{ij}(\mathbf a)=\frac{a_i+a_j}{\gcd(a_i,a_j)},
\]

and let \(\sigma_{(2)}\) be the second-smallest of the three values.

**Proposition 2 (finite generation).** For every integer \(S\ge2\), the set \(\mathcal E_S=\{\mathbf a:\sigma_{(2)}(\mathbf a)\le S\}\) of primitive positive triples is finite, and every coordinate is at most \((S-1)^2\).

*Proof.* Two qualifying pair ratios share an item; relabel them \((a_1:a_2)=(r:s)\) and \((a_1:a_3)=(u:v)\), with coprime pairs and \(r+s,u+v\le S\). With \(D=\operatorname{lcm}(r,u)\), the triple before primitive reduction is \((D,Ds/r,Dv/u)\). Its coordinates are bounded respectively by \(ru,us,rv\), each at most \((S-1)^2\); primitive reduction can only decrease them. Enumerating the two finite reduced-ratio lists therefore generates the set. ∎

## 3.5 Global triple tail

**Proposition 3 (triple tail).** Every primitive triple omitted from \(\mathcal E_S\) has cost at least

\[
\sqrt{\frac{S-1}{S+1}}\,M_\partial.
\]

*Proof.* Retain the least-complex pair, say \((1,2)\), and write \(U_{12}=f_1+f_2+f_3-I_{12}\) for its one-pair union. The other two complexities are at least \(S+1\), whence

\[
I_{13}+I_{23}\le\frac{f_1+f_2+2f_3}{S+1}\le\frac{2U_{12}}{S+1};
\]

the second inequality uses \(2I_{12}\le f_1+f_2\). Inclusion–exclusion and \(I_{123}\ge0\) give \(U\ge[(S-1)/(S+1)]U_{12}\). The same factor may be applied to all nonnegative frequency-linear item terms. Scaling the resulting frequencies by the square root of that factor preserves the caps and compares the reciprocal terms with the corresponding one-pair boundary optimum. Taking the least boundary yields the claim. ∎

## 3.6 Totality and exactness of the finite oracle

**Proposition 4 (strict interior improvement).** For every feasible rational three-item instance with \(K_0>0\), some fully commensurable feasible policy has cost strictly below \(M_\partial\).

*Proof.* Choose a boundary minimizer attaining \(M_\partial\), whose existence follows from Proposition 1 and the coercive capped EOQ terms. If its remaining ratios are rational, the same period vector is fully commensurable and the true inclusion–exclusion union subtracts at least one positive intersection absent from the boundary expression, strictly reducing cost.

Otherwise first consider a one-pair minimizer \((qt,pt,T_k)\), with \(\alpha=T_k/t\notin\mathbb Q\). Infinitely many one-sided continued-fraction convergents \(r_m/s_m\ge\alpha\) satisfy \(0\le r_m/s_m-\alpha<1/s_m^2\). Replacing \(T_k\) by \((r_m/s_m)t\) preserves its lower period bound. The boundary objective changes by at most \(c_1/s_m^2\) for a finite local Lipschitz constant \(c_1\). The resulting primitive common lattice has a new intersection between item \(k\) and, say, item \(i\) of density at least \(c_2/s_m\) for a constant \(c_2>0\) depending only on the fixed pair and the limiting periods. Because the net inclusion–exclusion saving \(I_{ik}+I_{jk}-I_{123}\) is at least \(I_{ik}\), the true objective is smaller by at least \(K_0c_2/s_m-c_1/s_m^2>0\) for large \(m\).

For a three-singleton minimizer, set \(\alpha=T_2/T_1\) and \(\beta=T_3/T_1\). Simultaneous Dirichlet approximation supplies infinitely many integers \(q\) and \(r,s\) with \(|\alpha-r/q|,|\beta-s/q|\le q^{-3/2}\). Dilate the approximating vector \(T_1(1,r/q,s/q)\) by

\[
\lambda=\max\{1,\alpha q/r,\beta q/s\}=1+O(q^{-3/2})
\]

so all three periods are no smaller than the boundary periods and every cap remains feasible. The smooth boundary cost changes by \(O(q^{-3/2})\), whereas at least the item-1/item-2 intersection of the common lattice has density \(\Omega(q^{-1})\). The net union saving is at least the largest pair intersection, so it again dominates. Thus a strictly cheaper fully commensurable policy exists in every case. ∎

<div class="theorem-statement">

**Theorem 1 (candidate exact three-item oracle).** Enumerate \(\mathcal E_S\), solve every fixed triple exactly, and increase \(S\) until the best incumbent \(C_S\) satisfies

\[
C_S<\sqrt{\frac{S-1}{S+1}}M_\partial.
\]

This procedure terminates after finitely many cutoffs and returns \(C^*(I)=C_S\). The optimum is attained by one of the enumerated primitive triples.

</div>

*Proof.* Proposition 4 supplies a fully commensurable policy of cost \(C<M_\partial\). Its finite primitive triple enters \(\mathcal E_S\) for all sufficiently large \(S\), while the tail factor increases to one, so the displayed strict inequality eventually holds. Proposition 3 then excludes every omitted triple; the finite enumeration covers the rest, and the boundary regimes are no better by definition of \(M_\partial>C_S\). ∎

# 4. Exact witness, active envelope, and consequences

## 4.1 Strongest rational witness

The strongest bundled instance sets \(K_0=1\), \(K_i=0\),

\[
(H_1,H_2,H_3)=
\left(
\frac{23550892369}{60000000000},
\frac23,
\frac{2113788266473847}{1396110000000000}
\right),
\]

and

\[
(\bar f_1,\bar f_2,\bar f_3)=
\left(\frac{56015}{92726},\frac{153463}{200000},1\right).
\]

The oracle enumerates 49,981 primitive triples at the minimal closing cutoff \(S=21\). The exact boundary minimum is

\[
M_\partial=
\frac{17632594822136234507342657}{3625730401798950000000000},
\]

and the omitted-triple threshold is

\[
\sqrt{\frac{10}{11}}M_\partial>C^*.
\]

The optimal exact frequencies are

\[
(f_1,f_2,f_3)=
\left(\frac{56015}{92726},\frac{56015}{92726},\frac{168045}{185452}\right),
\]

whereas the relaxed cap corner is

\[
\left(\frac{56015}{92726},\frac{153463}{200000},1\right).
\]

The exact coordinate slows item 2 by approximately 21.2720% and item 3 by 9.3863% relative to those relaxed frequencies. Four neighboring primitive policies lie only

\[
\frac{1908610761442657}{10877191205396850000000000}
=1.7546908254\times10^{-10}
\]

above the winner. That near-collision is mathematically useful and operationally fragile: a unique nominal minimizer should not be mistaken for a uniquely robust policy.

## 4.2 Exact active-policy equalisation

Write \(x=\bar f_1\), \(y=\bar f_2\), and normalize \(\bar f_3=K_0=1\), \(K_i=0\). The four policies

\[
(2,1,1),\quad(2,2,1),\quad(3,2,2),\quad(4,3,2)
\]

have exactly equal cap-bound cost when

\[
H_1=\frac{2y^2}{3},\qquad H_2=\frac23, H_3=-\frac{4y^3-7y^2+7y-2}{3(y-1)}.
\]

Their common cost is \((3y^2-5)/(3(y-1))\). Equality with the \((3,3,2)\) policy is governed by

\[
18x^2y-18x^2-9xy^2+15x-2y^3+8y^2-8y-2=0.
\]

Exact elimination isolates a stationary point of this five-policy family at

\[
y=0.7673150396176354748\ldots,\qquad
x=0.6040916335357804026\ldots,
\]

with family ratio \(1.1487291465036805297\ldots\). This stationary calculation is a discovery guide, not a proof of the exact three-item constant. The bundled rational point \(y=153463/200000\), \(x=56015/92726\) stays strictly on the \((3,3,2)\)-winner side and certifies a ratio within approximately \(2.9\times10^{-11}\) of that family value.

## 4.3 Fixed-item monotonicity and relaxation barrier

Let \(\Gamma_{n,\square}\) be the supremal exact-to-relaxed ratio over \(n\)-item independent-cap instances. Then

\[
\Gamma_{n+1,\square}\ge\Gamma_{n,\square}.
\]

To see this, append an item with \(K_{n+1}=0\), \(H_{n+1}=\varepsilon>0\), and a cap no larger than an existing relaxed maximum frequency. Removing that item from any exact schedule can only reduce union density and removes a nonnegative item cost, so the extended exact optimum is at least the original exact optimum. The extended relaxation can reuse the original relaxed solution and adds at most \(\varepsilon/f_0\) for a fixed admissible \(f_0>0\). Letting \(\varepsilon\downarrow0\), then taking suprema, proves monotonicity.

Consequently,

\[
1.1487291464748205845\ldots
\le\Gamma_{n,\square}
\le\frac5{6\ln2}
\qquad(n\ge3),
\]

where the upper comparator is the resource-constrained guarantee reported in Segev's arXiv:2603.18720v1 preprint. It is an external upper result with preprint status, not part of the present certificate. The witness also imposes a precise proof barrier: no universal statement of the form \(C^*(I)\le\alpha L(I)\) against this relaxation can hold with \(\alpha\) below the certified ratio. This does not preclude better approximation algorithms using stronger lower bounds or different analyses.

## 4.4 Certified inner holding-cost boxes and regression portfolio

For fixed periods the objective is affine in \((H_1,H_2,H_3)\). The winning \((3,3,2)\) schedule remains cap-bound and therefore fixed throughout each declared box. If exact global certificates select it at all eight vertices of a holding-cost box, its cost is no larger than any fixed competing schedule throughout the convex hull. This proves—not samples—the whole box.

The eight-vertex certificates give **certified inner radii under simultaneous relative holding-cost perturbation**

\[
\rho_{\mathrm{headline}}=9.6371555722\times10^{-11}
\]

for the strongest active-envelope witness and

\[
\rho_{\mathrm{margin}}=1.2167272558\times10^{-6}
\]

for the preceding v0.2 witness. In both boxes only \((H_1,H_2,H_3)\) varies; \(K_0\), all \(K_i\), every cap, event attribution, and the common-origin policy class remain fixed. Both select \((3,3,2)\) at every vertex. These are conservative certified inner boxes, not maximal stability chambers and not operational uncertainty regions. Moving essentially all the way to the active envelope improves the ratio by only \(3.6688888503\times10^{-7}\) but reduces the certified inner radius by more than four orders of magnitude. The bundled five-policy object is therefore frozen as a regression fixture; it is not an operational portfolio to be transferred to a fitted instance.

## 4.5 Audit and margin witnesses

A simpler audit instance gives

\[
\Gamma_{3,\square}\ge\frac{9586}{8355}=1.147336923997606\ldots
\]

at multipliers \((3,2,2)\). It sacrifices tightness for transparent coefficients.

The v0.2 rational witness is also retained. Its ratio

\[
1.1487287795859355536\ldots
\]

is slightly weaker but has a substantially larger exact policy margin and certified holding-cost box. It is the preferred regression and robustness fixture; the active-envelope witness is the headline lower-bound fixture.

The strong lower bound lies 4.6588% multiplicatively below the preprint upper comparator \(5/(6\ln2)=1.2022458674\ldots\), meaning \((U-L)/L=0.046588\ldots\) for \(L\) equal to this paper's certified lower bound and \(U\) equal to that reported preprint bound. This descriptive comparator is not a certified interval contraction, because the two endpoints have different producers and assurance states. The exact three-item constant and the unrestricted multi-item constant remain open.

# 5. Software and certificate assurance

The discovery oracle writes a certificate containing exact inputs, relaxation regimes, pair-boundary optima, enumerated triple count, incumbent, exact gap, tail factors, and strict closure margins. A solver-independent producer verifier recomputes these objects without importing the discovery oracle. Version 0.3.1 strengthens the handoff in seven ways:

1. JSON floats are rejected; rational data must be integers or explicit rational/decimal strings.
2. A versioned strict schema enforces required and allowed fields, exact list lengths, scalar types, unique pair/policy records, and canonical rational tokens before enumeration begins.
3. Certificate expressions are restricted to integer/rational arithmetic and `sqrt`; unrestricted symbolic parsing is not used on certificate frequencies.
4. Negative controls reject empty/truncated lists, omitted and duplicate records, malformed radicals, unknown fields, false tail factors, false certification, wrong scalar types, and seeded structural mutations.
5. Replay serializes repository-relative identifiers. The declared regeneration target is **byte identity for canonical JSON reports** and semantic identity for platform metadata; two independent temporary extraction roots produce identical verification JSON.
6. The active-envelope derivation and rational witness are separately recorded, preventing the numerical stationary guide from being confused with the certified lower bound.
7. Sixteen exact vertex certificates and two holding-box verifiers support the local holding-cost comparison; neither is represented as independent review.

The checker remains same-producer and shares `ScaleCost`, exact comparison, rational conversion, and instance parsing with the certificate producer. Agreement is therefore implementation-diverse producer consistency evidence, not independent rerun or reimplementation. The finite-generation, tail, and totality proofs are written mathematics checked against executable regressions; they have not been proof-assistant formalised or externally reviewed.

# 6. A defensible logistics role

The strongest near-term use is not to replace an enterprise replenishment system. It is to improve what small exact benchmarks can reveal.

## 6.1 Triplet diagnostic

Select three SKUs only after an **event-closure gate**. The triplet must either own the common event economically and calendrically, be evaluated conditional on a frozen exogenous background calendar with an explicitly marginal event cost, or be excluded from operational use and retained as software-only input. Estimate the incremental common event cost, item-specific costs, deterministic holding coefficients, and semantically valid average-frequency caps in consistent units. Compare the oracle, the max-frequency relaxation, and the incumbent fixed-interval schedule. A material exact-relaxation gap is a diagnostic that the relaxed lower bound should not be treated as operationally attainable.

## 6.2 Regression fixture

The rational witnesses are exact fixtures for ERP, APS, solver, and heuristic testing. A planning implementation that claims a lower deterministic periodic cost than the certificate is either solving a different model or contains a defect. The simple witness is suitable for human audit; the v0.2 margin witness is preferable for regression and sensitivity testing; the active-envelope witness tests exact arithmetic and the new lower-bound frontier.

## 6.3 Instance-specific candidate set

The bundled five-policy set is a frozen regression fixture for the two declared synthetic witnesses. For a fitted operational instance, the software must enumerate and verifier-check an **instance-specific** deterministic candidate set across the certified boundary, primitive-triple search, and tail closure. Membership is defined by a preregistered relative-regret tolerance plus calendar feasibility; excluded policies and the tail margin are recorded. Simulation then ranks that instance-specific set using service, workload peaks, supplier feasibility, and sensitivity. The certified inner holding-cost boxes vary only \(H\); they are warnings against operational confidence, not evidence under joint uncertainty or omitted constraints.

# 7. What the oracle omits

Real replenishment studies repeatedly add features absent here: minimum order quantities and nonlinear transport costs; dynamic demand and time-varying capacity; stochastic demand, lead time, backlog, and lost sales; and explicit service targets. These features can dominate arithmetic coordination. In particular:

- a container or dock has pointwise capacity, not merely a long-run frequency cap;
- a minimum order quantity restricts quantities and cycle sizes, not only frequency;
- uncertain demand changes both inventory cost and service risk;
- lead-time variability can turn a cost-optimal periodic calendar into an unacceptable service policy;
- fixed-cost estimates can be unstable when receiving labour or transport is tiered rather than truly fixed.

Consequently, the model-to-operation bridge must be owned through a recorded RACI: operations owns the decision and rollback; procurement owns supplier/calendar semantics; finance owns incremental-cost attribution; warehouse and service owners approve feasibility and non-inferiority constraints; data/engineering owns lineage and implementation; an independent methods reviewer approves any causal design. Any triplet failing the semantic-fit or event-closure gate is excluded rather than forced into the model.

# 8. Field-evidence programme

The proposed programme has seven escalating gates, numbered 0 through 6: semantic fit and event closure; reconciled data; exact stress test and instance-specific candidate generation; operational simulation; shadow deployment; bounded field pilot; and scale/monitor. Before simulation, an empirically justified joint uncertainty set covers \(K_0\), \(K_i\), \(H_i\), caps, event attribution, and relevant calendars. Reports include policy rank, regret, feasibility, service, and worst-case outcomes—not only an \(H\)-box.

The field design is not triggered by a fixed duration or cycle count. A preregistered adequacy assessment must justify the assignment unit, interference graph and exposure mapping, warm-up and carryover, horizon and seasonality coverage, precision or power for the service and cost estimands, override/noncompliance handling, missingness, multiplicity, full cost boundary, and stopping authority. Switchback, cluster-randomised, stepped, or other concurrent designs are selected only when their identifying assumptions fit the operating network. The requirements are motivated by the switchback guidance of Bojinov, Simchi-Levi, and Zhao, the cluster-interference evidence of Holtz et al., and the operations field-experiment tutorial of Ibanez and Staats; none selects a design automatically for a future site.

Primary outcomes are plan-change rate, total landed cost, inventory value, customer service, stockouts, expedites, carrier and supplier feasibility, transport utilization, dock workload, overtime and worker burden, emissions or waste where material, planner effort, and integration/compliance cost. Carriers and suppliers validate calendar feasibility; customer/service owners set non-inferiority limits; worker representatives review workload and safety; sustainability owners approve any environmental metric; legal, privacy, labour, and regulatory owners approve their respective boundaries. Automatic stops cover service degradation, safety or stockout thresholds, excessive infeasibility from omitted constraints, planner overrides, negative net value, and parameter drift.

Until such a design is completed, Evidence Press should classify operational value as **untested**. A successful exact certificate supports a bounded mechanism; a shadow run supports feasibility; an uncontrolled company comparison is at most a field association; a causal claim requires a defensible concurrent comparison and independent methodological review.

# 9. Limitations and open questions

- The executable oracle accepts independent caps, not arbitrary coupled resource rows.
- The lower bound comes from a synthetic active-envelope family and one certified rational member; no distribution of gaps over representative logistics instances is known.
- The exact three-item constant and unrestricted multi-item constant remain unknown.
- The finite generator, global tail, and totality proof require external specialist audit or formalisation.
- The targeted literature search does not establish absolute novelty or priority.
- The package has no unaffiliated rerun, independent reimplementation, specialist review, editorial peer review, or field validation.
- Periodic common-origin schedules exclude several common operational policy classes.

# 10. Conclusion

The candidate exact three-item calculation changes the known producer-side lower-bound frontier. The ratio \(1.1487291464748206\ldots\) propagates to every fixed \(n\ge3\), lower-bounds every universal analysis against the max-frequency relaxation, and rules out a simple extension of the unrefereed two-item candidate constant. The active-family and certified inner holding-cost boxes also expose a crucial application tradeoff: a marginally stronger mathematical witness can be far less stable to coefficient perturbation. Exact triplets should therefore test relaxation optimism, benchmark planning software, and generate instance-specific near-optimal sets; operational modelling and prospective evidence remain necessary before decisions or claims of value.

That separation is the central contribution of the release design. Exact arithmetic can settle the bundled model calculation. It cannot by itself settle semantics, field performance, or implementation value.

# References

1. Agent collective and I. Pitchford. *Exact two-item resource-constrained joint replenishment and its independent-cap relaxation gap*. Evidence Press / Zenodo, v1.2.0-candidate, 2026. <https://doi.org/10.5281/zenodo.21855894>.
2. D. Segev. *Resource-constrained joint replenishment via power-of-$m^{1/k}$ policies*. arXiv:2603.18720v1, 2026. <https://arxiv.org/abs/2603.18720>.
3. A. S. Schulz and C. Telha. “Integer factorization: Why two-item joint replenishment is hard.” *Operations Research* 72(3), 1192–1202, 2024. <https://doi.org/10.1287/opre.2022.2390>.
4. D. Segev. “The continuous-time joint replenishment problem: $\varepsilon$-optimal policies via pairwise alignment.” *Management Science* 71(5), 4183–4197, 2025. <https://doi.org/10.1287/mnsc.2023.00705>.
5. D. Segev. “Improved approximation guarantees for joint replenishment in continuous time.” *Mathematics of Operations Research* 51(2), 1683–1712, 2026; published online 2025. <https://doi.org/10.1287/moor.2024.0635>.
6. R. Roundy. “Rounding off to powers of two in continuous relaxations of capacitated lot sizing problems.” *Management Science* 35(12), 1433–1442, 1989. <https://doi.org/10.1287/mnsc.35.12.1433>.
7. C.-P. Teo and D. Bertsimas. “Multistage lot sizing problems via randomized rounding.” *Operations Research* 49(4), 599–608, 2001. <https://doi.org/10.1287/opre.49.4.599.11222>.
8. T. Cohen-Hillel and L. Yedidsion. “The periodic joint replenishment problem is strongly NP-hard.” *Mathematics of Operations Research* 43(4), 1269–1289, 2018. <https://doi.org/10.1287/moor.2017.0904>.
9. S. Creemers and T. Stephan. *Special Cases of the Joint Replenishment Problem (JRP): A Mathematical Analysis*. SSRN 6674418, 2026. <https://doi.org/10.2139/ssrn.6674418>.
10. M. Porras Musalem and R. Dekker. “Controlling inventories in a supply chain: a case study.” *International Journal of Production Economics* 93–94, 179–188, 2005. <https://doi.org/10.1016/j.ijpe.2004.06.016>.
11. T. S. Winter and J. H. Van Vuuren. “A practical method for joint inventory replenishment under supplier constraints.” *South African Journal of Industrial Engineering* 36(2), 2025. <https://doi.org/10.7166/36-2-3194>.
12. I. Suemitsu, N. Miyashita, J. Hosoda, Y. Shimazu, T. Nishikawa, and K. Izui. “Integration of sales, inventory, and transportation resource planning by dynamic-demand joint replenishment problem with time-varying costs.” *Computers & Industrial Engineering* 188, 109922, 2024. <https://doi.org/10.1016/j.cie.2024.109922>.
13. S. Creemers and R. Boute. “The joint replenishment problem: optimal policy and exact evaluation method.” *European Journal of Operational Research* 302(3), 1175–1188, 2022. <https://doi.org/10.1016/j.ejor.2022.02.005>.
14. L. Peng, L. Wang, and S. Wang. “A review of the joint replenishment problem from 2006 to 2022.” *Management System Engineering* 1, article 9, 2022. <https://doi.org/10.1007/s44176-022-00010-3>.
15. R. E. Wildeman, J. B. G. Frenk, and R. Dekker. “An efficient optimal solution method for the joint replenishment problem.” *European Journal of Operational Research* 99(2), 433–444, 1997. <https://doi.org/10.1016/S0377-2217(96)00072-0>.
16. I. Bojinov, D. Simchi-Levi, and J. Zhao. “Design and analysis of switchback experiments.” *Management Science* 69(7), 3759–3777, 2023. <https://doi.org/10.1287/mnsc.2022.4583>.
17. D. Holtz, F. Lobel, R. Lobel, I. Liskovich, and S. Aral. “Reducing interference bias in online marketplace experiments using cluster randomization: evidence from a pricing meta-experiment on Airbnb.” *Management Science*, published online 2024. <https://doi.org/10.1287/mnsc.2020.01157>.
18. M. R. Ibanez and B. R. Staats. “Field experiments in operations management.” In *Operations Research & Management Science in the Age of Analytics*, 1–16, 2019. <https://doi.org/10.1287/educ.2019.0197>.
19. A. Tschan, L. Hetzel, R. Eisinger, C. Eggen, C. Heuser, and V. Fritz. “Data-driven inventory control and integrated employee involvement for special buys at ALDI SÜD Germany.” *INFORMS Journal on Applied Analytics* 55(1), 22–35, 2025. <https://doi.org/10.1287/inte.2024.0182>.
20. L. Wang and H. Chen. “Optimization of a stochastic joint replenishment inventory system with service level constraints.” *Computers & Operations Research* 148, 106001, 2022. <https://doi.org/10.1016/j.cor.2022.106001>.

Publisher-linked source-use notes and the corrected pairwise-alignment DOI are maintained in `SOURCES.md`.

# Data and code availability

All original instance data, source code, certificates, review records, exact replay instructions, and the generated paper are included in the versioned public package. Cited papers and other third-party works are linked but not redistributed. The release archive and manifest are the governing byte boundary.

# Ethics statement

This mathematical and software study used no human participants, personal data, animals, or clinical intervention. The proposed future field protocol is not evidence that a field study has occurred; any implementation involving workers, customers, or personal/operational data requires the relevant organisational, privacy, labour, and research-ethics approvals before collection or assignment.

# Author contributions and accountability

**Anonymous (scholarly creator):** Conceptualization, Methodology, Formal analysis, Software, Validation, Investigation, Data curation, Writing—original draft, and Writing—review and editing. **Ian Pitchford (non-author contributor):** Research direction, Project administration, Publication maintenance, and correction routing. Evidence Press is the accountable publisher; corrections and objections are routed through the public repository issue channel and preserved additively. Internal model-mediated editorial reports are package evidence, not external peer review.

# Funding

No external funding was declared for this candidate.

# Competing interests

No competing financial or non-financial interests were declared. The publisher's interest in the Evidence Press workflow is disclosed by the provenance and assurance records and does not upgrade the research status.

# AI-use disclosure

AI systems assisted exact-computation development, software hardening, source discovery, citation checking, internal role review, and drafting under human direction. Their outputs were checked through exact replay, primary-source readback, and editorial traceability where applicable. AI systems are not scholarly authors, independent reviewers, or independent reproducers.
