# Why a bounded number of feedback rounds cannot attain quadratic global precision

[Science index](README.md) · [Posterior converse](two_batch_converse.md) · [Thermal information](entropy_budget.md)

The two-batch exponent extends to a **converse-only** statement for any prescribed number of Gibbs-preparation batches. These results constrain feedback depth; no general matching construction beyond two batches is claimed.

## Posterior-information recurrence

Fix the same smooth zero-endpoint prior $\pi$ as in the two-batch theorem and define $J_0=I(\pi)>0$. After batch $j$, let $\pi_{Y_{\le j}}$ denote the posterior given the complete revealed energy-label history and write

$$
J_j=\mathbb E[I(\pi_{Y_{\le j}})].
$$

The posterior-score identity and the conditional entropy-area budget apply history by history. For batch $j$ containing at most $n_j(y_{<j})\le N$ charged qubits on each branch,

$$
\begin{aligned}
J_j-J_{j-1}
&=\mathbb E\left[\int\pi_{Y_{<j}}(x)
F_{H_j(Y_{<j})}(x)dx\right]\\
&\le N\ln2\,
\mathbb E[\|\pi_{Y_{<j}}\|_\infty]\\
&\le\frac{N\ln2}{2}\sqrt{J_{j-1}}.
\end{aligned}
$$

Thus

$$
\boxed{J_j\le J_{j-1}+\tfrac12 N\ln2\,\sqrt{J_{j-1}}.}
$$

For deterministic allocations, $N$ in the additive term can be replaced by $n_j$. More generally the proof needs only the pathwise $N$-qubit cap; the bound is intentionally not optimized over allocations.

## Fixed-$r$ global-risk lower bounds

For any fixed $r$ independent of $N$, induction from $J_0=O(1)$ gives

$$
J_r=O_r(N^{\gamma_r}),\qquad
\gamma_0=0,\quad \gamma_j=1+\frac{\gamma_{j-1}}2
=2(1-2^{-j}).
$$

Indeed, if $J_{j-1}=O_r(N^{\gamma_{j-1}})$ with $\gamma_{j-1}<2$, the newly added $N\sqrt{J_{j-1}}$ term dominates asymptotically. Van Trees applies to the complete history, giving

$$
\boxed{
R_r^*(N;[a,b])\ge c_r\,N^{-[\,2-2^{1-r}\,]}.}
$$

For $r=1$ this is the inherited nonadaptive order $N^{-1}$; $r=2$ gives $N^{-3/2}$ and is attained by the construction here. For $r=3$ the converse is $N^{-7/4}$, **not** a demonstrated optimal rate. The constant $c_r$ may depend on $r$ and the fixed prior; this fixed-$r$ statement alone cannot be substituted into an $r=r(N)$ claim.

## A bound uniform in the number of batches

To ask how many rounds are *necessary* for $O(N^{-2})$ global risk, we need constants uniform in $r$. The [pointwise Gibbs bound](entropy_budget.md) provides

$$
F_{H_j}(x)\le B\,n_j^2,\qquad
B=(\ln2)^2+2\ln2+2.
$$

For an adaptive experiment the likelihood-score increments form a martingale difference sequence, so total classical Fisher information at each $x$ equals the expectation of the sum of conditional informations. On each branch $\sum_j n_j\le N$; hence

$$
F_{\mathrm{full}}(x)
\le B\,\mathbb E_x\sum_j n_j^2\le BN^2.
$$

The posterior-score identity implies the **round-uniform ceiling**

$$
J_j\le I_0+BN^2.
$$

For $N\ge1$ it follows that $J_{j-1}\le\sqrt{I_0+B}\,N\sqrt{J_{j-1}}$. Combining with the information-area recurrence and defining $A=\sqrt{I_0+B}+\frac12\ln2$, we obtain

$$
J_j\le A N\sqrt{J_{j-1}}.
$$

Iterating this inequality from $J_0=I_0$ yields the *explicit* $r$-uniform estimate

$$
\boxed{
J_r\le (AN)^{2(1-2^{-r})}\,I_0^{2^{-r}}.}
$$

Suppose a family of $r(N)$-batch protocols attains $\sup_x\mathbb E_x(\widehat x-x)^2\le K N^{-2}$ with a single finite constant $K$ independent of $N$. Van Trees then requires $J_{r(N)}\ge N^2/K$. Comparing this demand with the displayed upper bound forces

$$
2^{-r(N)}\ln N=O(1),
\quad\text{or equivalently}\quad
\boxed{r(N)\ge\log_2\ln N-O(1).}
$$

Changing from natural to base-two logarithms alters only the additive constant. This is a **necessary** number of feedback rounds, not an attainable schedule or a hardware-time lower bound.

## Why no full hierarchy is claimed

A tempting extension is to iterate the second-batch block construction, successively enlarging block size as the posterior narrows. But proving an expected-risk upper bound at each stage requires control of exponentially amplified bad-calibration events. A mean-square or merely high-probability bound on the previous estimate does not provide the needed exponential moments; a naive composition could hide logarithmic losses or large rare-event contributions.

The present scientific record therefore proves the complete $r=2$ minimax exponent and the general converse. It does **not** establish a matching $r>2$ minimax hierarchy, an $O(\log\log N)$-round quadratic-risk construction, or optimal leading constants. These are separate potential extensions, not assumptions in either proof above.