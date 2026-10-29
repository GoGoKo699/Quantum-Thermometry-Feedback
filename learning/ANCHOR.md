# From Quantum Thermometry to the feedback theorem

[Learning route](README.md) · [Milestone map](MILESTONES.md) · [Worked tutorial](TUTORIAL.md) · [Scientific account](../science/README.md)

## Single educational anchor

**Antonella De Pasquale and Thomas M. Stace, _Quantum Thermometry_ (2018), [arXiv:1807.05762v1](https://arxiv.org/abs/1807.05762v1).** The published book-chapter identifier is [10.1007/978-3-319-99046-0_21](https://doi.org/10.1007/978-3-319-99046-0_21). Page numbers below refer to the 16-page arXiv version, not the pagination of the edited book. Its section headings are unnumbered; the equation numbers supply stable locators.

This is the only educational anchor. Research citations in [Related work](../references/RELATED_WORK.md) remain necessary for attribution; they are not additional prerequisite books.

## Selected source locations

| Source location in v1 | Use in this project | Next project step |
|---|---|---|
| Introduction, p. 1 | Temperature is inferred from observations | [Tutorial: a counting thermometer](TUTORIAL.md#one-counting-thermometer) |
| Quantum estimation theory and quantum metrology, pp. 1–4, Eqs. (1)–(6) | Likelihood, Fisher information, measurement and QFI | Separate local information from global risk |
| Quantum Thermometry, pp. 5–6, Eq. (13) | Thermal QFI and heat capacity | [Log-temperature conversion](#notation-and-normalization) |
| Fundamental limitations on temperature estimation with individual quantum probes, p. 11, Eqs. (28)–(29) and following paragraph | Energy-spectrum design and degenerate probes | [Tuned blocks](../science/achievability.md#stage-2-retuned-degenerate-thermal-blocks) |
| Single-qubit thermometry through sequential measurements, pp. 11–14, Eqs. (30)–(35) | Conditional likelihoods and the meaning of repeated access | Contrast dynamical reuse with fresh Gibbs replacement |

The Heisenberg Limited Thermometry subsection on pp. 6–7 and the Global versus Local Measurements discussion on pp. 7–9 are useful **contrasts**, not extra assumptions imported into this project. The former uses a different dynamical interaction; the latter concerns access to spatial subsystems. Neither establishes the present two-batch minimax result.

## Notation and normalization

Use a fixed temperature unit and set Boltzmann's constant to one in the project equations. Logarithmic estimation error is independent of that unit: it is always the log of the ratio of estimated and true temperature.

| Anchor notation | Repository notation and meaning |
|---|---|
| General parameter lambda | Temperature T, then x = ln T |
| Q(T), thermal quantum Fisher information | F_H(x), information for log temperature |
| c_v, physical heat capacity | C_H = c_v / k_B, dimensionless heat capacity |
| N, repeated probes in a fixed experiment | N, total thermalized-qubit budget across all batches |
| M, Hilbert-space dimension in spectrum design | D = 2^k for one k-qubit block; M instead counts blocks here |
| Delta T, root mean-square error in local bounds | R, global mean-square log error; its square root is the corresponding root error |

Changing the parameter changes Fisher information. Since dx/dT = 1/T, the score for x is T times the score for T. Therefore

```math
F_H(x)=T^2Q(T)=\frac{c_v}{k_B}.
```

With k_B = 1 this becomes

```math
F_H(x)=e^{-2x}\mathrm{Var}_x(H)=C_H(x).
```

Do not read the anchor's local root-error formula as a global minimax guarantee. A local Cramer–Rao statement has estimator and regularity conditions; our lower bound uses a fixed smooth prior and van Trees to cover biased estimators. The complete proof is in [the converse](../science/two_batch_converse.md).

## Three bridges supplied here

**Sensitivity over an interval.** Heat capacity is a pointwise sensitivity. The project integrates it over log temperature using dS/dx = C_H. The resulting area cannot exceed the logarithm of the Hilbert-space dimension. This step and its nonadaptive application are credited to earlier Bayesian thermometry research in [Related work](../references/RELATED_WORK.md), rather than attributed to this educational source.

**Feedback and the posterior.** After the first batch, the remaining uncertainty is a probability density conditioned on the observed record. Its maximum height is bounded by half the square root of its density Fisher information. This converts a thermal sensitivity-area budget into a bound on how much information the retuned second batch can acquire. The [tutorial](TUTORIAL.md#why-one-update-has-a-limit) develops the argument; the [proof](../science/two_batch_converse.md) supplies the quantifiers and endpoint conditions.

**An estimator, not just sensitivity.** A high information peak alone does not exhibit an estimator with small worst-case error. The project supplies a globally identifiable pilot, a smoothed second-batch count estimator, clipping and an exponential-moment argument that includes rare pilot failures. Those steps, and the sharp two-batch law, are not claimed as content of the 2018 anchor.

## Distinctions to keep while reading

The anchor's spatially global measurements are not the same concept as this project's statistically global estimation over a fixed temperature interval. Its sequential unreset probe dynamics are also not the same operation as preparing a new full Gibbs state in each paid use. In this repository, outcomes may change the next batch's Hamiltonian only at the stated feedback boundary. Quantum memories may be retained, but correlations with an input probe do not survive its full replacement.

The anchor's extensive-energy example does not justify assuming extensive heat capacity for all allowed many-body probes. Here narrow peaks can be quadratic in block size; the universal constraint is their **integrated area**. Conversely, the attaining diagonal block protocol does not require entangled preparation merely because the underlying theory is quantum.

## Reading sequence

Read the source locations in the table selectively, then follow [M01–M14](MILESTONES.md#background-and-preliminaries) to assemble the experiment. The [worked tutorial](TUTORIAL.md) supplies the bridge to [M15–M30](MILESTONES.md#narrative-and-innovation). Specialists can instead go directly from [the model](../science/model.md) to [the lower bound](../science/two_batch_converse.md) and [the construction](../science/achievability.md).
