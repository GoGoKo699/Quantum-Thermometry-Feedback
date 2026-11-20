# Quadratic global thermometry with sharp feedback depth

[Science index](README.md) · [Access model](model.md) · [Feedback-depth converse](round_complexity.md)

For an initially unknown temperature, the thermometer has to locate the narrow temperature window in which a large Gibbs probe is sensitive. A sequence of nested intervals does this with an optimal number of feedback batches. When an interval loses the true temperature, the estimate remains in the preceding, wider interval. This bounds the effect of each failed refinement on the final error, even for records that leave the narrowest intervals.

## Result

Let $`x=\ln T`$ range over a fixed interval $`[a,b]`$ with $`a\lt b`$ and finite endpoints. The [Gibbs-replacement model](model.md) charges all qubits on every record, and Gibbs block Hamiltonians may change only between batches. For a budget $`N\ge1`$, there is a deterministic allocation and an explicit protocol using

```math
r(N)=\log_2\ln N+O(1)\quad(N\to\infty)
```

batches with

```math
\sup_{x\in[a,b]}\mathbb E_x[(\widehat x-x)^2]\le C_{a,b}N^{-2}.
```

The constant is independent of $`N`$, the number of batches and the true temperature. The result holds both for the degenerate Gibbs blocks used in the [fixed-round construction](fixed_round_achievability.md) and for the two-body star blocks described below. In each case, the readout gives one binary outcome per block, and outcomes within a batch are used only after all its Hamiltonians have been set.

