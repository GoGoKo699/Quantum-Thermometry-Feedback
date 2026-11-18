# Scientific account

The question is not how sensitive an already perfectly calibrated thermometer can be. It is how much precision is possible **globally**, when the unknown temperature spans a fixed interval and the experimentalist gets only a prescribed fixed number of opportunities to retune fully equilibrating probes.

The scientific chain is:

1. [Model and classical sufficiency](model.md): define fresh batches, full Gibbs replacement, arbitrary within-batch processing, global log-temperature squared error and a pathwise qubit budget. Energy labels are a sufficient statistical refinement even for quantum-memory protocols.
2. [Gibbs entropy-area identity](entropy_budget.md): the Fisher information of an $`n`$-qubit thermal family has an integrated logarithmic-temperature budget of at most $`n\ln 2`$. A separate pointwise $`O(n^2)`$ bound is proved for the round-count corollary.
3. [Two-batch converse](two_batch_converse.md): a posterior-supremum/Fisher inequality turns the initial extensive information into a maximum useful second-batch information of order $`N^{3/2}`$. Van Trees converts this into a lower bound for arbitrary estimators.
4. [Matching construction](achievability.md): a fixed-gap pilot gives uniform sub-Gaussian calibration, followed by $`\Theta(\sqrt N)`$ adaptively centered blocks of size $`\Theta(\sqrt N)`$. A self-contained smoothed-binomial-logit lemma and an exponential-moment bound charge all rare pilot failures.
5. [Round-count law](round_complexity.md) and [fixed-round attainment](fixed_round_achievability.md): the posterior budget gives the exponent $`2-2^{1-r}`$; polynomially weighted arrays attain it for every fixed $`r`$. Quadratic global precision still requires at least logarithmically many iterations in $`\log N`$.
6. [Physical interpretation and boundaries](interpretation.md): distinguish fixed-round global risk from local sensitivity, probe count from elapsed time, and full thermal replacement from dynamical bath access.

The [related-work comparison](../references/RELATED_WORK.md) identifies the inherited entropy-area, Bayesian and Hamiltonian-engineering ingredients, the substantive new finite-feedback theorem, and the bounded literature-access limitation. [Verification](../verification/README.md) records runnable checks and what they do not prove.

### Principal statements

Let $`x=\ln T`$ lie in $`[a,b]`$ with $`-\infty\lt a\lt b\lt \infty`$ fixed. If $`R_r^*(N)`$ minimizes the worst-case squared error of $`x`$ over allowed $`r`$-batch protocols, then

```math
R_1^*(N)=\Theta(N^{-1}),\qquad
R_2^*(N)=\Theta(N^{-3/2}).
```

The first statement is an inherited benchmark (with an elementary constructive upper bound). The second is the original sharp case of the full fixed-round hierarchy.

For any **fixed** number of batches $`r\ge1`$,

```math
R_r^*(N)=\Theta_r\!\left(N^{-(2-2^{1-r})}\right).
```

The [attaining arrays](fixed_round_achievability.md) overcome rare centering errors by propagating all fixed polynomial moments. Constants depend on $`r`$; this theorem does not allow replacing it with a growing $`r(N)`$. With an $`r`$-uniform information bound, $`O(N^{-2})`$ global risk requires $`r\ge\log_2\log N-O(1)`$. These qualifiers are part of the scientific result.