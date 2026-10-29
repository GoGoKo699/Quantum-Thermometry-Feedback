# De Pasquale–Stace source-to-project bridge

[Learning index](README.md) · [Milestones](MILESTONES.md) · [Worked examples](WORKED_EXAMPLES.md)

## Single selected source

**Antonella De Pasquale and Thomas M. Stace, _Quantum Thermometry_ (2018), [arXiv:1807.05762v1](https://arxiv.org/abs/1807.05762v1).** Use the [16-page arXiv chapter](https://arxiv.org/pdf/1807.05762v1); the page numbers below are its printed pages, not a later book's pagination. Its title page is dated 17 July 2018, while arXiv records submission on 16 July. No second educational anchor is required. Primary research citations in [Related work](../references/RELATED_WORK.md) serve attribution, not an additional prerequisite syllabus.

## Selective source route

| Read in the anchor | Use here | Canonical destination |
|---|---|---|
| Pages 1–4, Eqs. (1)–(6) | Likelihood, classical and quantum Fisher information, measurement optimization | [Model](../science/model.md) |
| Page 5, Eq. (13) | Gibbs energy fluctuations and temperature Fisher information | [Entropy budget](../science/entropy_budget.md) |
| Page 11, Eqs. (28)–(29) and following paragraph | Spectrum optimization and a highly degenerate excited level | [Construction](../science/achievability.md) |
| Pages 11–13, Eqs. (30)–(35) | Contrast independent sampling with sequential, non-reinitialized probe dynamics | [Access-model boundaries](../science/model.md) |

These selections supply the thermal and estimation background. They do not establish this project's finite-feedback minimax law.

## Translate notation before comparing precision

The anchor uses a general parameter lambda, temperature T, inverse temperature beta, and Q(T) for temperature quantum Fisher information. Here the estimated coordinate is the dimensionless quantity x = ln(T/T_ref), with a fixed reference unit T_ref suppressed in the formulas. Changing that reference merely translates x. Set Boltzmann's constant to one, or replace each physical energy by its value divided by Boltzmann's constant.

For one Gibbs probe, the coordinate change gives

```math
F_x=T^2 Q(T)=\frac{\operatorname{Var}(H)}{T^2}=C_H(x).
```

With physical units retained, the last expression is heat capacity divided by Boltzmann's constant. The symbol C_H in this repository is therefore dimensionless. Differentiation always holds the selected Hamiltonian fixed, even when a previous observation selected that Hamiltonian.

The source's N can denote repeated probe measurements. The repository's N is the **total number of thermalized qubit uses**, including calibration. The construction uses n_1 pilot qubits and M blocks of k qubits:

```math
n_1+Mk\le N.
```

Likewise, the source's probe dimension must not be confused with our M, which counts second-batch blocks. Their Hilbert-space dimension is 2 to the power k. A batch is a group whose Hamiltonians are fixed before its data are observed; it is not one qubit or one measurement outcome.

## Bridge 1: local sensitivity is not global risk

Fisher information describes how quickly nearby likelihoods separate at a specified parameter value. A local Cramér–Rao expression does not by itself give the error of a biased finite-sample estimator uniformly over a fixed temperature interval. Nor can a temperature-dependent optimal gap be supplied for free when the temperature is unknown.

The project fixes x in an interval [a,b] of nonzero width and asks for the smallest worst-case mean squared error over complete experiments. Its lower bound uses a smooth prior supported on that same fixed interval and the van Trees inequality. The prior is a mathematical tool for a minimax converse, not extra calibration given to the experimenter. See the [two-batch proof](../science/two_batch_converse.md).

## Bridge 2: trade peak height for sensitivity area

The thermal relation above becomes a global resource constraint by differentiating the entropy with respect to x:

```math
\frac{dS_H}{dx}=C_H(x),\qquad
\int_a^b C_H(x)\,dx\le n\ln 2.
```

An n-qubit state has entropy at most n ln 2. Interactions may concentrate sensitivity into a tall, narrow temperature window; they do not increase this integrated budget. This step is rederived in [entropy_budget.md](../science/entropy_budget.md), with the earlier Bayesian thermometry literature credited there.

## Bridge 3: charge what the calibration actually learned

Let q be a posterior density on [a,b], vanishing at both endpoints. Define its density Fisher information by

```math
I(q)=\int_a^b\frac{q'(x)^2}{q(x)}\,dx.
```

This functional concerns the shape of a density over the unknown parameter. It is not the Fisher information of one Gibbs measurement. Their connection comes from an exact posterior-score identity: the expected posterior density information equals the prior density information plus the experiment's prior-averaged likelihood information.

The [posterior peak lemma](../science/two_batch_converse.md) bounds the height of q by one half of the square root of I(q). Multiplying that height by the thermal sensitivity-area budget bounds what a newly selected Hamiltonian can gain. The first batch gives order N information; the second can add at most order N times the square root of N. Van Trees then gives the global lower bound of order N to the power minus three halves.

## Bridge 4: prove an estimator, not only a Fisher-information scaling

The [attaining protocol](../science/achievability.md) first estimates x using ordinary fixed-gap qubits. It then chooses k and M of order the square root of N, and uses the pilot to center all M degenerate k-qubit blocks. Excitation counts are converted into a smoothed logit and clipped to the physical interval before inversion.

Uniform control matters: a rare, badly centered pilot can make the second measurement almost always ground or almost always excited. The proof controls the exponential moment of the pilot error and includes the zero-count and full-count outcomes. No discarded failure event or uncharged initial estimate is needed. This statistical argument is supplied by the project, not by the educational anchor.

## Bridge 5: do not transfer a different bath-access model

The anchor's sequential protocol can retain a probe between finite-duration contacts. Our theorem instead assumes each paid contact supplies a **fresh, fully equilibrated Gibbs state**. Quantum memory outside that replacement is allowed, but input correlations do not survive it. With fixed Hamiltonian eigenvectors, energy labels are a sufficient statistical refinement for the converse.

Consequently, a transient dynamical thermometer is not an implementation of this theorem merely because it measures temperature. Conversely, the theorem does not exclude better performance in a different access model. The [model](../science/model.md) and [interpretation](../science/interpretation.md) state the exact boundary.

## End of the bridge

Follow [M01–M12](MILESTONES.md) to assemble these prerequisites, then [M13–M30](MILESTONES.md) for the new argument. The matching theorem is complete for two batches. The fixed-r extension is a lower bound only; necessity of at least order log log N batches for quadratic global precision is not a matching many-batch construction.
