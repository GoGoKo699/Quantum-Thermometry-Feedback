# Learn Quantum Thermometry Feedback

A thermometer can be very sensitive near one temperature and nearly useless elsewhere. This project asks what happens when the unknown temperature spans a fixed interval and there is only one opportunity to retune the thermometer after seeing data.

The single educational anchor is **Antonella De Pasquale and Thomas M. Stace, _Quantum Thermometry_, arXiv:1807.05762v1 (2018)**. Start with the [source-to-project bridge](ANCHOR.md), which selects the relevant pages, translates notation and distinguishes the review's local precision statements from this project's global risk theorem.

The [30-milestone map](MILESTONES.md) contains **12 background/preliminaries targets and 18 narrative/innovation targets**. The first phase assembles the statistical and thermal ingredients into the complete experiment. The second connects the information bound and the attaining construction, ending with their physical interpretation. The map is common to all readers; it is not an assessment record or a prerequisite to reading the science.

## Reading routes

| Aim | Route |
|---|---|
| Understand the physical question | [Worked examples](WORKED_EXAMPLES.md) → [interpretation](../science/interpretation.md) |
| Follow the whole conceptual story | [Anchor bridge](ANCHOR.md) → [M01–M30](MILESTONES.md) → [science index](../science/README.md) |
| Inspect the impossibility argument | [Model](../science/model.md) → [entropy budget](../science/entropy_budget.md) → [two-batch converse](../science/two_batch_converse.md) |
| Inspect the implementation and its statistics | [Construction](../science/achievability.md) → [worked numerical example](WORKED_EXAMPLES.md) → [verification](../verification/README.md) |
| Check what is new or remains unproved | [Related work](../references/RELATED_WORK.md) → [round-count limits](../science/round_complexity.md) |

The central result concerns **mean squared logarithmic error**, not its square root:

```math
R_2^*(N)=\Theta(N^{-3/2}).
```

Thus the corresponding root-mean-square logarithmic error has order N to the power minus three quarters. All calibration and final-readout thermalized qubits count toward N. The result does not establish a thermalization-time advantage.

The shared learning materials explain the project. Exact quantifiers, proofs and research citations remain in their authoritative [science](../science/README.md) and [reference](../references/RELATED_WORK.md) pages.
