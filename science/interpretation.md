# Physical meaning and boundaries

[Science index](README.md) · [Converse](two_batch_converse.md) · [Construction](achievability.md) · [Round complexity](round_complexity.md)

## A picture in words

A generic equilibrium thermometer trades **sensitivity height** against **temperature bandwidth**. With many-body interactions, a $k$-qubit Gibbs probe can have a heat-capacity peak of order $k^2$ near a chosen temperature, but the peak narrows to order $1/k$ in log temperature. Its integrated area remains only $O(k)$.

With no retuning, a fixed-width unknown-temperature interval forces the total useful averaged information back to $O(N)$. A first pilot batch of $O(N)$ ordinary qubits localizes the temperature to width $O(N^{-1/2})$. That is enough to center a second batch of blocks of size $k=O(\sqrt N)$. There are $O(\sqrt N)$ such blocks under the remaining budget, each providing order $k^2=O(N)$ information when centered. The total usable information is therefore $O(N^{3/2})$, leading to global squared error $O(N^{-3/2})$.

The converse proves that *no other choice of interactions, joint measurement or quantum memory* within the stated two-batch Gibbs-replacement model beats the exponent. Its decisive ingredient is not a speculative local Cramér–Rao argument: it bounds the posterior mass available to exploit a finite sensitivity area, and then invokes a global Bayesian inequality.

## One feedback action is an information resource

The rigorous comparison is:

| Regime | Global squared log-temperature risk under a qubit budget |
|---|---|
| One fixed nonadaptive batch | $\Theta(N^{-1})$ |
| Two batches, one intervening Hamiltonian update | $\Theta(N^{-3/2})$ |
| Every fixed $r$ batches | $\Theta_r(N^{-[2-2^{1-r}]})$ |
| Desired $O(N^{-2})$ risk | Sharp depth $\log_2\ln N+O(1)$ batches |

Earlier many-update adaptive strategies illustrate how retuning can approach local Heisenberg-like sensitivity. Here the batch count is an explicit resource in a global minimax theorem. Full comparison and attribution appear in [Related work](../references/RELATED_WORK.md).

## Why further batches need a different construction

Repeating the same perfectly centered block design would hide an important statistical problem. A slightly inaccurate estimate can put a narrow sensitivity peak far from the true temperature. The two-batch proof uses a sub-Gaussian pilot to pay for this through an exponential moment; a later mean-square guarantee alone does not supply that exponential control.

The [fixed-round construction](fixed_round_achievability.md) spreads each new batch over nearby centers instead. It spends fewer blocks on more distant centers, with polynomial rather than exponential decay. A nearby center remains available on moderately inaccurate histories, and higher polynomial moments pay for the remaining rare histories. At uncertainty width w, the next squared-error scale is of order w/N for a fixed batch count. Starting at w of order N to the power minus1/2 gives the exponent sequence 3/2, 7/4, 15/8. Every batch's full array is fixed before its outputs are read.

The [growing-round construction](growing_round_achievability.md) uses intervals that always stay nested. If a refinement first misses the true temperature, every later estimate stays in the preceding interval. The error on that history therefore grows at most with the width of that interval. A schedule designed backward from the final target makes the expected losses and qubit charges summable. It also accepts a two-body star probe whenever its central-bit probability has the required inverse-width slope.

## Energy readout and classical feedback

The impossibility theorem is universal over finite-dimensional Gibbs Hamiltonians and quantum measurements. However, each thermal family commutes with itself as $T$ changes when $H$ is fixed. Measuring its energy eigenlabel is statistically sufficient. The attaining protocol uses only classical excitation counts and a classical retuning instruction. Thus the result is an information-geometric constraint on equilibrium quantum *sample design*, rather than a claim of entanglement-enhanced readout or quantum computational speedup.

If the Hamiltonian itself secretly depends on temperature, if coherent bath access is supplied, or if probe–memory correlations survive thermalization, the energy-label reduction needs not apply. That is a change to the operation supplied by the experiment, not a loophole in the stated theorem.

## Costs absent from the qubit-budget statement

- **Time:** A Gibbs state is assumed to be available after full equilibration; the required contact or mixing time may depend strongly on $k$. No total elapsed-time advantage follows from $N^{-3/2}$ alone.
- **Interaction complexity:** The fixed-round arrays use an ideal global $k$-qubit projector. The growing-round scheme also admits a commuting two-body star with bounded pair strengths and a hub of growing degree. Its central field is of order $k$, and all $k$ spins are charged even though only the hub is read.
- **Energy and work:** On a fixed positive temperature interval, the tuned block gap is $\Theta(k)$; there is no assertion of constant maximum control energy, constant thermodynamic work, or fault tolerance.
- **Bath disturbance:** The reservoir is assumed large enough to supply the same unknown temperature to all thermalizations. A finite reservoir that cools due to measurement is a different joint inference problem.
- **Prior and statistics:** The interval $[a,b]$ is fixed as $N$ grows; a prior already localized on a scale shrinking with $N$, an atomic/discrete prior, or an expected-only sample budget changes the task.

These are load-bearing restrictions, not cosmetic caveats. The theorem compares all protocols within a broad but **specified** equilibrium replacement model.

## Examples and reproducibility

For one $k$-qubit degenerate block with $L=\ln(2^k-1)$, a pilot-centered gap $E=L e^{X_0}$ yields

$$
p_{\mathrm{exc}}=\sigma\big(L[1-e^{X_0-x}]\big).
$$

At exact centering $x=X_0$, $p_{\mathrm{exc}}=1/2$ and the block Fisher information is $L^2/4$. The complete upper-bound proof does not assume exact centering: it controls the entire pilot-error distribution, including the exponentially unlikely large deviations.

The [verification code](../verification/README.md) evaluates the risk by summing both binomial sampling stages exactly (subject to stated floating-point tail cutoffs) at finite sizes. That provides a check on the estimator, not independent proof of universal optimality.

## Open but nonessential extensions

Optimal leading constants, bounded-degree probe design and sensitivity to noninstantaneous thermalization remain open in the present account.
