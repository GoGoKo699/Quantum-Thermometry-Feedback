# Quantum Thermometry Feedback

**One feedback update changes the optimal global precision exponent of equilibrium thermometry.**

A thermometer can be highly sensitive near one temperature but uninformative elsewhere. When the unknown temperature lies in a fixed positive interval and the Hamiltonian may be retuned only once after calibration, the best possible mean squared logarithmic error is

```math
R_2^*(N)=\Theta(N^{-3/2}).
```

N counts **all thermalized qubits in both batches**, including the pilot. This is a global minimax statement valid for biased estimators, not an inference from a local quantum Cramér–Rao bound. The corresponding root-mean-square logarithmic error has order N to the power minus three quarters.

## Principal results

| Task | Supported result | Proof |
|---|---|---|
| One nonadaptive Gibbs batch | Squared global risk of order N to the power minus one; an inherited benchmark | [Attribution](references/RELATED_WORK.md) and [converse](science/two_batch_converse.md) |
| Two Gibbs batches, one feedback update | Matching lower and upper risk bounds of order N to the power minus three halves | [Lower bound](science/two_batch_converse.md), [construction](science/achievability.md) |
| Arbitrary fixed r batches | Lower bound with exponent 2 minus 2 to the power 1 minus r; matching attainment is not claimed beyond two | [Round complexity](science/round_complexity.md) |
| Desired global squared risk of order one over N squared | At least log-base-two of ln N minus a constant batches are necessary; necessity only | [Uniform round bound](science/round_complexity.md) |

The central mechanism is a finite **entropy–sensitivity-area budget**. A newly tuned Hamiltonian can exploit that area only to the extent that the calibration posterior is concentrated. A fixed-gap pilot followed by calibrated degenerate thermal blocks attains the two-batch limit, including unfavorable pilot and final-count outcomes.

## Read the science

Start with the [scientific index](science/README.md), or go directly to a question:

| Question | Authoritative route |
|---|---|
| What is supplied, measured and charged? | [Model and energy-label sufficiency](science/model.md) |
| Why does finite dimension bound integrated thermal sensitivity? | [Entropy budget](science/entropy_budget.md) |
| Why can no allowed two-batch protocol do better? | [Universal converse](science/two_batch_converse.md) |
| What protocol and estimator attain the bound? | [Construction and uniform statistical bounds](science/achievability.md) |
| What follows for more feedback rounds? | [Round complexity](science/round_complexity.md) |
| What is new, inherited or still uncertain? | [Related work](references/RELATED_WORK.md) and [physical interpretation](science/interpretation.md) |

## Learn the project

The single educational anchor is **Antonella De Pasquale and Thomas M. Stace, _Quantum Thermometry_, arXiv:1807.05762v1 (2018)**.

The [source-to-project bridge](learning/ANCHOR.md) selects the relevant pages and translates temperature Fisher information into this project's global logarithmic-loss model. The [30-milestone map](learning/MILESTONES.md) contains **12 background/preliminaries** and **18 narrative/innovation** understanding targets, independent of any reader's assessment history. The [worked examples](learning/WORKED_EXAMPLES.md) explain a complete paid pilot-and-retuning experiment, including saturated counts. The [learning index](learning/README.md) provides shorter reading routes.

## Reproduce

Install the dependencies in [verification/requirements.txt](verification/requirements.txt), then run:

```bash
python verification/checks.py
```

The [verification guide](verification/README.md) describes three finite Gibbs spectra, a prior-geometry check, 54 binomial-logit cases and an exact-binomial risk grid at seven budgets and nine temperatures. The committed [expected values](verification/expected.json) include an explicit bound on omitted probability tails. Finite checks supplement the proofs; grid maxima are not certified continuum suprema.

## Physical scope

Each paid thermalization supplies a **fresh, fully equilibrated Gibbs state** for a selected temperature-independent Hamiltonian. All Hamiltonians in a batch are fixed before that batch's outcomes are observed. Arbitrary within-batch interactions, measurements, ancillary processing and retained external quantum memory are allowed by the converse under this replacement contract. The total qubit-use budget is capped on every branch, not merely in expectation.

The attaining protocol uses ideal many-body blocks with one ground level and a highly degenerate excited level. It is diagonal and does not need entanglement. The theorem does not price interaction locality, control work, bath disturbance or equilibration time, and establishes no wall-clock or hardware advantage. Partially thermalizing dynamics and coherent bath access are different models. Matching higher-round attainment and optimal leading constants are not claimed.

The [literature comparison](references/RELATED_WORK.md) credits earlier global Bayesian thermometry and probe-design results and retains a full-text access limitation for the recent Fan–Pang paper.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

[LLM reading guide](llms.txt) · [Science](science/README.md) · [Learning](learning/README.md) · [References](references/references.bib)
