# Reproducible numerical checks

The results are analytical. This directory checks the two-batch estimator, hedged fixed-round refinement, and growing-round nested intervals and probe response. The finite probability calculations use floating point.

## Environment and command

Python 3.12 with the pinned dependency versions is recommended:

~~~bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
~~~

This command runs the historical two-batch, hedged-array and growing-round suites. The hedged-array checks can also run alone:

~~~bash
python verification/fixed_round_checks.py
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
5. The actual hedged-array implementation in [fixed_round_checks.py](fixed_round_checks.py): 37 checks compare stable reduced Gibbs probabilities with explicitly enumerated small spectra or a large-degeneracy saturation case; 96 layouts check integer floors, pathwise qubit use, clipped zero/full counts and selected nearest-group derivatives.
6. The complete grouped Poisson-binomial count distribution for 162 conditional arrays at $M=64,128,256$, widths $w=0.02,0.05$, three true temperatures and nine preceding-center offsets, plus one full $M=2^{16}$ array in the lemma's stated regime (31,574 actual blocks). The code inverts the complete monotone mean for every possible count, including saturation, physical endpoints and preceding centers outside the hedge radius. It checks 394 applicable one-sided concentration events. Six smaller examples compare grouped convolution against enumeration of every binary record.
7. A fully enumerated nine-point preceding-center distribution includes rare centers beyond the good-event cutoff and beyond the array. The checks include their actual contribution to normalized second and fourth moments, the deterministic output cap, and the higher-moment bound used for the bad histories. Seven design cases check the exact $M_0=2^{16}$ and $w\le1/2$ fallback thresholds. Twelve exact rational recurrence checks keep the fixed-round exponent and deterministic allocation conventions consistent.
8. The [growing-round suite](growing_round_checks.py) checks 56 rounded qubit schedules, 60 direct Gibbs enumerations for the star readout, 672 interval response slopes and 4,410 terminal histories in 14 fully enumerated toy count trees. The count trees exercise nested clipping and first-exclusion loss accounting.

The finite-grid script omits first-stage binomial terms with floating-point mass at most $10^{-18}$ for efficiency; its output includes an **upper bound on the discarded contribution to the squared loss**, using the fact that the estimator is clipped to the physical interval. This bound is below $10^{-12}$ in all committed cases. Smoothing handles zero and full second-stage counts rather than discarding them.

The exact finite-grid run uses a smaller numerical coefficient in $k$ than the simple asymptotic existence proof; both are $\Theta(\sqrt N)$ and satisfy the same theorem. Grid maxima are maxima over nine temperatures, **not** certified suprema over the continuum. An approximately constant value of $N^{3/2}$ times the finite-grid error is a consistency check, not evidence that a universal optimal leading constant has been determined.

The hedged-array suite uses the stated floors and multiplicities directly. The smaller complete-distribution grids test that finite array component below the proof's conservative threshold; the full protocol would use its paid fixed-gap/unchanged-estimate fallback there. The separate $M=2^{16}$ example and threshold checks cover the actual accepted-array regime. Its count-law convolution and estimator inversion use no Monte Carlo or intentional tail pruning. Numerical underflow and rounding still limit floating-point calculations; the tests are not interval certificates. A far-off preceding estimate can give a large conditional normalized risk, as the reported examples show. The theorem controls its *weighted* contribution through higher moments; it does not claim a uniform conditional-risk bound over all histories. The finite rare-history example tests this accounting, while the proof establishes the all-moment induction for every fixed number of stages.

## Proof-to-test map

| Scientific assertion | Proof location | Finite check |
|---|---|---|
| $\int C_H(x)dx\le n\ln2$ | [Entropy-area identity](../science/entropy_budget.md) | Three spectra and Simpson integration |
| $\Vert q\Vert_\infty\le\frac12\sqrt{I(q)}$ | [Posterior peak lemma](../science/two_batch_converse.md) | Fixed smooth prior |
| Logit squared error $\le200/[Mp(1-p)]$ | [Uniform lemma](../science/achievability.md) | 54 binomial distributions |
| $\Theta(N^{-3/2})$ minimax risk | [Converse](../science/two_batch_converse.md) and [attainment](../science/achievability.md) | Two-stage finite-grid implementation only |
| Hedged refinement, including rare preceding histories | [Fixed-round attainment](../science/fixed_round_achievability.md) | Complete finite count laws, clipping, derivative/concentration checks and weighted outlier example |
| Matching fixed-round exponent | [Round complexity](../science/round_complexity.md) and [attainment](../science/fixed_round_achievability.md) | Estimator implementation and exact rational recurrence only; no numerical asymptotic certification |
| Sharp depth for quadratic risk | [Uniform converse](../science/round_complexity.md) and [growing-round schedule](../science/growing_round_achievability.md) | Rounded budgets, Gibbs response and fully enumerated toy first-exit risks |

The proofs establish the continuum risk, including the growing-round bound. The numerical schedule and toy count trees check separate parts of the proof. They provide no estimate of a finite-budget optimal constant or equilibration time.
