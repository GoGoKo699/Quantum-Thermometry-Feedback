# Thirty milestones

[Learning route](README.md) · [Single anchor](ANCHOR.md) · [Worked tutorial](TUTORIAL.md) · [Scientific account](../science/README.md)

The map contains exactly **30 project-defined understanding targets**. M01–M14 are background/preliminaries; M15–M30 are narrative/innovation. Fourteen foundations are needed to align thermodynamics, global statistics and the access model before sixteen targets assemble the converse, construction and consequences. Each phase progresses from individual objects to an integrated scientific account. This is a shared conceptual route, not a record of assessments or a catalogue of every technical lemma.

Every source mention of the anchor refers to **De Pasquale and Stace, Quantum Thermometry, arXiv:1807.05762v1 (2018)**; see the [source bridge](ANCHOR.md) for page and notation conventions. The primary research dependencies remain in [Related work](../references/RELATED_WORK.md).

## Background and preliminaries

### M01 — Temperature as an inference task

**Phase:** Background/preliminaries.

**Central question:** What observation can reveal a temperature that is not directly read out?

**Understanding target:** Distinguish the fixed unknown bath parameter from a random measurement result.

**Dependencies:** None; entry point.

**Conceptual connection and story role:** Moves from a physical sample to a statistical task.

**Source pointers:** Anchor introduction, p. 1; [counting thermometer](TUTORIAL.md#one-counting-thermometer).

### M02 — Gibbs weights and energy levels

**Phase:** Background/preliminaries.

**Central question:** How does equilibrium determine the probabilities of energy outcomes?

**Understanding target:** Explain normalization by the partition function and the role of the fixed Hamiltonian.

**Dependencies:** M01.

**Conceptual connection and story role:** Connects temperature to a concrete probability distribution.

**Source pointers:** Anchor thermal-state discussion, p. 5; [Gibbs contract](../science/model.md#gibbs-preparation-contract).

### M03 — Qubit counts

**Phase:** Background/preliminaries.

**Central question:** What information does an excitation count contain?

**Understanding target:** Relate a Bernoulli outcome and its binomial count to a temperature-dependent excitation probability.

**Dependencies:** M02.

**Conceptual connection and story role:** Turns a state model into data.

**Source pointers:** Anchor single-probe discussion, p. 11; [counting thermometer](TUTORIAL.md#one-counting-thermometer).

### M04 — Likelihood and estimator

**Phase:** Background/preliminaries.

**Central question:** How are observed data converted into an estimate?

**Understanding target:** Separate the likelihood as a function of candidate temperature from the estimator as a rule on data.

**Dependencies:** M03.

**Conceptual connection and story role:** Connects random counts to a reported answer.

**Source pointers:** Anchor Eq. (3), p. 2; [pilot](../science/achievability.md#stage-1-fixed-globally-identifiable-pilot).

### M05 — Loss and global risk

**Phase:** Background/preliminaries.

**Central question:** Which error is being minimized, and over which temperatures?

**Understanding target:** Distinguish squared log error, root error, Bayes averaging and worst-case risk on a fixed interval.

**Dependencies:** M04.

**Conceptual connection and story role:** Defines success before optimizing a probe.

**Source pointers:** [Loss and minimax task](../science/model.md#parameter-and-loss); [budget and error](TUTORIAL.md#what-the-budget-and-the-error-mean). This global criterion is a project bridge beyond the anchor.

### M06 — Classical and quantum Fisher information

**Phase:** Background/preliminaries.

**Central question:** What does the sensitivity of a likelihood measure?

**Understanding target:** Interpret the score and Fisher information and distinguish a chosen measurement from QFI optimized over measurements.

**Dependencies:** M04.

**Conceptual connection and story role:** Connects a local probability change to measurement design.

**Source pointers:** Anchor Eqs. (1)–(6), pp. 2–4; [thermal information](../science/entropy_budget.md#gibbs-information-in-logarithmic-temperature).

### M07 — Log-temperature coordinates

**Phase:** Background/preliminaries.

**Central question:** Why must Fisher information change when the parameter is changed?

**Understanding target:** Use the chain rule to obtain F_H(x) = T squared times Q(T), with x = ln T.

**Dependencies:** M05, M06.

**Conceptual connection and story role:** Aligns the precision metric with the chosen global loss.

**Source pointers:** Anchor Eq. (13), p. 5; [notation conversion](ANCHOR.md#notation-and-normalization).

### M08 — Energy fluctuations and heat capacity

**Phase:** Background/preliminaries.

**Central question:** Why are thermal fluctuations informative rather than merely noise?

**Understanding target:** Relate Gibbs energy variance to heat capacity and log-temperature Fisher information without assuming a particular spectrum.

**Dependencies:** M02, M07.

**Conceptual connection and story role:** Joins thermodynamics and estimation.

**Source pointers:** Anchor Eqs. (13) and (28), pp. 5 and 11; [thermal identity](../science/entropy_budget.md#gibbs-information-in-logarithmic-temperature).

### M09 — Sufficient energy records

**Phase:** Background/preliminaries.

**Central question:** Why can the converse allow arbitrary quantum measurements?

**Understanding target:** Explain how energy-basis labels generate the commuting Gibbs family through parameter-independent preparation.

**Dependencies:** M02, M06.

**Conceptual connection and story role:** Connects quantum readout to a stronger classical statistical experiment.

**Source pointers:** [Memory and sufficiency](../science/model.md#allowable-measurements-and-memory); anchor energy-measurement discussion, pp. 5–6.

### M10 — Entropy and dimension

**Phase:** Background/preliminaries.

**Central question:** What limits the total entropy range of a finite probe?

**Understanding target:** Read dimension D = 2 to the power n as an entropy ceiling n ln 2, using natural logarithms.

**Dependencies:** M02.

**Conceptual connection and story role:** Supplies the thermodynamic budget for the forthcoming converse.

**Source pointers:** [Entropy-area derivation](../science/entropy_budget.md#integrated-area-bound). The entropy-budget step is supplied by the repository and its primary sources, not assumed from the anchor.

### M11 — Conditional uncertainty

**Phase:** Background/preliminaries.

**Central question:** What changes after the first record is observed?

**Understanding target:** Form a posterior from a prior and a normalized likelihood, and distinguish density Fisher information from likelihood Fisher information.

**Dependencies:** M04, M06.

**Conceptual connection and story role:** Makes feedback a conditional statistical decision.

**Source pointers:** [Prior and posterior](../science/two_batch_converse.md#a-fixed-global-prior); [posterior explanation](TUTORIAL.md#why-one-update-has-a-limit).

### M12 — Pathwise qubit accounting

**Phase:** Background/preliminaries.

**Central question:** Which resources are charged even on unfavorable outcomes?

**Understanding target:** Count reused qubits, interacting blocks and calibration on every branch, rather than charging only successful runs or expected usage.

**Dependencies:** M03, M05.

**Conceptual connection and story role:** Turns a precision claim into a matched resource comparison.

**Source pointers:** [Resource convention](../science/model.md#resources-and-scope); [finite experiment](TUTORIAL.md#a-finite-worked-experiment).

### M13 — Equilibrium access versus dynamics

**Phase:** Background/preliminaries.

**Central question:** When would a different thermometry experiment fall outside the theorem?

**Understanding target:** Separate full Gibbs replacement from partial thermalization, coherent bath access and repeated unreset probe dynamics.

**Dependencies:** M09, M12.

**Conceptual connection and story role:** Clarifies why a retained memory does not imply retained probe correlations.

**Source pointers:** Anchor sequential-measurement discussion, pp. 11–14, Eqs. (30)–(35); [access contract](../science/model.md#gibbs-preparation-contract).

### M14 — The complete two-batch experiment

**Phase:** Background/preliminaries.

**Central question:** What is fixed before and after the single feedback boundary?

**Understanding target:** State the common interval, allowed controls, output loss, two-batch timing and all-branch budget as one operational task.

**Dependencies:** M05, M08, M11, M12, M13.

**Conceptual connection and story role:** Integrates the background into the exact experiment being compared.

**Source pointers:** [Full model](../science/model.md); [learning synthesis](TUTORIAL.md#what-the-budget-and-the-error-mean).

## Narrative and innovation

### M15 — Entropy derivative

**Phase:** Narrative/innovation.

**Central question:** Why does integrating thermal sensitivity measure an entropy change?

**Understanding target:** Derive or explain dS/dx = C_H for a fixed Hamiltonian and identify what is held fixed in the derivative.

**Dependencies:** M08, M10, M14.

**Conceptual connection and story role:** Starts the new argument with a local thermodynamic identity.

**Source pointers:** [Entropy identity](../science/entropy_budget.md#integrated-area-bound).

### M16 — Sensitivity area

**Phase:** Narrative/innovation.

**Central question:** Why can a sharper many-body thermometer still be globally limited?

**Understanding target:** Use the entropy range to bound the sensitivity area by n ln 2 and distinguish peak height from bandwidth.

**Dependencies:** M15.

**Conceptual connection and story role:** Turns the identity into a universal probe-design resource bound.

**Source pointers:** [Area budget](../science/entropy_budget.md#integrated-area-bound); [narrow peaks](TUTORIAL.md#a-narrow-peak-is-not-a-global-guarantee).

### M17 — A test prior for minimax risk

**Phase:** Narrative/innovation.

**Central question:** Why may a proof introduce a prior when the operational task is worst-case?

**Understanding target:** Explain worst-case domination of a fixed prior average and why vanishing endpoint density removes a boundary term.

**Dependencies:** M05, M11, M16.

**Conceptual connection and story role:** Connects a global task to a usable integral inequality without giving free calibration.

**Source pointers:** [Sine-squared prior](../science/two_batch_converse.md#a-fixed-global-prior).

### M18 — Posterior score identity

**Phase:** Narrative/innovation.

**Central question:** How much concentration can the first batch generate on average?

**Understanding target:** Explain the cancellation of the prior–likelihood score cross term and the resulting O(N) mean posterior information.

**Dependencies:** M11, M16, M17.

**Conceptual connection and story role:** Pays explicitly for the information used to tune the second batch.

**Source pointers:** [First-batch information](../science/two_batch_converse.md#information-after-the-first-batch).

### M19 — Posterior height bound

**Phase:** Narrative/innovation.

**Central question:** What prevents a posterior from becoming arbitrarily tall at fixed Fisher information?

**Understanding target:** Connect zero endpoint values, total variation and Cauchy–Schwarz to the maximum-density bound.

**Dependencies:** M17, M18.

**Conceptual connection and story role:** Converts information into the posterior height that can weight a sensitivity peak.

**Source pointers:** [Peak lemma](../science/two_batch_converse.md#posterior-peak-lemma).

### M20 — Adaptive information budget

**Phase:** Narrative/innovation.

**Central question:** How much can one chosen second Hamiltonian exploit the first record?

**Understanding target:** Apply the area bound history by history, then average the posterior height bound with Jensen, keeping conditional controls fixed under differentiation.

**Dependencies:** M16, M18, M19.

**Conceptual connection and story role:** Produces the O(N to the power 3/2) full-experiment information ceiling.

**Source pointers:** [Conditional second batch](../science/two_batch_converse.md#conditional-second-batch-bound).

### M21 — Global error from information

**Phase:** Narrative/innovation.

**Central question:** Why does the converse also cover biased estimators?

**Understanding target:** Explain the integration-by-parts basis of van Trees and why a local unbiasedness assumption is not needed.

**Dependencies:** M17, M20.

**Conceptual connection and story role:** Turns a ceiling on total information into a floor on actual global risk.

**Source pointers:** [Error bound](../science/two_batch_converse.md#turning-information-into-global-error).

### M22 — The universal two-batch obstruction

**Phase:** Narrative/innovation.

**Central question:** Which alternatives does the lower bound really exclude?

**Understanding target:** Combine sufficiency, the pathwise budget and the posterior argument to state the lower bound with its complete assumptions.

**Dependencies:** M09, M13, M20, M21.

**Conceptual connection and story role:** Integrates the converse and identifies its receiving model.

**Source pointers:** [Converse statement](../science/two_batch_converse.md#statement); [model](../science/model.md).

### M23 — Uniform pilot calibration

**Phase:** Narrative/innovation.

**Central question:** How can an ordinary qubit batch localize every temperature in the interval?

**Understanding target:** Use monotonicity, a bounded inverse derivative, clipping and a binomial concentration bound to control the entire pilot distribution.

**Dependencies:** M03, M04, M12, M14.

**Conceptual connection and story role:** Begins the attaining construction with a paid, globally identifiable first stage.

**Source pointers:** [Pilot proof](../science/achievability.md#stage-1-fixed-globally-identifiable-pilot).

### M24 — Tuned degenerate blocks

**Phase:** Narrative/innovation.

**Central question:** Why choose both block size and block count proportional to the square root of N?

**Understanding target:** Connect pilot error width, sensitivity width, degeneracy, gap choice and the remaining qubit budget.

**Dependencies:** M08, M16, M23.

**Conceptual connection and story role:** Matches the second design to what the pilot actually knows.

**Source pointers:** Anchor spectrum-design discussion, p. 11; [tuned-block construction](../science/achievability.md#stage-2-retuned-degenerate-thermal-blocks).

### M25 — Finite estimators at all counts

**Phase:** Narrative/innovation.

**Central question:** How does the final estimator avoid infinities and remain valid at saturated counts?

**Understanding target:** Explain smoothing, projection, inverse-map stability and the uniform binomial-logit risk lemma.

**Dependencies:** M04, M05, M24.

**Conceptual connection and story role:** Converts designed sensitivity into a defined estimator on every data record.

**Source pointers:** [Estimator](../science/achievability.md#explicit-estimator-including-endpoints); [uniform lemma](../science/achievability.md#uniform-binomial-logit-lemma).

### M26 — Rare calibration failures

**Phase:** Narrative/innovation.

**Central question:** Why is a high-probability calibration statement insufficient by itself?

**Understanding target:** Identify exponential error amplification and show why the pilot tail controls its expectation without postselection or a logarithmic loss.

**Dependencies:** M23, M24, M25.

**Conceptual connection and story role:** Completes the uniform upper bound rather than relying only on typical records.

**Source pointers:** [Full-distribution proof](../science/achievability.md#charge-the-entire-pilot-error-distribution).

### M27 — The matching minimax law

**Phase:** Narrative/innovation.

**Central question:** Why do the upper and lower arguments establish one sharp exponent?

**Understanding target:** Match interval, loss, quantum access, feedback count and total budget on both sides before concluding Theta(N to the power minus 3/2).

**Dependencies:** M22, M26.

**Conceptual connection and story role:** Integrates the main contribution and separates rate optimality from an optimal leading constant.

**Source pointers:** [Scientific synthesis](../science/README.md#principal-statements); [interpretation](../science/interpretation.md#one-feedback-action-is-an-information-resource).

### M28 — Fixed-round recurrence

**Phase:** Narrative/innovation.

**Central question:** What can be concluded for a larger but fixed number of batches?

**Understanding target:** Iterate the posterior-information recurrence and label the exponent 2 - 2 to the power (1 - r) as a lower-bound result unless attainment is separately proved.

**Dependencies:** M18, M19, M20, M27.

**Conceptual connection and story role:** Extends the obstruction without silently extending the constructive theorem.

**Source pointers:** [Fixed-r proof](../science/round_complexity.md#fixed-r-global-risk-lower-bounds).

### M29 — Growing feedback depth

**Phase:** Narrative/innovation.

**Central question:** Why cannot a fixed-r constant be reused when r grows with N?

**Understanding target:** Explain the separate pointwise heat-capacity ceiling, pathwise squared-size sum and round-uniform information bound behind the necessary log-log round count.

**Dependencies:** M12, M16, M28.

**Conceptual connection and story role:** Distinguishes a necessary asymptotic control resource from a sufficient schedule.

**Source pointers:** [Uniform depth argument](../science/round_complexity.md#a-bound-uniform-in-the-number-of-batches); [pointwise thermal bound](../science/entropy_budget.md#separate-pointwise-upper-bound).

### M30 — The scientific contribution as a whole

**Phase:** Narrative/innovation.

**Central question:** What changes in thermometric capability, and what still needs a different theorem?

**Understanding target:** Connect inherited Bayesian and probe-design ingredients to the new finite-feedback law; distinguish checked examples, proved rates, ideal resources and unproved higher-round or hardware extensions.

**Dependencies:** M13, M27, M28, M29.

**Conceptual connection and story role:** Closes the narrative with the mechanism, evidence, novelty and boundaries in one account.

**Source pointers:** [Interpretation](../science/interpretation.md); [Related work](../references/RELATED_WORK.md); [verification](../verification/README.md); [anchor boundary](ANCHOR.md#three-bridges-supplied-here).
