# Quantum Thermometry Feedback

**Quadratic global precision takes log-log feedback depth.**

A temperature is unknown on a fixed interval with positive, finite endpoints. All calibration and measurement probes share a pathwise budget of N thermalized-qubit uses. For every fixed number r of Gibbs-preparation batches, with Hamiltonian updates only between batches, the optimal worst-case squared logarithmic temperature error obeys

```math
R_r^*(N)=\Theta_r\!\left(N^{-(2-2^{1-r})}\right).
```

Two batches give the original sharp exponent 3/2; three give 7/4, and four give 15/8. The matching construction uses a fixed-gap pilot followed by arrays of differently centered thermal blocks. Their polynomially decreasing allocations keep rare calibration errors in the unconditional risk. This is a global minimax mean-square law, including biased estimators and all histories.

When the batch count grows, the sharp threshold for squared error of order $`N^{-2}`$ is $`\log_2\ln N+O(1)`$ batches. A [nested-interval protocol](science/growing_round_achievability.md) reaches it by bounding the loss from the first missed localization using the width of the preceding interval.

## Results and their scope

| Question | Supported answer | Proof |
|---|---|---|
| One fixed, nonadaptive batch | Mean-square error of order N to the power minus 1; inherited benchmark | [Attribution](references/RELATED_WORK.md) |
| Two batches, one Hamiltonian update | Sharp mean-square error of order N to the power minus 3/2 | [Converse](science/two_batch_converse.md) and [attainment](science/achievability.md) |
| Retained quantum memory | Does not evade the converse under fresh Gibbs replacement | [Model and sufficiency](science/model.md) |
| Every fixed number r of batches | Matching minimax exponent 2 - 2 to the power (1 - r) | [General converse](science/round_complexity.md) and [explicit attaining arrays](science/fixed_round_achievability.md) |
| Quadratic global precision | Minimum asymptotic depth $`\log_2\ln N+O(1)`$ batches | [Uniform converse](science/round_complexity.md) and [nested-interval attainment](science/growing_round_achievability.md) |

The mechanism is an **entropy budget for integrated thermal sensitivity**. An n-qubit Gibbs thermometer has at most n ln 2 sensitivity area over logarithmic temperature. The first batch determines how concentrated the posterior can become; that concentration limits how much area a retuned second batch can exploit. A calibrated array of degenerate two-level blocks attains the two-batch bound. Differently centered arrays propagate all fixed error moments and attain the full fixed-batch hierarchy.

## Read the science

Start with [the scientific index](science/README.md) and [the exact model](science/model.md). The proof starts with [entropy and sensitivity](science/entropy_budget.md), then develops the [two-batch converse](science/two_batch_converse.md) and [attainment](science/achievability.md). Continue with the [general converse](science/round_complexity.md), [fixed-round construction](science/fixed_round_achievability.md) or [sharp growing-round construction](science/growing_round_achievability.md).

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

The [verification guide](verification/README.md) covers Gibbs and prior identities, finite risk calculations, and checks of the growing-round schedule and star response. The learning check validates the milestones and numerical worked example. The analytical proofs establish the continuum minimax claims.

## Physical and statistical boundaries

Every paid access prepares a **fresh, fully equilibrated Gibbs state** for a chosen temperature-independent Hamiltonian. Input probe correlations do not survive that replacement. Hamiltonians within one batch are fixed before its outcomes are observed; quantum processing, ancillas and retained memory are allowed. The total number of thermalized qubits is bounded on every branch, not only on average.

The fixed-round construction uses an ideal many-body block. The growing-round scheme can also use commuting two-body star probes and measure only their central spins. Pair strengths stay bounded on the chosen temperature interval while the hub degree and aggregate central field grow with the block size. Equilibration time, control work and bounded-degree hardware are separate resources.

The fixed-round hierarchy holds with r fixed independently of N. The growing-round theorem uses a separate schedule with an N-independent risk constant. Optimal leading constants remain open. The [literature comparison](references/RELATED_WORK.md) describes the scope of the comparisons.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
