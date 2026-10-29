# Quantum Thermometry Feedback

**One feedback update changes the optimal global precision exponent of equilibrium thermometry.**

A thermometer whose temperature is unknown on a fixed, nonshrinking interval must allocate some of its quantum probes to discovering where the thermal response is informative. When the interaction Hamiltonian may be retuned only once, after an initial batch of measurements, the best possible squared logarithmic temperature error is

$$
\boxed{R_2^*(N;[T_-,T_+])=\Theta(N^{-3/2})}.
$$

Here $0<T_-<T_+<\infty$ are fixed, $N$ counts **all thermalized qubits in both batches**, and the two batches comprise one calibration-and-feedback step followed by a final readout. The claim is a global, minimax risk statement, valid for biased estimators; it is not an inference from a local quantum Cramér–Rao bound.

## Results

| Question | Supported answer | Location |
|---|---|---|
| With no Hamiltonian feedback, what is the global minimax error? | $\Theta(N^{-1})$; the converse is an established earlier result, and a fixed-gap qubit protocol attains it | [Baseline and attribution](references/RELATED_WORK.md) |
| What is possible with exactly two Gibbs batches? | $\Theta(N^{-3/2})$; universal converse and matching construction | [Lower bound](science/two_batch_converse.md), [construction](science/achievability.md) |
| Does quantum memory circumvent the two-batch converse? | No, under **fresh Gibbs replacement** and classical inter-batch Hamiltonian selection | [Statistical model](science/model.md) |
| How does the number of batches constrain precision? | For every fixed $r$, $R_r^*(N)\ge c_r N^{-(2-2^{1-r})}$ | [Round complexity](science/round_complexity.md) |
| How many batches are necessary for a uniform $O(N^{-2})$ risk? | At least $\log_2\log N-O(1)$; **necessity only** | [Round complexity](science/round_complexity.md) |

The central mechanism is an **entropy–sensitivity-area budget**. For any $n$-qubit Gibbs thermometer, its heat capacity integrated against logarithmic temperature is at most $n\log 2$. After a first measurement, posterior concentration determines how much of this area a newly tuned Hamiltonian can exploit. This gives the sharp two-batch upper limit on information. A calibrated array of degenerate two-level blocks attains the limit without discarding unsuccessful pilot outcomes.

## What the theorem assumes

- Each use returns a completely equilibrated Gibbs state of a freely selected, temperature-independent Hamiltonian on the charged qubits. A thermalization is a **fresh state-preparation/replacement** operation: an input state or probe–ancilla correlation is not preserved through it.
- All Hamiltonians in a batch are selected without using outcomes from that same batch. The second batch may depend on the first classical record; arbitrary measurement processing, ancillas, and retained quantum memory are permitted.
- The total number of thermalized qubits on **every protocol branch** is at most $N$. A fixed compact positive temperature interval is given, but no preliminary temperature estimate is free.
- The attaining implementation uses an ideal $k$-qubit interaction with one ground level and a $(2^k-1)$-fold excited level. Preparing, engineering, and fully equilibrating such a Hamiltonian may be challenging. The theorem **does not** price thermalization time, interaction locality, control work, or hardware cost.

Accordingly, this is a statement about feedback opportunities under a qubit/Gibbs-sample budget, not an experimental or wall-clock quantum advantage. The construction itself is diagonal and needs no entanglement.

## Read the science

Begin with the [scientific reading route](science/README.md).

| Focus | Authoritative file |
|---|---|
| Inputs, outputs, risk, allowed feedback and quantum-memory reduction | [Model](science/model.md) |
| Gibbs Fisher information and the entropy-area identity | [Entropy and sensitivity budget](science/entropy_budget.md) |
| Posterior information and the two-batch minimax converse | [Two-batch converse](science/two_batch_converse.md) |
| Uniformly valid pilot, tuned blocks and smoothed-binomial theorem | [Achievability](science/achievability.md) |
| Fixed-round lower bounds and necessary feedback depth | [Round complexity](science/round_complexity.md) |
| Physical explanation, practical boundaries and limiting cases | [Interpretation](science/interpretation.md) |
| Primary literature and internal nonduplication comparison | [Related work](references/RELATED_WORK.md) |

## Reproduce the checks

With Python, NumPy and SciPy as documented in [verification](verification/README.md), run:

~~~bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
~~~

The checks include a finite-grid *exact-binomial* evaluation of the two-batch estimator at seven budgets, as well as finite Gibbs entropy/Fisher checks and finite scalar-estimator tests. Their expected numerical benchmark is committed alongside the code. **Finite computation does not establish the asymptotic minimax theorem**; the analytical proofs above do.

## Scientific scope

A complete proof is provided for the two-batch theorem and a converse-only extension to arbitrary round counts. No matching optimal fixed-$r>2$ construction, sufficiency of $O(\log\log N)$ rounds, optimal leading constant, or physical time complexity is claimed. Existing adaptive Bayesian thermometry, global logarithmic loss and locally optimal degenerate-probe mechanisms are explicitly credited in the [primary comparison](references/RELATED_WORK.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[LLM reading guide](llms.txt) · [Verification](verification/README.md) · [References](references/references.bib)