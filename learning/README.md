# Learn Quantum Thermometry Feedback

The question is how a finite number of opportunities to retune an equilibrium thermometer changes precision when the temperature is initially unknown over a fixed interval. For every fixed number r of preparation batches, the sharp global squared log-temperature risk is

```math
R_r^*(N)=\Theta_r\!\left(N^{-(2-2^{1-r})}\right).
```

The two-batch experiment is the simplest feedback case and remains the worked starting point.

If the batch count can grow with N, the nested-interval schedule reaches order $`N^{-2}`$ global risk in $`\log_2\ln N+O(1)`$ batches. The matching round-uniform lower bound determines the required batch count up to an additive constant.

The single educational anchor is **De Pasquale and Stace, _Quantum Thermometry_, arXiv:1807.05762v1 (2018)**. Use the [source bridge](ANCHOR.md) for exact locations and translated notation. No complete-book reading assignment is needed.

Start with the [30-milestone map](MILESTONES.md), then the [worked tutorial](TUTORIAL.md). The 14 background targets assemble the experiment. The 16 research targets develop the converse, the two-batch procedure, the weighted array for fixed depth and the nested intervals for growing depth. Each target records its dependencies and scientific sources.

| Reader's question | Route |
|---|---|
| How does a qubit tell us a temperature? | [Counting and likelihood](TUTORIAL.md#one-counting-thermometer) |
| Why is local sensitivity insufficient? | [A narrow peak is not a global guarantee](TUTORIAL.md#a-narrow-peak-is-not-a-global-guarantee) |
| What is the complete one-feedback procedure? | [A finite worked experiment](TUTORIAL.md#a-finite-worked-experiment) |
| Why can no allowed two-batch policy improve the exponent? | [Posterior-information explanation](TUTORIAL.md#why-one-update-has-a-limit), then [the converse](../science/two_batch_converse.md) |
| How can later batches remain useful after an inaccurate calibration record? | [The weighted array](TUTORIAL.md#a-wider-safety-net-for-the-next-batch), then [fixed-round achievability](../science/fixed_round_achievability.md) |
| Which error rates can a fixed batch count attain? | [The sharp fixed-round hierarchy](TUTORIAL.md#the-sharp-fixed-round-hierarchy) |
| How many batches does quadratic global accuracy require? | [The nested-interval schedule](TUTORIAL.md#how-a-growing-schedule-reaches-quadratic-risk) and [the round-uniform converse](../science/round_complexity.md#a-bound-uniform-in-the-number-of-batches) |
| How can one measured spin give a sharp response? | [The star probe](TUTORIAL.md#reading-a-single-spin-in-a-star-probe) |
| Where are the exact assumptions and full proofs? | [Scientific index](../science/README.md) |
| How do the results relate to prior work and physical costs? | [Related work](../references/RELATED_WORK.md) and [physical interpretation](../science/interpretation.md) |

The anchor explains the thermometric foundations. The [scientific account](../science/README.md) supplies the feedback proofs, and [verification](../verification/README.md) provides executable finite checks.
