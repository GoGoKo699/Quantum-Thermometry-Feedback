# From one retuning to every fixed feedback depth

[Learning route](README.md) · [Source bridge](ANCHOR.md) · [Milestones](MILESTONES.md) · [Exact model](../science/model.md)

The central question is how much a paid calibration record can improve the next equilibrium experiment. We first follow one complete two-batch procedure, then build the array that makes the same idea work for every fixed number of batches.

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

In the worked experiment there are two preparation batches. The first batch's record can determine the second batch's Hamiltonian. All second-batch Hamiltonians must then be fixed before their outcomes are seen. In general, r batches permit at most r - 1 such retunings. Changing a Hamiltonian in response to a record produced within its batch would spend another feedback opportunity.

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
\Vertq\Vert_\infty\le\frac12\sqrt{I(q)}.
```

The mean posterior information after the first batch is O(N). The next Hamiltonian has sensitivity area O(N), and only posterior concentration can make that area useful. Combining the two facts bounds the second batch's averaged information by O(N) times O(square root of N). The global van Trees inequality turns this into a mean-square risk lower bound of order N to the power minus 3/2, for biased estimators as well.

Quantum memory does not defeat this proof under the stated access. At fixed Hamiltonian the Gibbs family is diagonal in a known energy basis. Revealing every energy-basis index supplies a statistically stronger classical record from which all allowed quantum processing can be simulated. The reduction does not apply to a general transient bath interaction that retains probe correlations. See [the model](../science/model.md#allowable-measurements-and-memory).

## A wider safety net for the next batch

The two-batch example puts every final block at the pilot's estimated temperature. Its proof succeeds because the first pilot has a strong enough tail bound to control the cost of a misplaced narrow response. Repeating that design at ever narrower widths would need a new tail argument at every step. A small mean-square error alone does not control rare, badly misplaced response peaks.

The fixed-round construction instead spreads the next batch over a small array of possible centers. It spends most blocks near the current estimate and fewer at increasing distances. A poor earlier estimate can then leave a useful group nearer the true temperature. The number of blocks is fixed by the batch allocation, including on poor histories.

Write X for the preceding estimate of x = ln T, and w for its predetermined accuracy scale. The scale is chosen from the budget and stage number; it is not a certified error bound on the observed X. Let B be the next batch's qubit allocation. For sufficiently small w and large Bw, choose

```math
k=\lceil1/w\rceil,\qquad
L=\ln(2^k-1),\qquad
M=\lfloor B/k\rfloor,\qquad
J=\lfloor M^{1/8}\rfloor.
```

Here k is the number of qubits in each block, while M is the number of blocks the allocation could accommodate. For each integer j between -J and J, set

```math
c_j=X+jw,\qquad
m_j=\left\lfloor\frac{M}{4(1+|j|)^2}\right\rfloor.
```

The center c_j is a log temperature. The corresponding physical temperature is exp(c_j). The polynomial weights give progressively fewer blocks to distant centers. Their sum obeys

```math
\sum_{j=-J}^{J}m_j
\le\frac{M}{4}\sum_{j\in\mathbb Z}(1+|j|)^{-2}
\lt M,
\qquad
k\sum_jm_j\le B.
```

Every history therefore fits the same batch budget. A center outside the original temperature interval is still an allowed design choice: its Hamiltonian depends on X and the chosen grid, not on the unknown true temperature.

Each block at c_j has the same degenerate spectrum as before, with gap E_j = L exp(c_j). At a candidate log temperature t its excitation probability is

```math
p_j(t)=\frac{1}{1+\exp[-L(1-\exp(c_j-t))]}.
```

All blocks and gaps are chosen before any outcomes in this batch are inspected. Conditional on the earlier history and true temperature, fresh Gibbs replacement makes these binary outcomes independent. They generally have different probabilities, so their total Z is not a binomial count. Its known mean function is

```math
G(t)=\sum_{j=-J}^{J}m_jp_j(t).
```

Each term is increasing in t. Restrict the estimate to the nonempty interval

```math
I_X=[a,b]\cap[X-Jw,X+Jw].
```

Clip Z to the range G(I_X), then invert G on that interval. This defines the next estimate X' even at zero excitations or complete excitation. If a record saturates the response, clipping returns the relevant endpoint of I_X. Every record remains in the experiment.

The proof uses the conservative finite conditions w at most 1/2 and M at least 2 to the power 16. If these are not met, the complete protocol instead spends the batch allowance on ordinary fixed-gap qubits and keeps its preceding estimate. At any fixed number of stages, sufficiently large N makes every refinement meet the conditions. The fallback defines the small-budget procedure without asserting small finite constants.

### A small array budget

For a concrete design calculation, take B = 4096 and w = 1/8. Then k = 8, M = 512 and J = 2. The multiplicities are

| Center index j | Log-temperature offset c_j - X | Blocks m_j |
|---|---|---:|
| -2 | -1/4 | 14 |
| -1 | -1/8 | 32 |
| 0 | 0 | 128 |
| 1 | 1/8 | 32 |
| 2 | 1/4 | 14 |

There are 220 blocks and 1760 charged qubits, within the allocation. The readout would be a total of 220 binary indicators, inverted through their full mean G. This is an allocation calculation below the proof's conservative M threshold; the complete protocol uses its fixed-gap fallback at this budget. The numbers show how to specify and pay for the array, without claiming a finite-budget risk advantage. The earlier 256-qubit experiment remains a separate complete two-batch illustration.

## Paying for rare histories

The array is useful because a calibration error changes its effective information only by a polynomial factor. Normalize the preceding error as

```math
D=\frac{x-X}{w}.
```

For a moderate D, a grid center lies within w of the true x. Its multiplicity is at least a constant times M divided by (1 + |D|) squared. Near x, each block in this group has a probability slope of order 1/w. The full mean count G therefore still moves detectably when the candidate temperature moves a little. A bounded-variable concentration bound converts that slope into a conditional estimate width of order

```math
\frac{w}{\sqrt M}(1+|D|)^2.
```

This is the width of a conditional tail bound, not a deterministic error promise for one observed count. Its polynomial dependence is the key change from relying repeatedly on one center.

The proof keeps more than mean-square accuracy. At the incoming scale w it assumes, for every fixed positive moment order q,

```math
\sup_{x\in[a,b]}\mathbb E_x|X-x|^q\le C_qw^q.
```

The fixed-gap pilot supplies these bounds for all fixed q. For the next q-th moment, the polynomial factor above can be paid with the incoming 2q-th moment. Still rarer histories, where the useful center could fall beyond the array, are paid using a sufficiently high fixed incoming moment and the bounded estimator range. No such history is removed, and its qubits are already included in the same allocation B.

After both contributions are charged, the [full refinement proof](../science/fixed_round_achievability.md) gives

```math
\sup_{x\in[a,b]}\mathbb E_x|X'-x|^q
\le C'_q\left(\frac{w}{\sqrt{Bw}}\right)^q.
```

This holds for every fixed q under the lemma's large-budget conditions. All-zero records, all-one records and temperatures at a or b are included by the clipped estimator. To prove a later second moment, the induction may need a much higher moment at an earlier stage. That demand is finite at every fixed number of stages and is supplied by the pilot and the same refinement lemma.

## The sharp fixed-round hierarchy

Fix the number r of batches before increasing N, and allocate B = floor(N/r) qubits to each batch. The first batch is a fixed-gap pilot. Its error width is of order B to the power minus one half. For later batches use the array with a predetermined width

```math
w_j=B^{-\alpha_j},\qquad
\alpha_1=\frac12,\qquad
\alpha_{j+1}=\frac{1+\alpha_j}{2}.
```

The refinement width w divided by the square root of Bw gives exactly this recurrence. Solving it yields

```math
\alpha_j=1-2^{-j}.
```

At every fixed stage, Bw diverges as N increases, so the required block count also grows. The second-moment upper bound after r batches has exponent 2 alpha_r. The [general posterior converse](../science/round_complexity.md) gives the same exponent from the opposite direction. Both arguments use the same fixed interval, Gibbs replacement, permitted feedback and pathwise qubit cap. Therefore

```math
\boxed{
R_r^*(N;[a,b])
=\Theta_r\!\left(N^{-(2-2^{1-r})}\right)
\qquad\text{for every fixed integer }r\ge1.
}
```

The constants may depend on r and the fixed temperature interval. The law concerns squared log-temperature error; the root error has half the displayed exponent.

| Preparation batches r | Available retunings | Sharp squared-error order |
|---:|---:|---|
| 1 | 0 | $`N^{-1}`$ |
| 2 | 1 | $`N^{-3/2}`$ |
| 3 | 2 | $`N^{-7/4}`$ |
| 4 | 3 | $`N^{-15/8}`$ |

The three-batch entry is now attained by an explicit protocol. This is the scientific change beyond the earlier record, which had matching bounds only for two batches. It establishes exponents, not optimal leading constants or an assertion about which design is best at a particular finite N.

## Why fixed-round attainment does not settle growing depth

Each additional fixed batch brings the exponent closer to two. It is tempting to put a growing r directly into the formula and declare quadratic global risk. That substitution is not justified: the upper-bound constants and required moment orders can grow with r, the allocation B = floor(N/r) changes, and the proof's large-budget conditions must hold at every stage.

A separate converse has constants uniform in the number of batches. It shows that attaining risk at most K times N to the power -2, with one constant K independent of N, requires

```math
r(N)\ge\log_2\ln N-O(1).
```

This is a necessary number of preparation batches. A matching growing-r schedule and its uniform error analysis remain unproved here. The fixed-r hierarchy settles every fixed depth while leaving that different asymptotic question open.

## What has and has not been established

The project now supplies matching minimax exponents and an attaining method for every fixed number of preparation batches. The weighted array is the step that protects successive refinements against all earlier calibration histories; high local sensitivity alone would not prove the result. The converse also allows arbitrary quantum processing and retained memory under the stated Gibbs-replacement access, while the construction needs only binary energy readout.

Complete equilibrium and a controllable degenerate many-body spectrum remain supplied resources. Gaps and block sizes grow with the budget. There is no local-Hamiltonian implementation, thermalization-time guarantee, optimal constant or entangled-measurement advantage in the theorem. Faster error decay in charged Gibbs samples does not by itself imply faster laboratory operation. [Physical interpretation](../science/interpretation.md) separates those costs from the proved sample-budget result.
