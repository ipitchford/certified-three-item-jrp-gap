# A candidate exact three-item independent-cap oracle for continuous-time joint replenishment

**Status:** candidate theorem and machine-checked finite certificate. Producer-side reconstruction only; no unaffiliated mathematical review or proof-assistant formalisation has occurred.

## Result

The unrefereed predecessor candidate reports a narrow producer-side interval with upper endpoint

\[
\Gamma_{2,\square}=\gamma\approx 1.11188959394
\]

for the two-item independent-cap quantity. The present candidate shows that this two-item interval cannot supply the unrestricted multi-item constant. The strongest bundled rational instance has

\[
K_0=1,\qquad K_1=K_2=K_3=0,
\]

\[
(H_1,H_2,H_3)=
\left(
\frac{23550892369}{60000000000},
\frac23,
\frac{2113788266473847}{1396110000000000}
\right),
\]

and caps

\[
(\bar f_1,\bar f_2,\bar f_3)=
\left(\frac{56015}{92726},\frac{153463}{200000},1\right).
\]

The oracle gives the exact relaxed value

\[
L=
\frac{12099233027737989052666993}
{3000320647128487500000000},
\]

and the exact common-origin fixed-interval optimum

\[
C^*=\frac{50387704513257323196307343}{10877191205396850000000000},
\]

attained uniquely, among primitive coordination types, by

\[
(T_1,T_2,T_3)=(3t,3t,2t),
\qquad t=\frac{92726}{168045}.
\]

Therefore

\[
\boxed{
\Gamma_{3,\square}\geq
\frac{C^*}{L}
=
\frac{7732648297718008589674913778809}
{6731480890380196637385597557508}
=1.1487291464748206\ldots
}
\]

The producer-side unrefereed two-item upper endpoint is below `1.111889593940297`. This three-item lower bound exceeds it by about `0.03683955` absolutely, or `3.3132%` multiplicatively. Every declared witness value is exact within the candidate-proof boundary, and the bundled optimum is closed by a finite tail certificate rather than inferred from a numerical search.

A second, deliberately simpler rational instance gives

\[
\Gamma_{3,\square}\geq\frac{9586}{8355}
=1.147336923997606\ldots
\]

with small coefficients and optimum multiplier triple \((3,2,2)\). It is retained as a transparent audit case; the stronger instance supplies the reported lower bound.

The package implements the **independent-cap** oracle. Its broader resource interpretation is conditional on the unrefereed predecessor candidate's cap-reduction theorem, which transfers the supremum over arbitrary nonnegative linear resource systems to item-specific frequency caps. The present three-item finite-generation, tail, totality, and witness proofs do not depend on that transfer. A generic arbitrary-row three-item implementation would require an additional exact certificate engine for two- and three-variable separable convex programmes; it is not claimed here.

## 1. Model

