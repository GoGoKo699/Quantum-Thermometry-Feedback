# Universal two-batch minimax converse

[Science index](README.md) · [Model](model.md) · [Entropy-area lemma](entropy_budget.md) · [Matching upper bound](achievability.md)

## Statement

Fix $a<b$ and the full Gibbs-replacement/one-inter-batch-feedback model of [the model](model.md). For some $c=c(a,b)>0$ and all sufficiently large integer budgets $N$,

$$
\boxed{R_2^*(N;[a,b])\ge c N^{-3/2}.}
$$

The bound holds for arbitrary within-batch many-body Hamiltonians, energy or non-energy measurements, ancillas, retained quantum memory, adaptive second-round qubit allocations satisfying the **pathwise** $N$-qubit cap, and arbitrary biased estimators. The first Hamiltonian and any initial random seed must be independent of the unknown temperature. The second Hamiltonian may depend on the first classical record.

## A fixed global prior

Choose the normalized smooth density

$$
\pi(x)=
\begin{cases}
\frac{2}{b-a}\sin^2\!\left(\frac{\pi(x-a)}{b-a}\right),&a\le x\le b,\\
0,&\text{otherwise.}
\end{cases}
$$

It vanishes at both endpoints, is positive in the interior and has

$$
\|\pi\|_\infty=\frac{2}{b-a},\qquad
I(\pi):=\int_a^b\frac{\pi'(x)^2}{\pi(x)}\,dx
=\frac{4\pi^2}{(b-a)^2}=:I_0.
$$

For any estimator, minimax squared risk dominates the Bayes risk under this one fixed-width prior. Using this prior avoids pretending that the experimenter is initially localized to a shrinking window.

## Posterior peak lemma

Let $q$ be a differentiable probability density on $[a,b]$, with $q(a)=q(b)=0$ and finite density Fisher information

$$
I(q)=\int_a^b \frac{q'(x)^2}{q(x)}\,dx.
$$

If $m=\|q\|_\infty$, the curve must rise from zero to $m$ and return to zero. Therefore

$$
2m\le \int_a^b|q'(x)|\,dx
\le\left(\int_a^b \frac{q'(x)^2}{q(x)}dx\right)^{1/2}
\left(\int_a^b q(x)dx\right)^{1/2}
=\sqrt{I(q)}.
$$

Thus

$$
\boxed{\|q\|_\infty\le\tfrac12\sqrt{I(q)}.}
$$

This is a global Sobolev/Cauchy bound on the posterior *density*, not a claim about local Gaussian approximations.

## Information after the first batch

By [classical sufficiency](model.md), it is legitimate to reveal each Gibbs energy-basis label. Denote the first record by $Y$, with likelihood $p_1(y|x)$ and posterior $\pi_y(x)$. Conditional on any first-round exogenous randomization we can make the same calculation, then average.

For the joint density $\pi(x)p_1(y|x)$,

$$
\partial_x\ln\pi_y(x)=\partial_x\ln\pi(x)+\partial_x\ln p_1(y|x).
$$

The cross term in the expected squared score is zero because the normalized likelihood has $\mathbb E[\partial_x\ln p_1(Y|x)\mid x]=0$. Hence the exact posterior-score identity

$$
\begin{aligned}
J_1:=\mathbb E_Y[I(\pi_Y)]
&=I_0+\int_a^b\pi(x)F_{H_1}(x)\,dx\\
&\le I_0+n_1\ln2\,\|\pi\|_\infty\\
&\le I_0+N\ln2\,\|\pi\|_\infty
=O(N).
\end{aligned}
$$

Here $n_1$ is the first-batch qubit count, possibly fixed by an exogenous random seed; its total information follows from the full Gibbs state entropy budget, not from an assumption of independent qubits.

## Conditional second-batch bound

For each first record $y$, the selected next Hamiltonian $H_y$ is held fixed when differentiating the parameter. It acts on $n_2(y)\le N$ charged qubits. Its posterior-averaged Fisher information obeys

$$
\begin{aligned}
\int_a^b\pi_y(x)F_{H_y}(x)\,dx
&\le \|\pi_y\|_\infty
\int_a^b F_{H_y}(x)\,dx\\
&\le n_2(y)\ln2\,\|\pi_y\|_\infty\\
&\le\tfrac12 N\ln2\,\sqrt{I(\pi_y)}.
\end{aligned}
$$

Average over $Y$ and use concavity of the square root:

$$
\mathbb E_Y\int_a^b\pi_Y(x)F_{H_Y}(x)dx
\le\tfrac12 N\ln2\,\sqrt{\mathbb E I(\pi_Y)}
=\tfrac12N\ln2\,\sqrt{J_1}.
$$

For the full two-stage likelihood (including the parameter-dependent distribution of the first record), the cross term between the first score and the conditional second score also vanishes. Consequently the total prior-averaged classical Fisher information is bounded by

$$
\boxed{J_2\le J_1+\tfrac12N\ln2\,\sqrt{J_1}
=O(N^{3/2}).}
$$

For deterministic batch sizes, the displayed bound can retain $n_2$ instead of $N$. The pathwise argument intentionally covers random allocations without silently upgrading an expected-size budget.

## Turning information into global error

For a smooth zero-endpoint prior, integration by parts yields the van Trees (Bayesian Cramér–Rao) inequality

$$
\int_a^b\pi(x)\mathbb E_x[(\widehat x-x)^2]dx
\ge \frac{1}{I_0+\int_a^b\pi(x)F_{\rm full}(x)\,dx}
=\frac1{J_2}.
$$

The integration by parts does not assume unbiasedness; the endpoint term vanishes because $\pi(a)=\pi(b)=0$. Applying the derived $J_2$ bound gives

$$
\sup_{x\in[a,b]}\mathbb E_x[(\widehat x-x)^2]
\ge\frac{1}{I_0+A N+(N\ln2/2)\sqrt{I_0+A N}}
=\Omega(N^{-3/2}),
$$

where $A=\ln 2\,\|\pi\|_\infty$. This proves the claimed converse. It cannot be evaded by selecting a taller but narrower heat-capacity peak after only one noisy calibration batch, because posterior concentration and sensitivity area must both be paid for.

[Continue: matching construction](achievability.md).