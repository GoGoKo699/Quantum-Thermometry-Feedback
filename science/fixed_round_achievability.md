# Attaining the full fixed-feedback precision hierarchy

[Science index](README.md) · [Model](model.md) · [Matching converse and round-uniform boundary](round_complexity.md) · [Simpler two-batch construction](achievability.md)

## The fixed-round theorem

Fix a nondegenerate finite interval $`[a,b]`$ for $`x=\ln T`$ and an integer $`r\ge1`$ **independent of the total budget** $`N`$. In the full Gibbs-replacement model, there is an explicit $`r`$-batch protocol with at most $`N`$ thermalized qubits on every history and

```math
\sup_{x\in[a,b]}\mathbb E_x[(X_r-x)^2]
\le C_r N^{-\gamma_r},
\qquad \gamma_r=2-2^{1-r},
```

for all sufficiently large $`N`$. The constant may depend on $`r`$, the interval and the fixed pilot gap, but not on $`N`$ or the true temperature. Together with the [posterior-information converse](round_complexity.md#fixed-r-global-risk-lower-bounds), this proves

```math
\boxed{R_r^*(N;[a,b])=\Theta_r\!\left(N^{-(2-2^{1-r})}\right).}
```

In particular, one, two, three and four batches have sharp squared-error exponents $`1,3/2,7/4,15/8`$. Every finite $`r`$ remains below the quadratic exponent. No constant uniform in a growing $`r=r(N)`$ is asserted.

The construction uses a fixed-gap pilot followed by **arrays of differently centered degenerate thermal blocks**. Their group sizes decrease polynomially with the distance from the current estimate. The complete list of blocks is fixed before a batch begins. Summing their binary energy outcomes gives one monotone statistic, which is inverted after that batch ends.

The simpler [two-batch protocol](achievability.md) puts all its second-batch blocks at one estimated center and controls the pilot's exponential moments. Its mean-square bound alone cannot be substituted into that same exponential-moment argument for a third batch. The arrays below instead propagate **every fixed polynomial error moment**; the tail accounting needed for the next refinement is therefore retained.

## A pilot with all fixed moments

Reserve a batch budget $`B`$ and choose one positive gap $`E_0`$. Prepare and energy-measure $`B`$ independent qubits. Their excitation probability is

```math
p_0(x)=\frac{1}{1+\exp(E_0e^{-x})}.
```

On $`[a,b]`$, $`m_0=\inf_x p_0'(x)>0`$. Project the excitation fraction to $`[p_0(a),p_0(b)]`$ and invert $`p_0`$ to obtain a range-valued estimate $`X_1`$. The [pilot calculation](achievability.md#stage-1-fixed-globally-identifiable-pilot) gives

```math
\sup_{x\in[a,b]}\Pr_x(|X_1-x|>u)
\le 2e^{-2Bm_0^2u^2}.
```

For each fixed real $`q>0`$, integration of this tail yields

```math
\sup_x\mathbb E_x|X_1-x|^q
\le q\int_0^\infty 2u^{q-1}e^{-2Bm_0^2u^2}du
=C_q B^{-q/2}.
```

Thus the pilot supplies all fixed moments at the deterministic width $`w_1=B^{-1/2}`$. It also handles every possible pilot count, including zero and $`B`$.

## One refinement: finite array and estimator

Suppose the previous batches have produced $`X\in[a,b]`$ and a deterministic design width $`w`$. For every fixed $`q>0`$, assume

```math
\sup_{x\in[a,b]}\mathbb E_x\left|\frac{X-x}{w}\right|^q
\le C_q<\infty.
```

The constants are uniform over the problem-size sequence under consideration. The design width need not be a confidence radius for an individual record, and the proof does not condition away records outside that width.

Let $`B`$ be the next batch's qubit allowance. For the nontrivial refinement take $`0<w\le1/2`$ and put

```math
k=\lceil1/w\rceil,\qquad
L=\ln(2^k-1),\qquad
M=\lfloor B/k\rfloor,\qquad
J=\lfloor M^{1/8}\rfloor.
```

We prove the lemma for $`M\ge M_0:=2^{16}`$. These deliberately conservative thresholds make the floor and boundary estimates explicit; the finite-budget fallback below defines the protocol outside them. For each integer $`-J\le j\le J`$, select

```math
c_j=X+jw,\qquad
m_j=\left\lfloor\frac{M}{4(1+|j|)^2}\right\rfloor.
```

Prepare $`m_j`$ independent $`k`$-qubit Gibbs blocks with Hamiltonian

```math
H_j=L e^{c_j}\bigl(I-|0^k\rangle\langle0^k|\bigr).
```

The gap and every center depend only on preceding batches. In particular, $`c_j`$ is a selected known number when differentiating a likelihood with respect to the unknown temperature. A binary measurement distinguishes the ground state from the degenerate excited subspace. At log-temperature $`t`$ its excitation probability is

```math
p_j(t)=\sigma\!\left(L(1-e^{c_j-t})\right),
\qquad \sigma(z)=\frac{1}{1+e^{-z}}.
```

Conditional on the preceding history, fresh Gibbs replacement makes all these outcomes independent. Let $`M'=\sum_{j=-J}^Jm_j`$ be the number of blocks and let $`Z`$ be the sum of their binary outcomes. Its known conditional mean is

```math
G_X(t)=\sum_{j=-J}^Jm_jp_j(t).
```

At least $`m_0\ge1`$ blocks are present, so $`G_X`$ is continuous and strictly increasing. Define

```math
\ell_X=\max\{a,X-Jw\},\qquad
h_X=\min\{b,X+Jw\},\qquad I_X=[\ell_X,h_X].
```

The interval has positive length: $`X\in[a,b]`$, $`a<b`$ and $`J\ge1`$. The estimator is

```math
\boxed{
X'=G_X^{-1}\!\left(
\operatorname{clip}_{[G_X(\ell_X),G_X(h_X)]}Z\right),
}
```

where the inverse is restricted to $`I_X`$. In particular, $`X'\in[a,b]`$ for every record. All-zero and all-one counts are clipped to the corresponding endpoint when necessary; no record is postselected.

### Pathwise budget and floor bounds

For the integer array,

```math
\sum_{j\in\mathbb Z}\frac{1}{(1+|j|)^2}
=2\zeta(2)-1<4.
```

Consequently $`M'\le M`$ and $`kM'\le B`$, independently of $`X`$ and the actual outcomes. All low-probability histories use the same prescribed qubit allowance.

Since $`J\le M^{1/8}`$, for every included $`j`$,

```math
\frac{M}{4(1+|j|)^2}\ge\frac{M^{3/4}}{16}\ge2
\quad(M\ge M_0).
```

The elementary inequality $`\lfloor u\rfloor\ge u/2`$ for $`u\ge2`$ therefore gives

```math
m_j\ge\frac{M}{8(1+|j|)^2}.
```

In particular, $`M'\ge m_0\ge M/8`$. Thus $`M'=\Theta(M)`$, with constants independent of the temperature and previous estimate.

## Refinement lemma

**Lemma.** Under the preceding moment assumption, for every fixed $`q>0`$ the estimator satisfies

```math
\sup_{x\in[a,b]}\mathbb E_x|X'-x|^q
\le C'_q\left(\frac{w}{\sqrt M}\right)^q.
```

Here $`C'_q`$ depends on finitely many of the input moment constants, but not on $`B,w,x`$ in the stated regime. Along any sequence with $`w\to0`$ and $`Bw\to\infty`$,

```math
M\asymp Bw,\qquad
\frac{w}{\sqrt M}\asymp\sqrt{\frac{w}{B}}.
```

### A nearby group supplies conditional sensitivity

Fix $`x`$ and write $`D=(x-X)/w`$. First consider preceding histories in

```math
\mathcal A=\{|D|\le M^{1/16}\}.
```

For $`M\ge2^{16}`$, writing $`y=M^{1/16}\ge2`$ gives
$`J=\lfloor y^2\rfloor\ge y+1`$. Hence $`x\in I_X`$ on $`\mathcal A`$, and there is an integer $`j_*`$ with

```math
|j_*-D|\le\tfrac12,\qquad |j_*|\le J,\qquad
|c_{j_*}-x|\le w/2.
```

The floor estimate then gives, with a numerical constant,

```math
m_{j_*}\ge\frac{M}{32(1+|D|)^2}.
```

For $`w\le1/2`$ and $`k=\lceil1/w\rceil`$,

```math
\frac{\ln2}{2}\le Lw\le2\ln2.
```

Whenever $`|t-x|\le w`$, the distance $`|c_{j_*}-t|\le2w\le1`$ keeps $`e^{c_{j_*}-t}`$ between $`e^{-1}`$ and $`e`$, and the magnitude of the logit is at most $`4e\ln2`$. Therefore

```math
p_{j_*}'(t)
=L e^{c_{j_*}-t}p_{j_*}(t)(1-p_{j_*}(t))
\ge\frac{c_*}{w},
\qquad
c_*:=\frac{\ln2}{2e}\,\sigma'(4e\ln2)>0.
```

All other group derivatives are nonnegative. With $`a_*=c_*/32`$, integration on either side of $`x`$ proves

```math
|G_X(x+u)-G_X(x)|
\ge\frac{a_*M|u|}{w(1+|D|)^2},\qquad |u|\le w,
```

whenever $`x+u\in I_X`$. No global linearization of the thermal likelihood is being assumed.

### Local concentration and the large-error tail

On $`\mathcal A`$, if $`x+u\in I_X`$, monotonicity and clipping imply

```math
\{X'>x+u\}\subseteq\{Z>G_X(x+u)\}\qquad(u>0).
```

If $`x+u\notin I_X`$, the corresponding upward-deviation event is empty. The downward event is handled in the same way. Hoeffding's inequality for the $`M'`$ independent, not necessarily identically distributed binary variables, using $`M'\le M`$, yields

```math
\Pr_x(|X'-x|>u\mid X)
\le 2\exp\!\left[-\frac{cM u^2}{w^2(1+|D|)^4}\right],
\qquad 0<u\le w,
```

where $`c=2a_*^2>0`$ may be decreased without changing the proof. Conditioning only on $`X`$ is sufficient because the design and all fresh block laws are functions of $`X`$ and deterministic parameters; conditioning on the full history gives the same bound.

For all preceding histories, the estimator's designed range gives the deterministic bound

```math
|X'-x|\le w(J+|D|)=:A_D.
```

For $`u>w`$, the probability is at most its bound at $`u=w`$. Integrating the tail identity $`\mathbb E Y^q=q\int_0^\infty u^{q-1}\Pr(Y>u)du`$ for $`Y\ge0`$ therefore gives, on $`\mathcal A`$,

```math
\begin{aligned}
\mathbb E_x[|X'-x|^q\mid X]
&\le C_q\left(\frac{w}{\sqrt M}\right)^q(1+|D|)^{2q}\\
&\quad+2A_D^q\exp\!\left[-\frac{cM}{(1+|D|)^4}\right].
\end{aligned}
```

The first term follows by integrating the Gaussian bound over $`u\in(0,\infty)`$; extending that integral only enlarges it. The second bounds the portion above $`w`$ using the deterministic cap. This also covers the case $`A_D\le w`$, when that portion vanishes.

### Averaging every preceding history

Set $`v=w/\sqrt M`$. The first term, divided by $`v^q`$ and averaged on $`\mathcal A`$, is bounded by the assumed $`2q`$-th normalized moment. For the second term, on that same event,

```math
\frac{A_D}{v}\le2M^{5/8},\qquad
\frac{M}{(1+|D|)^4}\ge\frac{M^{3/4}}{16}.
```

Its averaged normalized contribution is thus at most

```math
C_q M^{5q/8}e^{-cM^{3/4}/16},
```

which is bounded uniformly over $`M\ge M_0`$.

It remains to include the histories in $`\mathcal A^c`$. The deterministic bound and $`J\le M^{1/8}`$ imply

```math
\begin{aligned}
\mathbb E_x\!\left[
\left|\frac{X'-x}{v}\right|^q;\mathcal A^c\right]
&\le C_q M^{q/2}
\left(M^{q/8}\Pr_x(\mathcal A^c)
+\mathbb E_x[|D|^q;\mathcal A^c]\right).
\end{aligned}
```

For any fixed $`K>q`$, the input moment assumption and $`|D|>M^{1/16}`$ give

```math
\Pr_x(\mathcal A^c)\le C_K M^{-K/16},\qquad
\mathbb E_x[|D|^q;\mathcal A^c]
\le C_K M^{-(K-q)/16}.
```

Consequently the entire bad-history contribution is at most

```math
C_{q,K}\left(M^{(10q-K)/16}+M^{(9q-K)/16}\right).
```

Choose, for example, $`K=12q+2`$. Both exponents are negative, so this contribution is uniformly bounded. Combining the good and bad parts proves the lemma for every fixed $`q>0`$. No assumption about exponential moments of the preceding estimate has entered the argument. $`\square`$

## Fixed-round induction and complete protocol

For fixed $`r`$ and $`N\ge r`$, take the deterministic per-batch allowance

```math
B=\lfloor N/r\rfloor.
```

Use the pilot in batch one. Define the design widths, independently of all records, by

```math
w_j=B^{-\alpha_j},\qquad
\alpha_1=\tfrac12,\qquad
\alpha_{j+1}=\frac{1+\alpha_j}{2}.
```

At each batch $`j+1`$, apply the array with allowance $`B`$, previous estimate $`X_j`$ and width $`w_j`$. If the finite design conditions $`w_j\le1/2`$ and $`\lfloor B/\lceil1/w_j\rceil\rfloor\ge M_0`$ are not met, use $`B`$ ordinary fixed-gap qubits in that batch, ignore their outcomes and retain $`X_j`$. This fallback makes every small-budget protocol well defined without discarding a history or exceeding $`rB\le N`$; it is not used in the large-$`N`$ proof.

For each fixed stage, $`\alpha_j<1`$. As $`B\to\infty`$,

```math
w_j\to0,\qquad
M_j:=\left\lfloor\frac{B}{\lceil1/w_j\rceil}\right\rfloor
\asymp B^{1-\alpha_j}\to\infty.
```

Thus all $`r-1`$ refinements meet the lemma's conditions once $`N`$ exceeds a finite, $`r`$-dependent threshold. The pilot has every fixed normalized moment. If stage $`j`$ has that property, the lemma gives it at scale

```math
\frac{w_j}{\sqrt{M_j}}
\asymp B^{-(1+\alpha_j)/2}=w_{j+1}.
```

The constants in these comparisons are uniform in $`B`$ for that fixed stage. The induction is not circular: to prove the stage-$`j+1`$ bound for one $`q`$, the argument uses only finitely higher moments, such as orders $`2q`$ and $`12q+2`$, at the **preceding** stage. The preceding-stage assertion supplies every fixed moment. Starting from the pilot and iterating finitely many times therefore proves all fixed moments at every fixed stage.

Solving the width recurrence gives

```math
\alpha_j=1-2^{-j},\qquad
\sup_x\mathbb E_x|X_r-x|^q\le C_{r,q}B^{-q(1-2^{-r})}.
```

For $`q=2`$ and fixed $`r`$, $`B\asymp_r N`$, which proves the stated upper bound. The remaining finitely many integer budgets $`r\le N<N_r`$ have range-valued error at most $`(b-a)^2`$. Enlarging $`C_r`$ if desired extends the displayed upper inequality to all $`N\ge r`$. No asymptotic constant is claimed to be small.

## Resources and the fixed-round boundary

In a refinement whose preceding width is $`w=B^{-\alpha}`$, with fixed $`1/2\le\alpha<1`$:

| Resource or parameter | Explicit order and charge |
|---|---|
| Qubits in one degenerate block | $`k=\lceil1/w\rceil=\Theta(B^\alpha)`$ |
| Independently prepared blocks and binary energy outcomes | $`M'=\Theta(M)=\Theta(B^{1-\alpha})`$ |
| Distinct known block centers | $`2J+1=O(B^{(1-\alpha)/8})`$ |
| Total thermalized qubits in the batch | $`kM'\le B`$ on every history |
| Spread of centers around the preceding estimate | $`Jw=O(B^{(1-9\alpha)/8})\to0`$ |
| Gap of each block | $`Le^{c_j}=\Theta(k)`$, uniformly over histories for sufficiently large $`B`$ |
| Inter-batch Hamiltonian updates | At most $`r-1`$; none inside a batch |

The center-spread statement follows because $`\alpha\ge1/2`$. Since $`X\in[a,b]`$, for sufficiently large $`B`$ all centers lie in $`[a-1,b+1]`$, which justifies the history-uniform gap order. The construction still uses growing gaps and highly degenerate, many-body projector Hamiltonians. Energy readout is the ideal binary ground-versus-excited measurement allowed by the model. The known function $`G_X`$ and its monotone inverse specify the classical estimator; an optimized finite-precision implementation or computation-time bound is not part of this theorem.

Only a classical estimate must persist between batches. Retained quantum memory is unnecessary for attainment, although the converse permits it. Preparing all blocks at once, or independently in a fixed preannounced list, gives the same product Gibbs experiment. Every block and every unfavorable record is included in the qubit budget and error average.

Finally, fixed-$`r`$ constants and moment orders may grow with $`r`$. Equal allocation uses $`B=\lfloor N/r\rfloor`$, and the proof requires each refinement's $`M_j`$ to diverge. Substituting $`r=r(N)`$ into this argument does **not** establish an $`O(\log\log N)`$-batch, $`O(N^{-2})`$-risk schedule. The [round-uniform converse](round_complexity.md#a-bound-uniform-in-the-number-of-batches) still supplies only the necessity $`r(N)\ge\log_2\ln N-O(1)`$ for that stronger target. Its sufficiency, optimal leading constants, local-interaction realization and thermalization-time costs remain outside the established result.
