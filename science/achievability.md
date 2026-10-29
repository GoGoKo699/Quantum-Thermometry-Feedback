# A two-batch thermometer attaining $`N^{-3/2}`$ global risk

[Science index](README.md) · [Model](model.md) · [Lower bound](two_batch_converse.md)

## Statement

On every fixed interval $`a\le x=\ln T\le b`$, there is a fully specified **two-batch** classical-feedback protocol using at most $`N`$ thermalized qubits on every branch and a range-valued estimator such that, for some interval-dependent $`K\lt \infty`$,

```math
\sup_{x\in[a,b]}\mathbb E_x[(\widehat x-x)^2]
\le K N^{-3/2}\quad\text{for all sufficiently large }N.
```

The protocol does not know $`x`$ in advance and does not ignore unfavorable calibration outcomes. It uses fixed-gap calibration qubits followed by independently thermalized, equally tuned $`k`$-qubit blocks, with **no intermediate retuning inside the second batch**.

## Stage 1: fixed, globally identifiable pilot

Choose a fixed, positive energy gap $`E_0`$ independent of $`N`$ and $`x`$. Thermalize

```math
n_1=\lfloor N/2\rfloor
```

independent qubits with Hamiltonian $`E_0|1\rangle\langle1|`$, and measure their energy. At $`x=\ln T`$, each excitation is Bernoulli with

```math
p_0(x)=\frac{1}{1+\exp(E_0e^{-x})}.
```

On the compact interval, $`p_0`$ is smooth, strictly increasing, and its derivative has a positive lower bound $`m_0=\inf_{[a,b]}p_0'(x)>0`$. If $`\bar B`$ is the observed excitation fraction, first project it to $`[p_0(a),p_0(b)]`$, then set

```math
X_0=p_0^{-1}\!\left(
\mathrm{clip}_{[p_0(a),p_0(b)]}\bar B\right).
```

Projection cannot increase the distance to the true $`p_0(x)`$. The inverse is $`1/m_0`$-Lipschitz on the interval, so Hoeffding's inequality gives, uniformly in $`x`$,

```math
\boxed{\Pr_x(|X_0-x|>u)
\le2\exp(-2n_1m_0^2u^2).}
```

In particular, $`X_0\in[a,b]`$ for every observed pilot record, including all-zero and all-one counts. Its calibration errors are uniformly sub-Gaussian at scale $`N^{-1/2}`$.

## Stage 2: retuned, degenerate thermal blocks

Choose

```math
k=\lfloor\sqrt N\rfloor,\qquad
M=\left\lfloor\frac{N-n_1}{k}\right\rfloor,\qquad
g=2^k-1,\qquad L=\ln g.
```

For sufficiently large $`N`$, $`k\asymp\sqrt N`$, $`M\asymp\sqrt N`$, and $`L\asymp k`$. Given the *single* first-batch estimate $`X_0`$, all $`M`$ blocks receive the same $`k`$-qubit Hamiltonian

```math
H_{X_0}=E_{X_0}(I-|0^k\rangle\langle0^k|),
\qquad E_{X_0}=L e^{X_0}.
```

One state has energy zero and the $`g`$ other orthogonal states have energy $`E_{X_0}`$. Measure the binary excited/ground indicator of each completely thermalized block. The $`M`$ outcomes are conditionally i.i.d. Bernoulli with

```math
p=\sigma(z),\qquad
\sigma(z)=\frac1{1+e^{-z}},\qquad
z=L(1-e^{X_0-x}).
```

For perfect pilot centering, $`X_0=x`$ and $`p=1/2`$, providing Fisher information of order $`L^2`$ per block. Importantly, the centering error is never assumed to be zero.

## Explicit estimator, including endpoints

Let $`S\in\{0,\ldots,M\}`$ be the second-batch excitation count. Use the smoothed logit

```math
\widetilde z=\ln\frac{S+1}{M-S+1}.
```

For the known value of $`X_0`$, the physical interval $`x\in[a,b]`$ corresponds to $`z\in[z_a,z_b]`$, where $`z_v=L(1-e^{X_0-v})`$. Project $`\widetilde z`$ onto this $`z`$-interval and write the result as $`\widehat z`$. Return

```math
\boxed{\widehat x=X_0-\ln(1-\widehat z/L).}
```

The clipping makes the inverse well-defined and ensures $`\widehat x\in[a,b]`$, including at $`S=0`$ or $`S=M`$.

For fixed $`X_0`$, the inverse map from $`z`$ to $`x`$ has derivative

```math
\frac{dx}{dz}=\frac{e^{x-X_0}}L,
```

whose magnitude is bounded by $`e^{b-a}/L`$ over the physical interval. Therefore clipping and the mean value theorem imply

```math
|\widehat x-x|\le\frac{e^{b-a}}L|\widetilde z-z|.
```

## Uniform binomial-logit lemma

**Lemma.** For every $`M\ge1`$, $`0\lt p\lt 1`$, and $`S\sim\mathrm{Bin}(M,p)`$,

