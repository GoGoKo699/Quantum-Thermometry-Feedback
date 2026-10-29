# Reproducible numerical checks

The primary result is analytical. This directory checks the estimator's exact finite-distribution implementation, selected Gibbs identities and a finite grid of the uniform logit lemma. None of these tests certifies an asymptotic theorem, the universality of the converse, or a priority claim.

## Environment and command

Python 3.12 with the pinned dependency versions is recommended:

~~~bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
~~~

The direct exact-binomial summation is also available:

~~~bash
python verification/finite_grid.py
~~~

It prints machine-readable JSON. The checked historical output is stored as [expected.json](expected.json). Note that code, expected values and proofs were not derived from the same source of independent verification.

## What is tested

1. Three finite energy spectra: numerical Fisher-information area equals the Gibbs-entropy difference over a large finite $x=\ln T$ interval, and respects the dimension entropy and pointwise $O(n^2)$ bounds.
2. The zero-boundary sine-squared prior: normalization, exact analytic prior Fisher information, and the density peak inequality.
3. Fifty-four finite $(M,p)$ combinations: exact binomial moments satisfy the conservative $200/[Mp(1-p)]$ smoothed-logit bound.
4. The two-batch implementation: exact sums over first-stage and second-stage Bernoulli counts at budgets $N=256,512,1024,2048,4096,8192,16384$ and nine log-spaced temperatures in $[1,2]$, with pilot gap $E_0=1.5$ and block size $\lfloor0.3\sqrt N\rfloor$. The grid checks the observed $N^{3/2}$-scaled risk and verifies all qubits are charged.

The finite-grid script omits first-stage binomial terms with floating-point mass at most $10^{-18}$ for efficiency; its output includes an **upper bound on the discarded contribution to the squared loss**, using the fact that the estimator is clipped to the physical interval. This bound is below $10^{-12}$ in all committed cases. Smoothing handles zero and full second-stage counts rather than discarding them.

The exact finite-grid run uses a smaller numerical coefficient in $k$ than the simple asymptotic existence proof; both are $\Theta(\sqrt N)$ and satisfy the same theorem. Grid maxima are maxima over nine temperatures, **not** certified suprema over the continuum. An approximately constant value of $N^{3/2}$ times the finite-grid error is a consistency check, not evidence that a universal optimal leading constant has been determined.

## Proof-to-test map

| Scientific assertion | Proof location | Finite check |
|---|---|---|
| $\int C_H(x)dx\le n\ln2$ | [Entropy-area identity](../science/entropy_budget.md) | Three spectra and Simpson integration |
| $\|q\|_\infty\le\frac12\sqrt{I(q)}$ | [Posterior peak lemma](../science/two_batch_converse.md) | Fixed smooth prior |
| Logit squared error $\le200/[Mp(1-p)]$ | [Uniform lemma](../science/achievability.md) | 54 binomial distributions |
| $\Theta(N^{-3/2})$ minimax risk | [Converse](../science/two_batch_converse.md) and [attainment](../science/achievability.md) | Two-stage finite-grid implementation only |
| Fixed-round and depth converse | [Round complexity](../science/round_complexity.md) | Analytical result; no numerical asymptotic certification |

The code does not simulate a thermalization dynamical channel or a local Hamiltonian implementation. The complete-access model is specified in [the science](../science/model.md).