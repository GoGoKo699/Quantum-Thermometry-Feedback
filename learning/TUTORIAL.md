# One calibration, one retuning, one final estimate

[Learning route](README.md) · [Source bridge](ANCHOR.md) · [Milestones](MILESTONES.md) · [Exact model](../science/model.md)

## One counting thermometer

A thermometer need not display a number directly. Consider a qubit with a ground state of energy zero and an excited state of energy E_0. After full equilibrium with a bath at temperature T, measuring its energy gives an excitation with probability

```math
p_0(T)=\frac{1}{1+\exp(E_0/T)}.
```

Energies and temperatures use the same fixed units, with k_B = 1. Higher temperature increases this probability, so an excitation count from many independent qubits supplies a temperature estimate. The randomness of the count is sampling uncertainty, not a fluctuating true bath temperature.

For n independent qubits and a count s, the likelihood is the probability of that record at each candidate temperature:

```math
\Pr_T(S=s)=\binom ns p_0(T)^s[1-p_0(T)]^{n-s}.
```

The parameter is fixed but unknown. An estimator is a rule taking the observed count to a reported value. The [pilot construction](../science/achievability.md#stage-1-fixed-globally-identifiable-pilot) clips the observed fraction to the probabilities possible in the known interval, then inverts p_0. This remains defined even when no qubit is excited.

This foundation corresponds to the anchor's estimation discussion and thermal QFI relation; see [the exact source locations](ANCHOR.md#selected-source-locations).

## What the budget and the error mean

A thermalized-qubit use is charged each time it supplies a Gibbs state. Reusing one physical qubit a hundred times costs a hundred uses. A k-qubit block costs k, even if its readout is only a single binary outcome. The total N includes calibration, final readout probes and unfavorable branches.

Write x = ln T. The squared error is

```math
(\widehat x-x)^2=\left(\ln\frac{\widehat T}{T}\right)^2.
```

Reporting twice the true temperature and reporting half of it have the same loss. The global risk takes the largest expected loss across a fixed positive temperature interval. It is a mean-square error; taking its square root changes the two-batch exponent from 3/2 to 3/4. No statement below claims root-error scaling N to the power minus 3/2.

The experiment has two preparation batches. The first batch's record can determine the second batch's Hamiltonian. All second-batch Hamiltonians must then be fixed before their outcomes are seen. A third retuning based on those outcomes would be a different feedback budget.

## A narrow peak is not a global guarantee

A large interacting probe can respond very sharply near a chosen temperature. For a fixed Hamiltonian, Fisher information for x equals its dimensionless heat capacity C_H(x). It measures how rapidly the likelihood changes near x, not whether x is already known well enough to place the response peak there.

Entropy provides the missing global restriction. With entropy S measured using natural logarithms,

```math
\frac{dS_H}{dx}=C_H(x),\qquad
\int_a^b C_H(x)\,dx\le n\ln2
```

for any Hamiltonian on n qubits. The first equality is a Gibbs identity; the second follows because the entropy range is at most n ln 2. A tall peak must have limited width or area. The [entropy proof](../science/entropy_budget.md) does not assume weak interactions or an extensive heat-capacity peak.

A k-qubit block with one ground state and g = 2^k - 1 excited states at a common gap E illustrates this. Define L = ln g. Its excitation probability and log odds are

```math
p=\frac{1}{1+e^{-z}},\qquad z=L-\frac{E}{T}.
```

Choosing E = L T_0 centers the binary response at a provisional temperature T_0. At T = T_0 the outcomes are equally likely and the block information for x is L squared divided by four. Its useful log-temperature width is of order 1/k. A large value at the center alone does not prove low global risk when the provisional temperature is wrong.

## A finite worked experiment

Take N = 256, a known interval from T = 1 to T = 2, and pilot gap E_0 = 1.5. Use 128 calibration qubits. Suppose 34 are excited. The observed fraction 34/128 is inside the permitted probability interval, and inversion gives

```math
T_0=\frac{1.5}{\ln(94/34)}\simeq1.47502.
```

Use the remaining 128 qubits as M = 32 blocks of k = 4 qubits. Each block has g = 15 excited states and gap

```math
E=(\ln15)T_0\simeq3.99443.
```

All blocks are centered using that same pilot record; none is retuned in response to second-batch outcomes. The pathwise budget is exactly 128 + 32 times 4 = 256.

If the true temperature were T = 1.5, the second-batch excitation probability would be about 0.51127. This probability is used to explain the experiment; the estimator is not given the true temperature.

For second-batch count S, use the smoothed log odds

```math
\widetilde z=\ln\frac{S+1}{M-S+1}.
```

The added ones prevent infinite values at S = 0 and S = M. Project this number onto the interval of z values corresponding to T between 1 and 2. Invert the projected value to return the estimated temperature. For S = 16, the smoothed log odds are zero and the answer is T_0. For S = 0 or S = 32, projection returns the lower or upper temperature endpoint, respectively. Every outcome is assigned a finite, range-valued estimate; no record is discarded.

The [verification grid](../verification/README.md) uses this N = 256 block allocation and its analogues at larger N. These sample counts illustrate a procedure, not a claim that the displayed single realization is representative of the worst-case error.

## Why the construction scales

With a fixed positive temperature interval, the first batch of order N qubits estimates x with an error width of order N to the power minus one half. Choose block size of order the square root of N so its sensitivity width is comparable. The remaining budget then supplies order the square root of N blocks, each having centered information of order N. Their combined centered information is of order N to the power 3/2.

There are two additional proof obligations. First, sensitivity must be turned into an actual estimate, including saturated counts. The uniform smoothed-binomial-logit lemma in [the construction](../science/achievability.md#uniform-binomial-logit-lemma) supplies that step. Second, rare bad pilot outcomes must not dominate the average loss. The pilot has a uniform sub-Gaussian tail, which bounds the exponential amplification of its centering error at block size proportional to the square root of N. The [full-distribution calculation](../science/achievability.md#charge-the-entire-pilot-error-distribution) is why the result has no hidden discarded failures or logarithmic loss.

## Why one update has a limit

The lower-bound proof chooses a smooth prior density that vanishes at the endpoints of the fixed interval. It is a mathematical test prior: a protocol's worst-case risk cannot be smaller than its average risk under this prior. The operational problem remains minimax, not an assumption that nature draws the temperature from that density.

After observing the first batch, the posterior q describes the remaining uncertainty. Define its density Fisher information by

```math
I(q)=\int_a^b\frac{q'(x)^2}{q(x)}\,dx.
```

Because q starts at zero, rises to its maximum and returns to zero, its total variation is at least twice its maximum. Cauchy–Schwarz then gives

```math
\|q\|_\infty\le\frac12\sqrt{I(q)}.
```

The mean posterior information after the first batch is O(N). The next Hamiltonian has sensitivity area O(N), and only posterior concentration can make that area useful. Combining the two facts bounds the second batch's averaged information by O(N) times O(square root of N). The global van Trees inequality turns this into a mean-square risk lower bound of order N to the power minus 3/2, for biased estimators as well.

Quantum memory does not defeat this proof under the stated access. At fixed Hamiltonian the Gibbs family is diagonal in a known energy basis. Revealing every energy-basis index supplies a statistically stronger classical record from which all allowed quantum processing can be simulated. The reduction does not apply to a general transient bath interaction that retains probe correlations. See [the model](../science/model.md#allowable-measurements-and-memory).

## What has and has not been established

The upper construction and the universal lower bound have the same resources, fixed interval and loss. Together they establish

```math
R_2^*(N)=\Theta(N^{-3/2}).
```

For a fixed number r of batches, the repository additionally proves a lower bound with exponent 2 - 2 to the power (1 - r). For r = 3 that gives a risk lower bound of order N to the power minus 7/4, not an attaining three-batch protocol. The necessary round count for a uniform quadratic global-risk law grows at least as the logarithm of log N; sufficiency is not proved here.

Finally, complete equilibrium and a controllable degenerate many-body spectrum are supplied resources. Faster error decay in charged Gibbs samples does not by itself imply faster laboratory operation. [Physical interpretation](../science/interpretation.md) separates thermalization time, interaction locality, energy and bath stability from the proved sample-budget result.
