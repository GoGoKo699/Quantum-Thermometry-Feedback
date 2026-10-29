# Worked examples: from calibration to the global law

[Learning index](README.md) · [Anchor bridge](ANCHOR.md) · [Milestones](MILESTONES.md) · [Exact construction](../science/achievability.md)

These examples use the repository's model, not an additional educational source. Temperature is measured in a fixed reference unit and Boltzmann's constant is set to one. The examples explain the experiment and its accounting; the universal theorem is proved in the linked scientific pages.

## Example 1: a fixed-gap pilot

Suppose the unknown temperature lies between 1 and 2. One pilot qubit has energies zero and 1.5. Its probability of an excited outcome is

```math
p_0(T)=\frac{1}{1+\exp(1.5/T)}.
```

At temperatures 1, 1.5 and 2, this probability is approximately 0.182426, 0.268941 and 0.320821. The monotonic dependence makes the pilot globally identifiable on the interval: larger temperatures give larger expected excited fractions.

For n_1 independent pilot qubits, count the excited outcomes and divide by n_1. Clip this observed fraction to [0.1824255..., 0.3208213...], then apply the inverse

```math
T_0=\frac{1.5}{\ln[(1-p)/p]},\qquad X_0=\ln T_0.
```

The endpoints in an implementation must be computed from the probability formula, not from the rounded numbers printed here. An all-ground pilot returns T_0 = 1; an all-excited pilot returns T_0 = 2. Neither outcome causes a failed or undefined experiment. The [pilot proof](../science/achievability.md) bounds the error uniformly, including these unlikely records.

## Example 2: one complete budget and readout

Take N = 1024. For the smaller block coefficient used by the [finite-grid implementation](../verification/finite_grid.py), use n_1 = 512 pilot qubits, k = 9 qubits per final block and M = 56 final blocks. The total is

```math
512+56\times9=1016\le1024.
```

Eight qubit uses remain unspent. This does not violate the upper budget. The theoretical existence proof permits other fixed positive coefficients in the square-root block size; the example uses the coefficient in the committed numerical checks.

Conditional on a pilot estimate T_0 = 1.5, the final block has one ground state and 511 excited states. Its log degeneracy is L = ln 511, approximately 6.236370, and the excited energy is E = 1.5 L, approximately 9.354554. The excited probability at the actual temperature T is

```math
p(T\mid T_0)=\frac{1}{1+\exp[-L(1-T_0/T)]}.
```

The condition T_0 = 1.5 is an illustrative centering value, not a statement that this exact pilot estimate has positive probability in the finite pilot experiment. If the true temperature is also 1.5, the final excited probability is one half. One block then has log-temperature Fisher information L squared divided by four, approximately 9.723076. All 56 blocks would have approximately 544.492279 information at this perfectly centered point. **This conditional local value is not a global risk certificate.**

Let S count the final excited blocks. The estimator first uses

```math
\widetilde z=\ln\frac{S+1}{57-S}.
```

The true logit, as T ranges from 1 to 2, lies between minus L divided by two and L divided by four. Clip the observed logit to that interval, giving z_hat, then return

```math
\widehat T=\frac{1.5}{1-\widehat z/L}.
```

The three records S = 0, 28 and 56 therefore return temperatures 1, 1.5 and 2, respectively. Smoothing avoids infinite logits; clipping keeps the inverse inside the known physical interval. Every record is retained. In the full experiment, the same calculation uses the actual random pilot estimate rather than fixing it to 1.5.

## Example 3: why one update gives the exponent three halves

A first batch of order N ordinary qubits estimates log temperature to a typical width of order N to the power minus one half. A k-qubit degenerate block has a sensitive window of width order one over k. Choosing k of order the square root of N lets the pilot place the second batch on that scale. Under the remaining budget, the number M of such blocks is also of order the square root of N.

Each well-centered block supplies order k squared information. The combined scale is therefore

```math
M k^2=\Theta(N^{3/2}).
```

This count explains the design but does not prove its global performance. The [construction proof](../science/achievability.md) supplies a uniform estimator-error bound and controls badly centered pilots. The [converse](../science/two_batch_converse.md) separately limits every allowed two-batch experiment, not merely this design.

The area argument explains the converse. A normalized posterior of density information I cannot have height exceeding one half the square root of I. The next n-qubit Gibbs experiment has sensitivity area at most n ln 2. Their product limits the posterior-averaged useful information. Starting with first-stage information of order N, the final batch adds at most order N to the power three halves. A smooth-prior van Trees bound converts this into worst-case squared error of at least order N to the power minus three halves.

## Example 4: read a numerical check without overstating it

The committed [exact-binomial benchmark](../verification/expected.json) sums both stages at seven budgets and nine temperatures in [1,2]. At N = 1024, its largest tested value of N to the power three halves times squared log-temperature risk is approximately 65.778436. At N = 16384 it is approximately 65.316481. These numbers are reproduced by `python verification/checks.py`.

A nearly stable rescaled error is consistent with the analytical exponent. It does not determine the optimal leading constant, certify a supremum over all temperatures, or establish the lower bound. The small omitted first-stage tail is bounded explicitly because the estimator is range-valued; the benchmark does not discard saturated final counts.

## What survives the examples

The matching claim is for the global squared log-temperature risk of **two** full-Gibbs batches, with all calibration counted. The construction is diagonal and needs no entanglement. Its ideal many-body Hamiltonian and complete equilibration are not free in a laboratory cost model; they are supplied operations in this qubit-use model. The [round-count result](../science/round_complexity.md) is a converse beyond two batches, not an asserted matching extension of this example.
