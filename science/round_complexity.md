# Fixed-round precision and the converse for quadratic global risk

[Science index](README.md) · [Posterior converse](two_batch_converse.md) · [Thermal information](entropy_budget.md) · [Fixed-round attainment](fixed_round_achievability.md)

The posterior-information converse applies to any prescribed number of Gibbs-preparation batches. The [hedged-array construction](fixed_round_achievability.md) matches its exponent for every **fixed** number of batches. A bound uniform in the number of batches also gives the lower half of the [sharp growing-round depth theorem](growing_round_achievability.md).

For $`r\ge1`$ fixed independently of $`N`$, the complete law is

```math
\boxed{R_r^*(N;[a,b])=\Theta_r\!\left(N^{-(2-2^{1-r})}\right).}
```

The lower bound below permits arbitrary within-batch Hamiltonians, measurements, retained quantum memory and pathwise-valid adaptive allocations. The attaining protocol uses a fixed-gap pilot and finite arrays of differently centered degenerate Gibbs blocks, with every history and block charged. Its constants are allowed to depend on the fixed $`r`$.

## Posterior-information recurrence

Fix the same smooth zero-endpoint prior $`\pi`$ as in the two-batch theorem and define $`J_0=I(\pi)>0`$. After batch $`j`$, let $`\pi_{Y_{\le j}}`$ denote the posterior given the complete revealed energy-label history and write

```math
J_j=\mathbb E[I(\pi_{Y_{\le j}})].
```

The posterior-score identity and the conditional entropy-area budget apply history by history. For batch $`j`$ containing at most $`n_j(y_{\lt j})\le N`$ charged qubits on each branch,

```math
\begin{aligned}
J_j-J_{j-1}
&=\mathbb E\left[\int\pi_{Y_{\lt j}}(x)
F_{H_j(Y_{\lt j})}(x)dx\right]\\
&\le N\ln2\,
\mathbb E[\Vert\pi_{Y_{\lt j}}\Vert_\infty]\\
&\le\frac{N\ln2}{2}\sqrt{J_{j-1}}.
\end{aligned}
```

Thus

```math
\boxed{J_j\le J_{j-1}+\tfrac12 N\ln2\,\sqrt{J_{j-1}}.}
```

For deterministic allocations, $`N`$ in the additive term can be replaced by $`n_j`$. More generally the proof needs only the pathwise $`N`$-qubit cap; the bound is intentionally not optimized over allocations.

## Fixed-$`r`$ global-risk lower bounds

For any fixed $`r`$ independent of $`N`$, induction from $`J_0=O(1)`$ gives

```math
J_r=O_r(N^{\gamma_r}),\qquad
\gamma_0=0,\quad \gamma_j=1+\frac{\gamma_{j-1}}2
=2(1-2^{-j}).
```

Indeed, if $`J_{j-1}=O_r(N^{\gamma_{j-1}})`$ with $`\gamma_{j-1}\lt 2`$, the newly added $`N\sqrt{J_{j-1}}`$ term dominates asymptotically. Van Trees applies to the complete history, giving

```math
\boxed{
R_r^*(N;[a,b])\ge c_r\,N^{-[\,2-2^{1-r}\,]}.}
```

For $`r=1`$ this is the inherited nonadaptive order $`N^{-1}`$; $`r=2`$ gives $`N^{-3/2}`$, attained by the [simpler single-center construction](achievability.md). For $`r=3`$ it gives $`N^{-7/4}`$, and the new [fixed-round construction](fixed_round_achievability.md) attains this and every other fixed-$`r`$ exponent. Thus the sequence $`1,3/2,7/4,15/8,\ldots`$ is sharp. The lower and upper constants may depend on $`r`$; the fixed-$`r`$ law cannot be substituted into an $`r=r(N)`$ claim.

## A bound uniform in the number of batches

To ask how many rounds are *necessary* for $`O(N^{-2})`$ global risk, we need constants uniform in $`r`$. The [pointwise Gibbs bound](entropy_budget.md) provides

```math
F_{H_j}(x)\le B\,n_j^2,\qquad
B=(\ln2)^2+2\ln2+2.
```

For an adaptive experiment the likelihood-score increments form a martingale difference sequence, so total classical Fisher information at each $`x`$ equals the expectation of the sum of conditional informations. On each branch $`\sum_j n_j\le N`$; hence

```math
F_{\mathrm{full}}(x)
\le B\,\mathbb E_x\sum_j n_j^2\le BN^2.
```

The posterior-score identity implies the **round-uniform ceiling**

```math
J_j\le I_0+BN^2.
```

For $`N\ge1`$ it follows that $`J_{j-1}\le\sqrt{I_0+B}\,N\sqrt{J_{j-1}}`$. Combining with the information-area recurrence and defining $`A=\sqrt{I_0+B}+\frac12\ln2`$, we obtain

```math
J_j\le A N\sqrt{J_{j-1}}.
```

Iterating this inequality from $`J_0=I_0`$ yields the *explicit* $`r`$-uniform estimate

```math
\boxed{
J_r\le (AN)^{2(1-2^{-r})}\,I_0^{2^{-r}}.}
```

Suppose a family of $`r(N)`$-batch protocols attains $`\sup_x\mathbb E_x(\widehat x-x)^2\le K N^{-2}`$ with a single finite constant $`K`$ independent of $`N`$. Van Trees then requires $`J_{r(N)}\ge N^2/K`$. Comparing this demand with the displayed upper bound forces

```math
2^{-r(N)}\ln N=O(1),
\quad\text{or equivalently}\quad
\boxed{r(N)\ge\log_2\ln N-O(1).}
```

Changing the inner logarithm base alters only the additive constant. The [growing-round construction](growing_round_achievability.md) matches this lower bound up to an additive constant. The argument counts preparation batches, with one intervening update between consecutive batches.

## Two routes to attainment

A naive iteration of the two-batch, identically centered construction would require control of exponentially amplified bad-calibration events. A mean-square or merely high-probability bound on the preceding estimate does not provide those exponential moments. The [hedged array](fixed_round_achievability.md#refinement-lemma) repairs this inference by spreading block centers with polynomially decreasing multiplicities and retaining all fixed polynomial moments throughout the induction. At deterministic uncertainty width $`w`$ and next-batch allowance $`B`$, it reaches width $`\Theta(\sqrt{w/B})`$ while explicitly including rare histories. The recurrence $`\alpha_{j+1}=(1+\alpha_j)/2`$ for root-error exponents then matches the information converse.

This establishes the complete **fixed-$`r`$** hierarchy with $`r`$-dependent constants. The [separate growing-round schedule](growing_round_achievability.md) chooses interval widths backward from the target precision and bounds the expected loss caused by the first missed interval. Its summable error and qubit costs match the converse when the number of batches grows. Optimal leading constants and thermalization-time efficiency remain open.
