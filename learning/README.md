# Learn Quantum Thermometry Feedback

The question is how a finite number of opportunities to retune an equilibrium thermometer changes precision when the temperature is initially unknown over a fixed interval. For every fixed number r of preparation batches, the sharp global squared log-temperature risk is

```math
R_r^*(N)=\Theta_r\!\left(N^{-(2-2^{1-r})}\right).
```

The two-batch experiment is the simplest feedback case and remains the worked starting point.

The single educational anchor is **De Pasquale and Stace, _Quantum Thermometry_, arXiv:1807.05762v1 (2018)**. Use the [source bridge](ANCHOR.md) for exact locations and translated notation. No complete-book reading assignment is needed.

Start with the [30-milestone map](MILESTONES.md), then the [worked tutorial](TUTORIAL.md). The map has **14 background/preliminaries targets** and **16 narrative/innovation targets**: the first phase assembles the experiment; the second develops the converse, the two-batch procedure, the robust array that attains every fixed-round exponent, and the physical limits. Each target records its dependencies and scientific sources. It describes the project independently of any reader's assessment history.

| Reader's question | Route |
|---|---|
| How does a qubit tell us a temperature? | [Counting and likelihood](TUTORIAL.md#one-counting-thermometer) |
| Why is local sensitivity insufficient? | [A narrow peak is not a global guarantee](TUTORIAL.md#a-narrow-peak-is-not-a-global-guarantee) |
| What is the complete one-feedback procedure? | [A finite worked experiment](TUTORIAL.md#a-finite-worked-experiment) |
| Why can no allowed two-batch policy improve the exponent? | [Posterior-information explanation](TUTORIAL.md#why-one-update-has-a-limit), then [the converse](../science/two_batch_converse.md) |
| How can later batches remain useful after an inaccurate calibration record? | [The weighted array](TUTORIAL.md#a-wider-safety-net-for-the-next-batch), then [fixed-round achievability](../science/fixed_round_achievability.md) |
| Which rates are attained, and what changes when the batch count grows? | [The sharp hierarchy](TUTORIAL.md#the-sharp-fixed-round-hierarchy) and [the growing-depth boundary](TUTORIAL.md#why-fixed-round-attainment-does-not-settle-growing-depth) |
| Where are the exact assumptions and full proofs? | [Scientific index](../science/README.md) |
| Which conclusions are inherited, new, or unproved? | [Related work](../references/RELATED_WORK.md) and [scope](../science/interpretation.md) |

The research-level inequalities and rare-event proof are developed in the repository. The anchor explains their thermometric foundation; it does not replace them. [Verification](../verification/README.md) provides executable finite checks, not an alternative to the proofs.