For periods \(T_i>0\), let \(f_i=1/T_i\). A policy is common-origin and fixed-interval: item \(i\) acts at \(T_i\mathbb Z_{>0}\). The union need not itself have a finite common period. For a locally finite event set \(A\), define \(\operatorname{dens}(A)=\lim_{x\to\infty}\#(A\cap(0,x])/x\). The limit exists for the finite lattice unions here. The exact long-run objective is

\[
F(T)=K_0\,\operatorname{dens}\!\left(\bigcup_{i=1}^3T_i\mathbb Z_{>0}\right)
+\sum_{i=1}^3\left(K_if_i+\frac{H_i}{f_i}\right),
\]

subject to independent caps

\[
0<f_i\leq \bar f_i.
\]

The standard convex relaxation replaces the exact union density by \(\max_i f_i\):

\[
L=\min_{0<f_i\leq\bar f_i}
\left[
K_0\max_i f_i+
\sum_i\left(K_if_i+\frac{H_i}{f_i}\right)
\right].
\]

All input coefficients in the implementation are rational, with \(K_0>0\), \(K_i\geq0\), \(H_i>0\), and \(\bar f_i>0\). Exact optima may contain square roots.

## 2. The three regimes are exhaustive

Define \(i\sim j\) when \(T_i/T_j\in\mathbb Q\). This is an equivalence relation. A three-element set therefore has only three possible commensurability partitions:

1. all three periods are commensurable;
2. exactly one pair is commensurable and the third period lies in a separate class;
3. all three periods are pairwise incommensurable.

The oracle solves the closure of each regime exactly. The word *closure* matters: a one-pair or desynchronised infimum can occur at scale values whose accidental rational relations place the point in the fully commensurable regime. It remains the correct boundary value for lower bounds and tail arguments.

## 3. Fully commensurable patterns

Write

\[
T_i=a_it,
\]

where \(\mathbf a=(a_1,a_2,a_3)\in\mathbb Z_{>0}^3\) is primitive:

\[
\gcd(a_1,a_2,a_3)=1.
\]

Inclusion-exclusion gives the exact union-density coefficient

\[
u(\mathbf a)=
\sum_i\frac1{a_i}
-\sum_{i<j}\frac1{\operatorname{lcm}(a_i,a_j)}
+\frac1{\operatorname{lcm}(a_1,a_2,a_3)}.
\]

For a fixed primitive triple,

\[
F_{\mathbf a}(t)=\frac{A_{\mathbf a}}t+B_{\mathbf a}t,
\]

where

\[
A_{\mathbf a}=K_0u(\mathbf a)+\sum_i\frac{K_i}{a_i},
\qquad
B_{\mathbf a}=\sum_iH_ia_i.
\]

The caps impose

\[
t\geq t_{\min}(\mathbf a)=
\max_i\frac1{a_i\bar f_i}.
\]

Hence

\[
t^*_{\mathbf a}=
\max\left\{
\sqrt{\frac{A_{\mathbf a}}{B_{\mathbf a}}},
\ t_{\min}(\mathbf a)
\right\},
\]

and the pattern cost is either rational or \(2\sqrt{A_{\mathbf a}B_{\mathbf a}}\). Comparisons between fixed triples therefore require only rational arithmetic and one squaring.

## 4. Boundary oracles

### 4.1 Pairwise incommensurable boundary

When no pair meets with positive density, the joint setup cost is charged independently to each stream:

\[
M_0=
\min_{0<f_i\leq\bar f_i}
\sum_i\left[(K_0+K_i)f_i+\frac{H_i}{f_i}\right].
\]

This separates into three one-dimensional capped economic-order-quantity calculations.

### 4.2 Exactly one commensurable pair

For pair \((i,j)\), write

\[
T_i=qt,\qquad T_j=pt,
\qquad \gcd(p,q)=1,
\]

and let item \(k\) have independent frequency \(y\). With \(x=1/t\), the pair-boundary objective is

\[
\left[
K_0\frac{p+q-1}{pq}+\frac{K_i}{q}+\frac{K_j}{p}
\right]x
+\frac{H_iq+H_jp}{x}
+(K_0+K_k)y+\frac{H_k}{y},
\]

subject to

\[
x\leq\min(q\bar f_i,p\bar f_j),
\qquad y\leq\bar f_k.
\]

The two variables separate. Each fixed \((p,q)\) again has an exact radical-or-rational cost.

### 4.3 Exact pair tail

For an omitted pair with \(p+q\geq R+1\), its intersection density is

\[
I_{ij}=\frac{f_i+f_j}{p+q}
\leq\frac{f_i+f_j}{R+1}.
\]

Therefore its union density, including the singleton, is at least

\[
\frac{R}{R+1}(f_1+f_2+f_3).
\]

Let \(r=R/(R+1)\). Multiplying all frequencies by \(\sqrt r\) preserves the caps and gives

\[
C_{ij,pq}\geq\sqrt r\,M_0.
\]

Enumerating all coprime pairs with \(p+q\leq R\) stops once the incumbent lies below this tail. The tail tends to \(M_0\), while rational approximation creates a pair-synchronised policy strictly below \(M_0\) whenever \(K_0>0\). Thus each pair-boundary oracle terminates finitely.

## 5. The correct finite cutoff for triples

A cutoff on \(\max_i a_i\) is unsuitable for a theorem. One pair can remain perfectly simple while the third multiplier grows without bound. The tail must measure how many pair relations remain simple.

For a primitive triple define the reduced pair complexity

\[
\sigma_{ij}(\mathbf a)=
\frac{a_i+a_j}{\gcd(a_i,a_j)}.
\]

It satisfies

\[
I_{ij}=\frac{f_i+f_j}{\sigma_{ij}(\mathbf a)}.
\]

Let \(\sigma_{(2)}(\mathbf a)\) denote the second-smallest of the three pair complexities.

### Finite-enumeration lemma

For every integer \(S\geq2\), the set

\[
\mathcal E_S=
\left\{
\mathbf a\text{ primitive}:\ 
\sigma_{(2)}(\mathbf a)\leq S
\right\}
\]

is finite. Every component of every member satisfies

\[
a_i\leq(S-1)^2.
\]

**Proof.** Two pair complexities at most \(S\) share a vertex; relabel them as \((1,2)\) and \((1,3)\). Write the two reduced ratios as

\[
(a_1:a_2)=(r:s),\qquad(a_1:a_3)=(u:v),
\]

with \(r+s\leq S\), \(u+v\leq S\), and both pairs coprime. Let \(L=\operatorname{lcm}(r,u)\). Up to a common factor the triple is

\[
\left(L,\frac{Ls}{r},\frac{Lv}{u}\right).
\]

The three entries are bounded respectively by \(ru\), \(us\), and \(rv\), each at most \((S-1)^2\). Removing the common divisor can only reduce them. ∎

The implementation generates \(\mathcal E_S\) from the two reduced ratios rather than scanning the containing cube. At \(S=21\), the exact set has 49,981 labelled primitive triples.

## 6. Triple tail theorem

Consider an omitted primitive triple, so

\[
\sigma_{(2)}(\mathbf a)\geq S+1.
\]

Choose the least-complex pair, say \((1,2)\), and define the one-pair boundary union density

\[
U_{12}=f_1+f_2+f_3-I_{12}.
\]

The full union density is

\[
U=U_{12}-I_{13}-I_{23}+I_{123}.
\]

The other two pair complexities are at least \(S+1\), so

\[
I_{13}+I_{23}
\leq
\frac{f_1+f_2+2f_3}{S+1}.
\]

Since \(2I_{12}\leq f_1+f_2\),

\[
f_1+f_2+2f_3\leq2U_{12}.
\]

Dropping the nonnegative triple intersection from the saving gives

\[
U\geq
\left(1-\frac{2}{S+1}\right)U_{12}
=
\frac{S-1}{S+1}U_{12}.
\]

Let

\[
r_S=\frac{S-1}{S+1},
\]

and let \(M_\partial\) be the minimum of the three exact one-pair boundary values and the desynchronised boundary value. Item-specific ordering terms are nonnegative, so the same factor can be applied to the whole frequency-linear part. Scaling every frequency down by \(\sqrt{r_S}\) preserves the caps and yields

\[
\boxed{
C_{\mathbf a}\geq
\sqrt{\frac{S-1}{S+1}}\,M_\partial
}
\]

for every omitted triple.

This is the global triple tail. It depends on the **second** pair complexity because one simple pair must be retained as the boundary model while the two omitted overlaps are bounded.

## 7. Quantified totality argument

The boundary value \(M_\partial\) is strictly above some fully commensurable feasible policy cost whenever \(K_0>0\). Boundary minima exist because the capped EOQ terms are coercive, and the pair tails reduce the one-pair search to finitely many reduced patterns.

If a boundary minimiser already has rational remaining ratios, evaluating the true three-lattice union at the same periods subtracts a positive intersection term. Otherwise, on a one-pair boundary \((qt,pt,T_3)\), choose one-sided continued-fraction convergents \(r_m/s_m\ge T_3/t\) with error below \(s_m^{-2}\). Replacing \(T_3\) by \((r_m/s_m)t\) preserves its cap. On a fixed compact neighbourhood the smooth boundary objective changes by at most \(c_1s_m^{-2}\). The new item-1/item-3 intersection has density at least \(c_2s_m^{-1}\) for a constant \(c_2>0\); inclusion–exclusion's net new saving is at least that intersection. Hence \(K_0c_2s_m^{-1}-c_1s_m^{-2}>0\) for large \(m\).

On the three-singleton boundary, simultaneous Dirichlet approximation gives infinitely many \(q,r,s\) with ratio errors at most \(q^{-3/2}\). Dilate the rational vector \(T_1(1,r/q,s/q)\) by \(\lambda=\max\{1,(T_2/T_1)q/r,(T_3/T_1)q/s\}=1+O(q^{-3/2})\). Every period is then no smaller than its boundary value, so all caps remain feasible. The smooth cost perturbation is \(O(q^{-3/2})\), whereas the common-lattice item-1/item-2 intersection has density at least \(1/(r\lambda T_1)=\Omega(q^{-1})\). Again the intersection saving dominates.

Thus some fully commensurable candidate has cost \(C<M_\partial\). Since the tail factor increases to one, a finite \(S\) eventually satisfies

\[
C<\sqrt{\frac{S-1}{S+1}}M_\partial.
\]

The candidate's primitive triple is in the finite generator for all sufficiently large \(S\); at the displayed strict inequality, the enumeration and tail jointly certify the common-origin fixed-interval global optimum. This is a totality statement, not a polynomial-time bound. The complete numbered theorem and dependency table are in §§2–3 of the paper PDF.

## 8. The rational counterexample certificates

### 8.1 Margin witness retained from v0.2

At the cap corner

\[
(f_1,f_2,f_3)=
\left(\frac{6041}{10000},\frac{15347}{20000},1\right),
\]

item 3 is the unique maximum. The one-sided derivatives toward larger feasible frequencies are

\[
-\frac{235530409}{218962086},
\qquad
-\frac{800000000}{706591227},
\qquad
-\frac{718120871923}{1395900000000}.
\]

All are negative. Convexity therefore certifies the cap corner as the relaxed optimum, with

\[
L=
\frac{521939813582654774521}
{129415601769300000000}
=4.033051706648784\ldots
\]

The exact desynchronised boundary value is

\[
M_0=
\frac{699426840629161259521}
{129415601769300000000}.
\]

The three pair-boundary oracles close as follows:

| Pair | Best reduced ratio \((p,q)\) | Exact value | Minimal pair cutoff |
|---|---:|---:|---:|
| \((1,2)\) | \((1,1)\) | \(41083199883461843/8432631900000000\) | \(R=5\) |
| \((1,3)\) | \((1,2)\) | \(10573673069231/2142287730000\) | \(R=6\) |
| \((2,3)\) | \((1,1)\) | \(2050673655001/421631595000\) | \(R=5\) |

Hence

\[
M_\partial=\frac{2050673655001}{421631595000}.
\]

The enumeration over \(\mathcal E_{21}\) contains exactly 49,981 labelled primitive triples. Its unique best triple is

\[
\mathbf a=(3,3,2).
\]

For this triple,

\[
u(3,3,2)=\frac23,
\qquad
A=\frac23,
\qquad
B=\frac{17327452466923}{2791800000000},
\qquad
t_{\min}=\frac{10000}{18123}.
\]

The first-item cap binds, so

\[
C^*=\frac{A}{t_{\min}}+Bt_{\min}
=\frac{23440435983871}{5059579140000}
=4.632882564985632\ldots
\]

Four neighbouring coordination types, \((4,3,2)\), \((3,2,2)\), \((2,1,1)\), and \((2,2,1)\), tie at

\[
\frac{1293408773}{279180000}
=4.632884780428397\ldots
\]

Only

\[
\frac{1401151}{632447392500}
=2.21544\times10^{-6}
\]

separates them from the optimum. This five-policy near-collision explains why a local numerical search found the stronger instance.

The omitted-triple tail at \(S=21\) is

\[
\sqrt{\frac{10}{11}}
\frac{2050673655001}{421631595000}
=4.637319963640239\ldots
>C^*.
\]

The comparison is exact after squaring:

\[
\frac{10}{11}
\left(\frac{2050673655001}{421631595000}\right)^2
-
\left(\frac{23440435983871}{5059579140000}\right)^2
=
\frac{11583482360332362632810389}
{281592751813154535600000000}>0.
\]

At \(S=20\), the corresponding squared margin is

\[
-\frac{439157165690186034331663}
{7167815500698479088000000}<0,
\]

so \(S=21\) is the minimal closing cutoff for this enumeration order.

The resulting exact gap is

\[
\frac{1798701855222341185000}
{1565819440747964323563}
=1.1487287795859355\ldots
\]

This witness remains the preferred regression and sensitivity fixture because its exact winner margin is materially larger than that of the headline active-envelope point.

### 8.2 Active-envelope headline witness

Let \(x=\bar f_1\), \(y=\bar f_2\), \(\bar f_3=1\), \(K_0=1\), and \(K_i=0\). Direct equality of the four cap-bound policy costs for

\[
(2,1,1),\quad(2,2,1),\quad(3,2,2),\quad(4,3,2)
\]

gives the rational family

\[
H_1=\frac{2y^2}{3},\qquad H_2=\frac23,qquad
H_3=-\frac{4y^3-7y^2+7y-2}{3(y-1)}.
\]

The four policies have common cost

\[
R(y)=\frac{3y^2-5}{3(y-1)}.
\]

The cap-bound \((3,3,2)\) cost meets that envelope precisely when

\[
E(x,y)=18x^2y-18x^2-9xy^2+15x-2y^3+8y^2-8y-2=0.
\]

Eliminating \(x\) between \(E=0\) and the stationary equation for \(R(y)/L(x,y)\) gives a degree-22 factor. The machine-readable analysis records that polynomial and an exact isolating interval containing one root. Numerically, the relevant stationary point is

\[
y_*=0.7673150396176354748\ldots,
\qquad
x_*=0.6040916335357804026\ldots,
\]

with active-family ratio

\[
1.1487291465036805297\ldots.
\]

This is a stationary point of the five-policy family, not a global three-item upper certificate. For a rational exact witness choose

\[
y=\frac{153463}{200000},
\qquad
x=\frac{56015}{92726}.
\]

The exact crossover polynomial satisfies

\[
E(x,y)=
\frac{1908610761442657}{8598111076000000000000000}>0,
\]

placing the point strictly on the \((3,3,2)\)-winner side. The exact oracle again closes at \(S=21\) after enumerating 49,981 triples. It gives

\[
L=\frac{12099233027737989052666993}{3000320647128487500000000},
\]

\[
C^*=\frac{50387704513257323196307343}{10877191205396850000000000},
\]

and therefore

\[
\boxed{
\Gamma_{3,\square}\ge
\frac{7732648297718008589674913778809}
{6731480890380196637385597557508}
=1.1487291464748205845\ldots
}.
\]

The four runner policies tie exactly at \(129347322893/27922200000\), only

\[
\frac{1908610761442657}{10877191205396850000000000}
=1.7546908254\times10^{-10}
\]

above the winner. Thus the active-envelope witness is the strongest bundled lower-bound fixture but deliberately not the preferred robustness fixture.

### 8.3 Small-coefficient audit instance

The second certificate uses

\[
(H_1,H_2,H_3)=\left(\frac25,\frac23,\frac32\right),
\qquad
(\bar f_1,\bar f_2,\bar f_3)=
\left(\frac35,\frac{23}{30},1\right).
\]

It has

\[
L=\frac{557}{138},
\qquad
C^*=\frac{4793}{1035},
\qquad
\mathbf a^*=(3,2,2),
\qquad
t^*=\frac{15}{23},
\]

and therefore

\[
\frac{C^*}{L}=\frac{9586}{8355}
=1.147336923997606\ldots
\]

Its boundary value is \(3353/690\), and its minimal triple cutoff is also \(S=21\). The simpler fractions make this certificate useful for hand reconstruction, while the active-envelope certificate records the current exact lower bound.

## 9. Fixed-item monotonicity and holding-box robustness

Let \(C_n(I)\) and \(L_n(I)\) be the exact and relaxed values of an \(n\)-item independent-cap instance. Append an item with \(K_{n+1}=0\), \(H_{n+1}=\varepsilon>0\), and a cap admitting a fixed \(f_0\) below the old relaxed maximum. Deleting the new item from any exact schedule weakly lowers union density and removes nonnegative cost, so

\[
C_{n+1}(I_\varepsilon)\ge C_n(I).
\]

The extended relaxation can use the old optimizer and \(f_{n+1}=f_0\), hence

\[
L_{n+1}(I_\varepsilon)\le L_n(I)+\frac{\varepsilon}{f_0}.
\]

Letting \(\varepsilon\downarrow0\), then taking the supremum over \(I\), proves

\[
\boxed{\Gamma_{n+1,\square}\ge\Gamma_{n,\square}}.
\]

The active-envelope lower bound therefore holds for every fixed \(n\ge3\). It also lower-bounds every universal inequality comparing exact cost directly with this relaxation.

The robustness certificate uses a separate finite-vertex argument. Holding coefficients enter the objective affinely for every fixed feasible schedule. The \((3,3,2)\) winner is cap-bound, so the same fixed schedule applies throughout each declared holding box. At every box vertex, the exact oracle certifies that this schedule beats the entire infinite schedule universe. For any competing fixed schedule, its cost difference from the winner is affine in \(H\); nonnegativity at all eight vertices implies nonnegativity throughout their convex hull.

The producer-side certificates establish simultaneous relative holding-cost radii

\[
\rho=9.6371555722\times10^{-11}
\]

for the active-envelope witness and

\[
\rho=1.2167272558\times10^{-6}
\]

for the v0.2 margin witness. These boxes do not cover cap, setup-cost, demand, lead-time, or omitted-model uncertainty. The five active calendars remain frozen regression fixtures; any fitted operational instance must regenerate its own verifier-checked candidate set.

## 10. Relation to Segev's 2026 power-grid result

Segev's resource-constrained analysis proves an algorithmic factor

\[
\frac{5}{6\ln2}=1.2022458674\ldots
\]

and shows that factor is best possible for the paper's interleaved power-of-\(m^{1/k}\) policy class. It does not identify the exact integrality gap of the convex relaxation.

The present certificate places the actual multi-item relaxation gap at least at

\[
1.1487291465.
\]

Thus the remaining multiplicative interval to Segev's factor is about `4.659%`. The two results delimit different objects:

* this oracle gives an exact lower bound on the relaxation's intrinsic loss;
* Segev gives a general feasible-policy upper guarantee from a structured rounding family.

The next exact target is a global upper certificate over the three-item cap parameter space, not merely a larger integer-triple cutoff. The active-envelope calculation explains and nearly optimizes one five-policy obstruction, but it does not rule out another active set or regime. The exact three-item constant remains open.

## 11. Reproduction boundary

The certificate establishes the declared rational instance and nothing broader than the proved tail permits. In particular, it does **not** establish:

* the exact value of \(\Gamma_{3,\square}\);
* the unrestricted multi-item constant;
* equality with Segev's \(5/(6\ln2)\) factor;
* a polynomial-time three-item exact algorithm in binary input length;
* an arbitrary-resource-row implementation;
* external independent verification or peer review.

The supplied verifier is solver-independent: it reimplements the relaxation, boundary enumeration, primitive-triple generator, fixed-pattern cost, tail comparisons, and gap calculation without importing the discovery oracle. It also checks that the pair and triple cutoffs are minimal and rejects numerical and structural mutations. Because it was created in the same workflow and shares parsing and exact-algebra utilities, this is producer-side replay rather than an independent reimplementation.
