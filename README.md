# Quantum Thermometry Feedback

**One feedback update changes the optimal global precision exponent of equilibrium thermometry.**

A temperature is unknown on a fixed interval with positive, finite endpoints. All calibration and measurement probes share a budget of N thermalized-qubit uses. With two Gibbs-preparation batches and one intervening Hamiltonian update, the optimal worst-case squared logarithmic temperature error obeys

```math
R_2^*(N;[T_-,T_+])=\Theta(N^{-3/2}).
```

This is a global minimax mean-square error law, including biased estimators and unfavorable calibration records. It is not inferred from a local Cramer–Rao bound or a free preliminary estimate.

## Results and their scope

| Question | Supported answer | Proof |
|---|---|---|
| One fixed, nonadaptive batch | Mean-square error of order N to the power minus 1; inherited benchmark | [Attribution](references/RELATED_WORK.md) |
| Two batches, one Hamiltonian update | Sharp mean-square error of order N to the power minus 3/2 | [Converse](science/two_batch_converse.md) and [attainment](science/achievability.md) |
| Retained quantum memory | Does not evade the converse under fresh Gibbs replacement | [Model and sufficiency](science/model.md) |
| A fixed number r of batches | Lower-bound exponent 2 - 2 to the power (1 - r); no general matching construction asserted | [Round-count converse](science/round_complexity.md) |
| Desired quadratic global precision | Requires at least log-base-two of log N, up to an additive constant, batches; necessity only | [Uniform depth bound](science/round_complexity.md) |

The mechanism is an **entropy budget for integrated thermal sensitivity**. An n-qubit Gibbs thermometer has at most n ln 2 sensitivity area over logarithmic temperature. The first batch determines how concentrated the posterior can become; that concentration limits how much area a retuned second batch can exploit. A calibrated array of degenerate two-level blocks attains the bound without discarding pilot failures.

## Read the science

Start with [the scientific index](science/README.md), then [the exact model](science/model.md). The proof route is [entropy and sensitivity](science/entropy_budget.md) → [posterior-information converse](science/two_batch_converse.md) → [matching construction](science/achievability.md). The [round-count result](science/round_complexity.md) is a separately qualified consequence.

For physical meaning and implementation boundaries, read [the interpretation](science/interpretation.md). For inherited results and the specific new contribution, read [Related work](references/RELATED_WORK.md) and the [bibliography](references/references.bib).

## Learn the project

The single educational anchor is **Antonella De Pasquale and Thomas M. Stace, _Quantum Thermometry_, arXiv:1807.05762v1 (2018)**.

The [source bridge](learning/ANCHOR.md) selects exact pages and equations, translates notation and distinguishes the source's local sensitivity and dynamical examples from this project's global, finite-feedback task. The [30-milestone map](learning/MILESTONES.md) has **14 background/preliminaries** and **16 narrative/innovation** targets. The [worked tutorial](learning/TUTORIAL.md) follows an explicit 256-qubit experiment, including saturated counts, before joining the converse and construction. These are shared scientific learning materials, not personal assessment records.

[Learning entry point](learning/README.md) · [Direct specialist route](science/README.md) · [LLM reading guide](llms.txt)

## Reproduce

With the pinned dependencies in [verification/requirements.txt](verification/requirements.txt), run:

```bash
python -m pip install -r verification/requirements.txt
python verification/checks.py
python verification/learning_checks.py
```

The [verification guide](verification/README.md) explains the Gibbs and prior identities, uniform-logit finite checks, and exact-binomial risk summations at seven budgets and nine temperatures. The learning check validates milestone structure and the numerical worked example. Finite checks supplement the analytical proofs; they do not certify universal optimality or a continuum worst-case constant.

## Physical and statistical boundaries

Every paid access prepares a **fresh, fully equilibrated Gibbs state** for a chosen temperature-independent Hamiltonian. Input probe correlations do not survive that replacement. Hamiltonians within one batch are fixed before its outcomes are observed; quantum processing, ancillas and retained memory are allowed. The total number of thermalized qubits is bounded on every branch, not only on average.

The construction uses an ideal many-body block with one ground level and a large degenerate excited level. It requires no entangled readout, but does not establish a local-interaction implementation, thermalization-time advantage, bounded-control-energy advantage or laboratory speedup. A shrinking prior interval or a partially thermalizing dynamical channel changes the task.

The complete matching result concerns **two batches**. Matching attainment for arbitrary fixed r greater than two, sufficiency of log-log feedback depth, and optimal leading constants are not claimed. The [literature comparison](references/RELATED_WORK.md) retains its stated recent-source full-text access limitation.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
