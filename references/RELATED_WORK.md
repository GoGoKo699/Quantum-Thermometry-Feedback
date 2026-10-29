# Related work, inherited ingredients and precise novelty boundary

This account separates **what earlier papers establish** from what the present finite-feedback model proves. It is a scoped literature comparison, not an exhaustive priority certificate. See [BibTeX](references.bib), [Model](../science/model.md), [Main theorem](../science/two_batch_converse.md), and [Construction](../science/achievability.md).

## Closest controlling comparator: Mehboudi et al. (2022)

**M. Mehboudi, M. R. Jørgensen, S. Seah, J. B. Brask, J. Kołodyński and M. Perarnau-Llobet**, *Fundamental Limits in Bayesian Thermometry and Attainability via Adaptive Strategies*, Physical Review Letters **128**, 130502 (2022), [DOI](https://doi.org/10.1103/PhysRevLett.128.130502), [arXiv:2108.05932v2](https://arxiv.org/abs/2108.05932).

Their primary article and relevant appendices were examined in the exploration checkpoint. It supplies the Bayesian/van-Trees setup with conditional heat capacity (main Eq. (4), Appendix A), global limitations of nonadaptive many-body thermometry (main Eq. (8) and Appendix B), locally quadratic heat capacities, the degenerate two-level thermometer design, and adaptive gap-tuning strategies. Their reported numerical adaptive examples include large round counts (e.g. $m=2000$ and an appendix example with $m=100$). These are consequential antecedents.

**What is not presented there:** a sharp, uniformly global minimax error exponent for *exactly two* feedback batches under a total qubit budget, with a matching implementation charging all pilot failures. The present proof combines an elementary posterior density-supremum/Fisher inequality with the inherited entropy-area budget to show $J_2=O(N^{3/2})$, then exhibits a global $N^{-3/2}$ attaining estimator with a uniform exponential-moment analysis. The result is not a mere restatement of their general quadratic information ceiling, and it neither denies nor improves their unrestricted many-update conclusions.

The conceptual difference is **a finite allowed number of Hamiltonian retunings**, not a new thermometric Hamiltonian or a stronger generic Bayesian formula.

## Global-loss and Bayesian foundations

- **J. Rubio, J. Anders and L. A. Correa**, *Global Quantum Thermometry*, PRL **127**, 190402 (2021), [DOI](https://doi.org/10.1103/PhysRevLett.127.190402): develops mean logarithmic error and global inference rather than assuming local temperature knowledge. The logarithmic loss is inherited, not invented here.
- **M. R. Jørgensen, J. Kołodyński, M. Mehboudi, M. Perarnau-Llobet and J. B. Brask**, *Bayesian quantum thermometry based on thermodynamic length*, PRA **105**, 042601 (2022), [DOI](https://doi.org/10.1103/PhysRevA.105.042601): a different Bayesian precision geometry based on thermodynamic length. Its alternative loss does not establish the present fixed-round squared-log-temperature theorem.
- **A. De Pasquale and T. M. Stace**, *Quantum Thermometry* (review, 2018), [arXiv:1807.05762](https://arxiv.org/abs/1807.05762): foundational account of thermal-state Fisher information, heat capacity, and probe architectures.

The present minimax theorem fixes its own squared logarithmic loss and complete experiment. It does not assert invariance under an arbitrary alternative loss, although equivalent smooth losses on a fixed compact positive interval share rate exponents.

## Nearby adaptive and dynamical models

- **J. Glatthard et al.**, *Optimal Cold Atom Thermometry Using Adaptive Bayesian Strategies*, PRX Quantum **3**, 040330 (2022), [DOI](https://doi.org/10.1103/PRXQuantum.3.040330): adaptive release–recapture times and realistic cold-atom measurements; no universal two-Gibbs-batch minimax exponent in its stated abstract/model.
- **R. Salvia, M. Mehboudi and M. Perarnau-Llobet**, *Critical Quantum Metrology Assisted by Real-Time Feedback Control*, PRL **130**, 240803 (2023), [DOI](https://doi.org/10.1103/PhysRevLett.130.240803): Bayesian nonadaptive obstruction and adaptive improvement for critical estimation of magnetic fields/couplings, not temperature estimation from full Gibbs replacement with exactly two batches.
- **M. Mehboudi, F. Meier, M. Huber and H. J. D. Miller**, *Optimal limits of continuously monitored thermometers and their Hamiltonian structure*, PRA **111**, L020401 (2025), [DOI](https://doi.org/10.1103/PhysRevA.111.L020401), [arXiv:2408.01313](https://arxiv.org/abs/2408.01313): continuous-time environment-driven trajectories and transition-rate information. That probe/bath-access contract differs from a counted number of fully equilibrated Gibbs snapshots.
- **E. Tumbiolo et al.**, *Shake before Use: Universal Enhancement of Quantum Thermometry by Unitary Driving*, PRL **136**, 250401 (2026), [DOI](https://doi.org/10.1103/z6rz-d9sq): temperature-dependent unitary driving following preparation, an additional dynamical access/control resource not included in the Gibbs replacement model.

## Most recent relevant paper and access limitation

**J. Fan and S. Pang**, *Simultaneously achieving Heisenberg- and Landau-limited precision in equilibrium quantum thermometry*, npj Quantum Information (published 23 October 2026), [DOI](https://doi.org/10.1038/s41534-026-01397-7).

The verified publisher abstract describes a linearly coupled central-probe/ancilla design achieving strong **local** equilibrium thermometric sensitivity, low-temperature Landau behavior and local readout. It improves Hamiltonian engineering assumptions relative to an arbitrary many-body projector. The **full technical text was not accessible in the current research environment**, so we do not claim to have ruled out every theorem within it. The abstract does not state a finite-two-batch global minimax law; no direct subsumption is established on the evidence inspected. Its stronger physical implementation case is not transferred to the present attaining projector without proof. Future priority review should examine this full text before a publication assertion.

### Contribution boundary

| Ingredient or conclusion | Status here |
|---|---|
| Gibbs QFI equals heat capacity; entropy integrated over log temperature bounds sensitivity area | Established earlier; rederived for self-containment |
| Global log loss, Bayesian inference and nonadaptive extensive-information limit | Established earlier; cited |
| Degenerate two-level optimal local probe and adaptive gap tuning | Established earlier; used as a construction ingredient |
| Posterior Fisher-to-peak inequality coupled to thermal sensitivity area across **one feedback boundary** | Central analytical mechanism of this study |
| Tight $R_2^*(N)=\Theta(N^{-3/2})$ including arbitrary within-batch controls and uniformly charged pilot failures | Central supported contribution |
| General $r$-batch converse and $\Omega(\log\log N)$ necessary depth for quadratic risk | Further proved consequence; no matching hierarchy asserted |
| Local-interaction implementation or thermalization-time efficiency | Not established |

## Internal portfolio check (29 October 2026)

The current Guinevere contribution index and registry, searched semantically across venues and classifications, plus GitHub owner-scoped searches for thermometry/temperature, did not reveal an existing project establishing the same two-Gibbs-batch theorem. These are the two closest inspected repositories:

- [Quantum-Precision-Limits](https://github.com/GoGoKo699/Quantum-Precision-Limits/tree/790f9106cde3f72c3c17f54e22d98fad63fcc763): README and science/model.md at that revision concern coherent Bures tomography and local multiparameter Holevo bound evaluation under prepared-state/derivative-oracle access. Its $\varepsilon^{-3/2}$ query-conditioning obstruction is for a different model and is **not** a transfer of the present exponent.
- [Noise-Rate-Activated-Sensing](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/tree/e4c8a7d4f15c3b35dda1507caf7e411502b9b100): README and science/model.md at that revision concern an unknown Hamiltonian frequency, unknown error axis, collision/Markovian sensing and rate feedback under a *time* budget. A shared global-risk mathematical technique does not imply the equilibrium thermal-batch theorem.

There is no claim of an authorized sister relationship, merger or shared manuscript. This is a read-only internal comparison; the present work neither modifies nor inherits permissions in those repositories. Search results and inspected revisions do not constitute an exhaustive guarantee of priority.

## Checks and remaining uncertainty

The main PRL article and the primary model statements were compared at the theorem/operation level, and the local-versus-global and static-versus-continuous-monitoring differences were checked. Several peripheral papers were inspected at the primary abstract level, not reconstructed in full. The recent Fan–Pang full-text gap is material to any later exhaustive priority claim, and independent specialist review of the new proof remains appropriate. The internal scientific statements are not promoted to editorial acceptance or publication certification merely because code tests pass.