```math
\boxed{
\mathbb E\left[
\left(\ln\frac{S+1}{M-S+1}-\ln\frac{p}{1-p}\right)^2\right]
\le\frac{200}{Mp(1-p)}.}
```

The bound is deliberately loose; its uniformity for small $`p`$ and $`1-p`$ is what prevents ignored failure branches.

**Proof.** Put $`\mu=Mp`$ and $`A=\ln[(S+1)/\mu]`$. First we establish $`\mathbb E A^2\le45/\mu`$.

For $`\mu\le1`$, $`S+1\ge1`$ and
$`0\le A\le\ln(1/\mu)+S`$. Since $`\mathbb E S^2\le\mu+\mu^2`$ and $`\mu\ln^2(1/\mu)\le4/e^2`$, the estimate $`\mathbb EA^2\le6/\mu`$ follows.

For $`\mu\ge1`$ split into three regions. When $`S+1\ge\mu`$, use $`\ln u\le u-1`$ to bound the contribution by
$`\mathbb E(S+1-\mu)^2/\mu^2\le2/\mu`$.
When $`S+1\lt \mu`$ but $`S\ge\mu/2`$, use $`|\ln[(S+1)/\mu]|\le2|S+1-\mu|/\mu`$ to bound this contribution by $`8/\mu`$.
On the remaining event $`S\lt \mu/2`$, Chernoff gives probability at most $`e^{-\mu/8}`$, and the absolute log is at most $`\ln\mu`$. Since $`\ln^2\mu\le\mu`$ and $`\sup_{\mu\ge1}\mu^2e^{-\mu/8}=256/e^2\lt 35`$, that contribution is at most $`35/\mu`$. The sum is at most $`45/\mu`$.

Set $`q=(S+1)/(M+2)`$. The deterministic difference from $`A`$ to $`\ln(q/p)`$ is $`\ln(1+2/M)`$, whose square is at most $`4/M^2`$. By $`(u-v)^2\le2u^2+2v^2`$,

```math
\mathbb E[\ln(q/p)^2]
\le\frac{90}{Mp}+\frac8{M^2}
\le\frac{98}{Mp}.
```

Apply the identical argument to $`M-S`$ and $`1-p`$, obtaining $`\mathbb E[\ln((1-q)/(1-p))^2]\le98/[M(1-p)]`$. Subtract the two log expressions and use $`(u-v)^2\le2u^2+2v^2`$ again:

```math
\mathbb E[(\mathrm{logit}q-\mathrm{logit}p)^2]
\le\frac{196}{Mp(1-p)}
\le\frac{200}{Mp(1-p)}.
```

This proves the lemma. $`\square`$

## Charge the entire pilot-error distribution

Conditional on $`X_0`$, the inverse-Lipschitz bound and the lemma yield

```math
\mathbb E_x[(\widehat x-x)^2\mid X_0]
\le\frac{200e^{2(b-a)}}{M L^2 p(1-p)}.
```

Because $`p=\sigma(z)`$,

```math
\frac1{p(1-p)}=2+e^z+e^{-z}
\le4e^{|z|}.
```

Writing $`\delta=X_0-x`$, note that $`|\delta|\le b-a`$ and

```math
|z|=L|1-e^\delta|
\le L e^{b-a}|\delta|.
```

Thus the full unconditional error obeys

```math
\mathbb E_x[(\widehat x-x)^2]
\le\frac{800e^{2(b-a)}}{M L^2}
\mathbb E_x[e^{L e^{b-a}|X_0-x|}].
```

The uniform pilot tail bound shows that the exponential moment is bounded independently of $`N`$: for $`s=L e^{b-a}`$,

```math
\begin{aligned}
\mathbb E[e^{s|\delta|}]
&=1+s\int_0^\infty e^{st}\Pr(|\delta|>t)\,dt\\
&\le 1+2s\int_0^\infty e^{st-2n_1m_0^2t^2}\,dt.
\end{aligned}
```

Here $`s/\sqrt{n_1}`$ is uniformly bounded because $`L=O(\sqrt N)`$ and $`n_1=\Theta(N)`$. Change variables $`u=\sqrt{n_1}t`$ to see the final integral times $`s`$ is bounded by a constant depending only on the fixed interval and pilot gap. No calibration failure is discarded or postselected.

It follows that

```math
\sup_{x\in[a,b]}\mathbb E_x[(\widehat x-x)^2]
=O\!\left(\frac1{M L^2}\right)=O(N^{-3/2}).
```

Together with the [universal converse](two_batch_converse.md), this proves the **sharp two-batch law**.

## Implementation and mathematical limits

The construction pays $`n_1+Mk\le N`$ on every branch. It requires one inter-batch classical computation and a Hamiltonian whose excited subspace has degeneracy $`2^k-1`$. Its highest gap grows as $`E_{X_0}=\Theta(k)`$ on a fixed positive temperature interval. No $`N`$-independent energy norm, bounded-degree interaction, thermalization-time bound, or controlled-bath circuit is asserted. The ideal blocks are a theoretical access construction; their probability distribution is classical.

[Reproduce finite numerical checks](../verification/README.md) · [Interpretation](interpretation.md).