The [existing converse](round_complexity.md#a-bound-uniform-in-the-number-of-batches) gives $`r(N)\ge\log_2\ln N-O(1)`$ for any protocol whose worst-case risk is bounded by a constant times $`N^{-2}`$. Its pointwise information ceiling also gives the risk lower bound $`\Omega(N^{-2})`$. Thus the quadratic rate is sharp, with a necessary and sufficient batch count up to an additive constant. A schedule with $`r\ge1`$ batches allows $`r-1`$ Hamiltonian updates.

## One Gibbs batch refines a known interval

Put $`D=(b-a)/2`$. Suppose the retained interval $`I\subseteq[a,b]`$ has midpoint $`c`$ and half-width at most $`w\in(0,D]`$. Choose

```math
k=\max\{2,\lceil 1/w\rceil\},\qquad L=\ln(2^k-1),\qquad
H=L e^c\bigl(\mathbb{1}-|0^k\rangle\langle0^k|\bigr).
```

The outcome indicating excitation is Bernoulli with known response at log-temperature $`t`$,

```math
p(t)=\sigma\bigl(L(1-e^{c-t})\bigr),\qquad
\sigma(z)=(1+e^{-z})^{-1}.
```

The response is strictly increasing. Let $`K_D=\max\{2D,1+D\}`$, so $`1\le kw\le K_D`$. Since $`k\ge2`$, we have $`\tfrac12\ln2\le Lw\le K_D\ln2`$. For $`t\in I`$, the logit has magnitude at most $`K_De^D\ln2`$, and $`e^{c-t}\ge e^{-D}`$. Thus

```math
p'(t)=L e^{c-t}\sigma'\bigl(L(1-e^{c-t})\bigr)\ge m_D/w,\qquad
m_D=\tfrac12(\ln2)e^{-D}\sigma'(K_De^D\ln2)\gt0.
```

For a requested radius $`v\in(0,w]`$ and miss probability $`\eta\in(0,1)`$, energy-measure $`M`$ fresh identical blocks in one batch, with

```math
M=\left\lceil\frac{(w/v)^2}{2m_D^2}\ln\frac2\eta\right\rceil.
```

Clip their empirical excitation fraction to $`p(I)`$, then invert the known response on $`I`$ to obtain $`X'`$. The inverse of the singleton image is understood to give that singleton. Set

```math
I'= I\cap[X'-v,X'+v].
```

Every possible count gives a nonempty $`I'\subseteq I`$ of half-width at most $`v`$, because $`X'\in I`$. If the true $`x`$ lies in $`I`$, clipping and the derivative bound give $`|X'-x|\le(w/m_D)|\overline B-p(x)|`$, where $`\overline B`$ is the empirical fraction. Conditional on the previous record, fresh replacement makes the $`M`$ outcomes independent, so Hoeffding's inequality gives

```math
\Pr_x(x\notin I'\mid I,\text{ previous outcomes})\le
2\exp\bigl[-2M(m_Dv/w)^2\bigr]\le\eta
\qquad(x\in I).
```

This estimate includes endpoint counts. There is no conditioning on a successful readout when the overall risk is evaluated. Rounding both $`k`$ and $`M`$ costs

```math
kM\le C_D\frac{w}{v^2}\ln(2/\eta),\qquad
C_D=K_D\left(\frac{1}{\ln2}+\frac{1}{2m_D^2}\right).
```

Indeed, the ceiling adds at most $`K_D/w`$ qubits, which is bounded by $`K_D(w/v^2)\ln(2/\eta)/\ln2`$.

## Allocate radii and qubits backward from the target precision

Let $`d=\ln4`$, choose a constant $`A\ge1`$ below, and put

```math
W_h=A\exp(2^h+dh),\qquad
R=\min\{h\in\mathbb Z_{\ge0}:W_h\ge ND\},\qquad
\eta_h=2^{-h}(W_0/W_h)^2\quad(h\ge1).
```

Start with $`I=[a,b]`$ and visit $`h=R,R-1,\ldots,1`$. At stage $`h`$ use the one-batch refinement with

```math
w=\min(D,W_h/N),\qquad v=W_{h-1}/N,\qquad \eta=\eta_h.
```

Choosing the smallest depth that covers the initial interval gives $`v\le w`$ at the first stage, and monotonicity of the $`W_h`$ gives it thereafter. The preceding interval always has half-width at most $`w`$. The block size, repetition count and target widths are fixed in advance. For the degenerate blocks, the gap is recalibrated to the midpoint of the interval retained from previous batches. The final estimate $`\widehat x`$ is the midpoint of the final interval. If $`R=0`$, the original midpoint already satisfies $`|\widehat x-x|\le W_0/N`$.

The identity controlling the budget is

```math
\frac{W_h}{W_{h-1}^2}=\frac{16}{A}4^{-h}.
```

It cancels the doubly exponential part of the widths. Each stage costs at most $`C_DN(W_h/W_{h-1}^2)\ln(2/\eta_h)`$ qubits, including the first stage where $`w`$ may be smaller than $`W_R/N`$. The total is at most

```math
\frac{16C_DN}{A}\sum_{h=1}^\infty 4^{-h}
\bigl[2(2^h-1)+5h\ln2+\ln2\bigr]
=\frac{16C_DN}{A}\left(2+\tfrac{20}{9}\ln2+\tfrac{\ln2-2}{3}\right).
```

Choose $`A=\max\{1,16C_D(2+\tfrac{20}{9}\ln2+\tfrac{\ln2-2}{3})\}`$. This charges no more than $`N`$ qubits on every history. As $`N`$ grows, minimality means $`2^R+dR\ge\ln(ND/A)`$ and $`2^{R-1}+d(R-1)\lt\ln(ND/A)`$. Since $`R\le2^R`$, these inequalities give $`R=\log_2\ln N+O(1)`$.

## All records contribute to the risk

If every interval contains $`x`$, the final squared error is at most $`(W_0/N)^2`$. If the first exit occurs at stage $`h`$, the pre-refinement interval contained $`x`$. The final estimate lies in this same interval regardless of what happens afterward. Therefore its squared error on that event is at most $`4(W_h/N)^2`$. The probability of a first exit at $`h`$ is at most $`\eta_h`$, by averaging the one-batch guarantee over the histories that had retained $`x`$ up to that stage. The disjoint first-exit events account for every record, and yield

```math
\sup_{x\in[a,b]}\mathbb E_x[(\widehat x-x)^2]
\le \frac{W_0^2}{N^2}+4\sum_{h=1}^{R}\eta_h\frac{W_h^2}{N^2}
\le \frac{5W_0^2}{N^2}.
```

An exit from a broad interval must be very rare, while an exit from an already narrow interval can be more frequent. The allocated probabilities match these different costs. The fixed-round construction addresses a different regime, where the target risk exponent depends on a fixed integer $`r`$ and the proof propagates error moments between refinements.

## Two-body star blocks and single-spin readout

The argument needs a Bernoulli response with known derivative at least a constant times $`1/w`$ throughout the current interval. A diagonal two-body star supplies that response using the same $`k`$ qubits per block. Let $`P=|1\rangle\langle1|`$ act on the hub, and let $`Q_i=|1\rangle\langle1|`$ act on leaf $`i`$, for $`i=1,\ldots,k-1`$. With a fixed $`u\gt0`$ and $`g(u)=\ln2-\ln(1+e^{-u})`$, take

```math
H_\star=e^c\left[(k-1)g(u)P+u(\mathbb{1}-P)\sum_{i=1}^{k-1}Q_i\right].
```

The two conditional partition functions give the hub's log-odds for outcome $`P=1`$ at log-temperature $`t=c+\delta`$:

```math
z(t)=(k-1)\left[g(ue^{-\delta})-e^{-\delta}g(u)\right].
```

In particular $`z(c)=0`$. Its derivative is

```math
z'(t)=(k-1)e^{-\delta}\left[g(u)-\frac{u}{1+\exp(ue^{-\delta})}\right].
```

Choose $`u=e^D(2D+10)`$, which ensures $`u e^{-ue^{-D}}\le g(u)/2`$: the left side is $`(2D+10)e^{-D-10}\le10e^{-10}`$, while $`g(u)\ge g(10)`$. For $`|\delta|\le D`$,

```math
\tfrac14 k e^{-D}g(u)\le z'(t)\le k e^Dg(u),
```

where the lower bound uses $`k-1\ge k/2`$. On $`I`$ the logit therefore obeys $`|z(t)|\le K_De^Dg(u)`$. The hub response $`p_\star(t)=\sigma(z(t))`$ obeys the required derivative bound with the explicit constant

```math
m_{\star,D}=\tfrac14 e^{-D}g(u)\sigma'\bigl(K_De^Dg(u)\bigr)\gt0.
```

Replace $`m_D`$ by $`m_{\star,D}`$ throughout the schedule and measure the hub alone after each Gibbs replacement. All leaves still count as thermalized qubits. At fixed $`k`$, retuning multiplies the fields and couplings by the same factor $`e^c`$, fixed before the batch is observed.

The interaction order is two and the center has $`k-1`$ incident couplings. The leaf couplings are bounded on the fixed temperature interval, while the accumulated central field grows linearly with $`k`$. Both realizations assume complete Gibbs equilibration, with no bound on the time required. The constants above give a uniform asymptotic guarantee and are conservative for finite $`N`$.

## Relation to earlier thermometry protocols

[Mehboudi et al. (2022)](https://doi.org/10.1103/PhysRevLett.128.130502) supply the Bayesian adaptive scheme, the degenerate Gibbs block and the sensitivity-area starting point. Their adaptive examples tune equal-size groups and demonstrate saturation as group size varies with sufficiently many groups. Here the group sizes and repetition counts are scheduled to establish the least asymptotic number of feedback batches at a fixed total qubit budget, for worst-case risk on a compact interval. The two-body star Hamiltonian is the family in Eq. (13) of [Abiuso et al. (2024)](https://doi.org/10.1088/2058-9565/ad37d3), up to an additive scalar. Their Appendix D.1 gives the conditional sector partition functions, Sec. 3.3 proposes the central-spin measurement, and Sec. 3.4 reports quadratic local sensitivity with bounded pair couplings and a linear hub field. The calculation here uses exact balancing at the chosen center to supply an explicit derivative bound throughout the current interval. See the [comparison by model and result](../references/RELATED_WORK.md).
