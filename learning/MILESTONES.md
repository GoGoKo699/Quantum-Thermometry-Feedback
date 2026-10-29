# Thirty milestones from thermal samples to a feedback law

[Learning index](README.md) · [Selected anchor and notation](ANCHOR.md) · [Worked examples](WORKED_EXAMPLES.md) · [Science index](../science/README.md)

This is a project-defined understanding map, independent of any reader's progress. It has exactly **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background joins thermal probabilities, statistical precision and resource accounting into one experiment. The narrative joins the converse and the attaining protocol into the global feedback law. It does not replace the detailed proofs or claim to cover every technical extension.

**Anchor** below always means De Pasquale–Stace, _Quantum Thermometry_, arXiv:1807.05762v1. Page and equation references use the [bridge's verified source edition](ANCHOR.md). Later, project-specific steps are explicitly sourced to this repository rather than attributed to the anchor.

## Phase I — Background and preliminaries

### M01 — Temperature and an observable reading

**Question:** What does a thermometer actually observe?  
**Target:** Distinguish the reservoir's unknown temperature from the probe energy or excitation count that is measured.  
**Dependencies/story:** None; begin with the physical experiment rather than a precision formula.  
**Connection:** A temperature-dependent distribution makes indirect inference possible.  
**Sources:** Anchor p. 1; [model](../science/model.md), [example 1](WORKED_EXAMPLES.md#example-1-a-fixed-gap-pilot).

### M02 — Gibbs probabilities and degeneracy

**Question:** How do energy and the number of states determine thermal probabilities?  
**Target:** Explain normalization by the partition function and why many equally excited states can offset Boltzmann suppression.  
**Dependencies/story:** M01; identify the probability model for one supplied thermal sample.  
**Connection:** The same mechanism later centers a degenerate block's response.  
**Sources:** Anchor p. 5, Eq. (13), and p. 11; [entropy budget](../science/entropy_budget.md).

### M03 — A record is a likelihood, not a temperature

**Question:** How does a collection of binary outcomes constrain temperature?  
**Target:** Distinguish a Bernoulli probability, a binomial count and an estimate computed from that count.  
**Dependencies/story:** M01–M02; move from a single thermal draw to an experiment's record.  
**Connection:** The pilot and final batch both use count likelihoods but different Hamiltonians.  
**Sources:** Anchor pp. 1–2, Eqs. (2)–(3); [construction](../science/achievability.md).

### M04 — Global logarithmic error

**Question:** Which error is the project trying to minimize?  
**Target:** Interpret squared log-temperature error, a fixed prior interval and worst-case risk; distinguish mean square from root mean square.  
**Dependencies/story:** M03; define the success criterion before discussing sensitivity.  
**Connection:** Local precision and global risk are different claims about the same experiment.  
**Sources:** [Anchor bridge, notation and Bridge 1](ANCHOR.md); [model](../science/model.md).

### M05 — Scores and Fisher information

**Question:** What does a likelihood's derivative measure?  
**Target:** Explain the score as relative likelihood sensitivity, its zero conditional mean, and Fisher information as its second moment.  
**Dependencies/story:** M03–M04; introduce the quantity used in the lower-bound argument.  
**Connection:** Zero-mean scores later make sequential information increments add.  
**Sources:** Anchor p. 2, Eq. (2); [two-batch converse](../science/two_batch_converse.md).

### M06 — Quantum measurement and sufficient energy labels

**Question:** Must the optimal thermal readout be a complicated quantum measurement?  
**Target:** Explain why a fixed Gibbs Hamiltonian supplies a commuting family and why complete energy-basis labels retain its information.  
**Dependencies/story:** M02, M05; connect quantum readout to the thermal probability model.  
**Connection:** This prepares the all-measurement converse without restricting the actual controller to energy readout.  
**Sources:** Anchor pp. 3–5, Eqs. (4)–(6), (13); [model](../science/model.md).

### M07 — Heat capacity in the correct coordinate

**Question:** How does thermal response become information about log temperature?  
**Target:** Translate temperature QFI into log-temperature information and keep Boltzmann's constant and units consistent.  
**Dependencies/story:** M04–M06; identify the thermal quantity controlling statistical sensitivity.  
**Connection:** The result is dimensionless heat capacity, which will be integrated over the unknown interval.  
**Sources:** Anchor Eq. (13); [notation bridge](ANCHOR.md), [entropy budget](../science/entropy_budget.md).

### M08 — Finite Hilbert space and entropy

**Question:** What limits the entropy range of an n-qubit probe?  
**Target:** Explain the dimension 2 to the power n and the entropy ceiling n ln 2, including a possibly degenerate ground space.  
**Dependencies/story:** M02, M07; introduce the finite resource behind the global bound.  
**Connection:** Entropy range, not an imposed Hamiltonian norm, will bound total sensitivity area.  
**Sources:** [Entropy budget](../science/entropy_budget.md), [Bridge 2](ANCHOR.md).

### M09 — A sensitivity peak has a bandwidth

**Question:** Why does high sensitivity at one temperature not imply high sensitivity everywhere?  
**Target:** Relate a degenerate block's tall response peak to its narrow log-temperature window.  
**Dependencies/story:** M02, M07–M08; connect local probe design with uncertain temperature.  
**Connection:** Centering that window is the operational reason to calibrate before retuning.  
**Sources:** Anchor p. 11, Eqs. (28)–(29); [interpretation](../science/interpretation.md).

### M10 — Batches and charged resources

**Question:** Which actions count as an additional feedback opportunity?  
**Target:** Distinguish a qubit, a block, a batch and an inter-batch update; account for every thermalized qubit on every outcome branch.  
**Dependencies/story:** M03, M09; specify the controller's allowed experimental design.  
**Connection:** A free pilot or an expected-only budget would change the theorem.  
**Sources:** [Model](../science/model.md); [Bridge 5](ANCHOR.md), contrasting anchor Eqs. (30)–(35).

### M11 — Prior, posterior and density information

**Question:** What does calibration change about uncertainty?  
**Target:** Distinguish likelihood information from the Fisher functional of a prior or posterior density, and explain conditional inference without Gaussian assumptions.  
**Dependencies/story:** M04–M05, M10; join observed data to adaptive design.  
**Connection:** Posterior concentration determines which part of a new probe's sensitivity area is useful.  
**Sources:** [Bridge 3](ANCHOR.md); [two-batch converse](../science/two_batch_converse.md).

### M12 — The complete global estimation experiment

**Question:** How can an information bound constrain every estimator?  
**Target:** Assemble the physical access, pathwise budget, fixed interval and squared loss, and explain why a fixed smooth-prior Bayes bound lower-bounds minimax risk.  
**Dependencies/story:** M01–M11; synthesize the background into one operational problem.  
**Connection:** Van Trees replaces an unjustified local-unbiased argument; it does not itself construct an estimator.  
**Sources:** [Model](../science/model.md), [van Trees step](../science/two_batch_converse.md); anchor Eq. (1) only as a local contrast.

## Phase II — Narrative and innovation

### M13 — Enlarge the controller without weakening the converse

**Question:** Why can the lower bound cover retained quantum memory?  
**Target:** Follow the simulation that reveals energy-basis indices, then reproduces arbitrary instruments through parameter-independent processing.  
**Dependencies/story:** M06, M10, M12; begin with the precise domain of the theorem.  
**Connection:** Fresh Gibbs replacement makes the refinement valid; partially thermalizing dynamics are outside it.  
**Sources:** [Classical sufficiency](../science/model.md), [Bridge 5](ANCHOR.md).

### M14 — Convert entropy change into a sensitivity-area budget

**Question:** Why is integrated information only extensive?  
**Target:** Derive dS/dx = C and integrate between temperature endpoints, including the ground-state degeneracy boundary.  
**Dependencies/story:** M07–M08, M13; isolate the thermal inequality used by every batch.  
**Connection:** Arbitrary interactions reshape the information curve but preserve its dimension-controlled area.  
**Sources:** [Entropy-area proof](../science/entropy_budget.md); anchor Eq. (13) supplies the thermal starting point.

### M15 — The first batch cannot buy free localization

**Question:** How much information can a fixed nonadaptive thermometer acquire globally?  
**Target:** Bound its prior-averaged likelihood information by the prior height times the entropy-area budget.  
**Dependencies/story:** M11–M14; establish the initial order-N information scale.  
**Connection:** This inherited nonadaptive benchmark is the starting resource, not the new two-batch result.  
**Sources:** [First-batch calculation](../science/two_batch_converse.md), [attribution](../references/RELATED_WORK.md).

### M16 — Bound the height of a posterior

**Question:** How narrow can an informative posterior become?  
**Target:** Explain why a zero-endpoint density must rise to and fall from its maximum, then apply Cauchy–Schwarz to bound that maximum by density Fisher information.  
**Dependencies/story:** M11, M15; turn statistical information into a usable concentration bound.  
**Connection:** The bound applies to non-Gaussian and multimodal posteriors.  
**Sources:** [Posterior peak lemma](../science/two_batch_converse.md); [Bridge 3](ANCHOR.md).

### M17 — Keep calibration information averaged over all records

**Question:** How is posterior information related to the first likelihood?  
**Target:** Derive the exact expected posterior-score identity and identify the zero cross term.  
**Dependencies/story:** M05, M11, M16; connect the density inequality to a paid measurement.  
**Connection:** Conditioning on a favorable calibration record alone would not prove a global bound.  
**Sources:** [Posterior-score identity](../science/two_batch_converse.md).

### M18 — Price the adaptive second batch

**Question:** How much extra sensitivity can one retuning exploit?  
**Target:** Combine posterior height, thermal area and Jensen's inequality while allowing outcome-dependent second-batch sizes.  
**Dependencies/story:** M14, M16–M17; obtain the central adaptive information constraint.  
**Connection:** The remaining qubit budget multiplies the square root of the accumulated information.  
**Sources:** [Conditional second-batch bound](../science/two_batch_converse.md).

### M19 — Obtain a global lower bound for biased estimators

**Question:** Where does the exponent three halves enter the risk?  
**Target:** Combine first- and second-stage information, use the smooth-prior boundary condition, and apply van Trees without assuming unbiasedness.  
**Dependencies/story:** M12, M15, M18; finish the converse at the actual estimation task.  
**Connection:** A lower bound excludes faster error decay but does not establish attainment.  
**Sources:** [Two-batch converse](../science/two_batch_converse.md).

### M20 — Construct a globally identifiable pilot

**Question:** How can ordinary qubits calibrate over the whole interval?  
**Target:** Invert the monotone fixed-gap excitation probability after clipping the sample fraction to its allowed range.  
**Dependencies/story:** M02–M04, M10, M19; begin a concrete experiment that could match the bound.  
**Connection:** The pilot is paid, range-valued and defined for every count.  
**Sources:** [Stage 1](../science/achievability.md), [example 1](WORKED_EXAMPLES.md#example-1-a-fixed-gap-pilot); anchor Eq. (13).

### M21 — Control the full calibration tail

**Question:** Why is a typical pilot error not enough?  
**Target:** Use the positive minimum slope on the fixed interval and a Bernoulli concentration bound to obtain uniform sub-Gaussian error tails.  
**Dependencies/story:** M20; establish the stronger statistical input needed by a sharply tuned probe.  
**Connection:** The proof must survive rare, badly centered pilot outcomes.  
**Sources:** [Pilot tail bound](../science/achievability.md).

### M22 — Choose block size and repetition count together

**Question:** Why are both k and M proportional to the square root of N?  
**Target:** Balance calibration width, probe bandwidth and the identity n_1 + Mk at most N.  
**Dependencies/story:** M09–M10, M21; allocate the experiment's physical samples.  
**Connection:** Local information per block and number of blocks must both be charged.  
**Sources:** [Stage 2](../science/achievability.md), [example 2](WORKED_EXAMPLES.md#example-2-one-complete-budget-and-readout).

### M23 — Turn degeneracy into a tunable response

**Question:** What Hamiltonian implements the desired second batch?  
**Target:** Explain one ground state, 2 to the power k minus one excited states, and a pilot-dependent gap proportional to their log degeneracy.  
**Dependencies/story:** M02, M09, M22; turn resource allocation into a specified Gibbs family.  
**Connection:** The mechanism is inherited probe design used in a new finite-feedback experiment.  
**Sources:** Anchor p. 11, Eqs. (28)–(29); [construction](../science/achievability.md), [related work](../references/RELATED_WORK.md).

### M24 — Retain the complete conditional likelihood

**Question:** How does pilot error affect second-batch counts?  
**Target:** Derive the sigmoid excitation probability and distinguish conditional independence of final counts from unconditional dependence through the pilot.  
**Dependencies/story:** M03, M21, M23; describe the full data-generating experiment.  
**Connection:** Setting the pilot equal to the true temperature would erase the main difficulty.  
**Sources:** [Stage 2 likelihood](../science/achievability.md); anchor Eq. (3) supplies only the elementary product-likelihood background.

### M25 — Define the estimator at extreme counts

**Question:** What happens when every block is ground or every block is excited?  
**Target:** Explain additive smoothing, clipping in the physical logit interval and inversion back to log temperature.  
**Dependencies/story:** M20, M24; make the protocol a complete estimator rather than a sensitivity calculation.  
**Connection:** The inverse Lipschitz bound converts logit error into temperature error.  
**Sources:** [Estimator and uniform logit lemma](../science/achievability.md), [example 2](WORKED_EXAMPLES.md#example-2-one-complete-budget-and-readout).

### M26 — Average rare errors without a logarithmic loss

**Question:** How can a badly centered second batch still have controlled total risk?  
**Target:** Combine the uniform binomial-logit bound with the exponential moment of the pilot error; explain why k squared over n_1 stays bounded.  
**Dependencies/story:** M21–M25; close the global upper-bound argument.  
**Connection:** No failed pilot is discarded, and no shrinking high-probability event substitutes for expected risk.  
**Sources:** [Entire pilot-error distribution](../science/achievability.md).

### M27 — Match the two sides of the theorem

**Question:** What exactly is now optimal?  
**Target:** Match converse and construction under the same interval, loss, feedback count and pathwise budget, including the distinction between squared and root-mean-square error.  
**Dependencies/story:** M19, M26; synthesize the central contribution.  
**Connection:** The law is a two-batch minimax exponent, not a sharp leading constant or a practical-time claim.  
**Sources:** [Converse](../science/two_batch_converse.md), [attainment](../science/achievability.md), [interpretation](../science/interpretation.md).

### M28 — Extend the converse, not the attainment claim

**Question:** What follows for a fixed larger number of batches?  
**Target:** Iterate the posterior-information recurrence and distinguish the exponent 2 minus 2 to the power 1 minus r from a proved optimal hierarchy.  
**Dependencies/story:** M17–M18, M27; extract a justified consequence without changing the supported endpoint.  
**Connection:** A matching construction for r greater than two is not supplied.  
**Sources:** [Fixed-round converse](../science/round_complexity.md).

### M29 — Use uniform constants when rounds grow

**Question:** Why is a fixed-r formula insufficient to bound r as a function of N?  
**Target:** Combine the pointwise quadratic heat-capacity ceiling with the pathwise budget to obtain a round-uniform bound and necessary log-log depth.  
**Dependencies/story:** M10, M14, M28; connect a family of converses to feedback complexity.  
**Connection:** Necessity of log log N batches does not prove sufficiency.  
**Sources:** [Pointwise bound](../science/entropy_budget.md), [uniform recurrence](../science/round_complexity.md).

### M30 — Explain the discovery and its physical boundary

**Question:** What changes in thermometry, and what does not?  
**Target:** Present one coherent account of the finite-feedback law, inherited ingredients, complete estimator, evidence, and limitations on locality, equilibration time and bath access.  
**Dependencies/story:** M12, M27–M29; synthesize both phases into the scientific contribution.  
**Connection:** Distinguish analytical proof, finite-grid checks, unresolved literature coverage and engineering feasibility.  
**Sources:** [Interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md), [verification](../verification/README.md), [anchor bridge](ANCHOR.md).
