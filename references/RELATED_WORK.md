# Related work, inherited ingredients and precise novelty boundary

This account separates **what earlier papers establish** from what the present finite-feedback model proves. It is a scoped literature comparison, not an exhaustive priority certificate. See [BibTeX](references.bib), [Model](../science/model.md), [Two-batch theorem](../science/two_batch_converse.md), and [Feedback hierarchy](../science/round_complexity.md).

## Closest controlling comparator: Mehboudi et al. (2022)

**M. Mehboudi, M. R. Jørgensen, S. Seah, J. B. Brask, J. Kołodyński and M. Perarnau-Llobet**, *Fundamental Limits in Bayesian Thermometry and Attainability via Adaptive Strategies*, Physical Review Letters **128**, 130502 (2022), [DOI](https://doi.org/10.1103/PhysRevLett.128.130502), [arXiv:2108.05932v2](https://arxiv.org/abs/2108.05932).

The relevant primary text supplies the Bayesian/van-Trees formulation (Eq. (4), Appendix A), the nonadaptive limitation (Eq. (8), Appendix B), degenerate two-level probes, and adaptive gap tuning. Its experiment has $N=mn$ probes in $m$ successive groups. The aggregate information bound permits order $mn^2$ sensitivity; adaptive numerical examples use large $m$, including $m=2000$. These are inherited foundations. Their bound and numerical saturation do not determine the sharp global minimax exponent as $N\to\infty$ with the number of updates fixed. A finite-range numerical slope close to two does not settle that limiting order.

Here the feedback count is an explicit resource. The [existing posterior-information converse](../science/round_complexity.md) gives exponent $2-2^{1-r}$ for every fixed number $r$ of batches. The original [two-batch construction](../science/achievability.md) attains the $r=2$ case. The added [hedged-array construction](../science/fixed_round_achievability.md) closes the upper-bound gap for every fixed $r$: it spreads each refinement batch across a finite array of differently centered copies of the inherited degenerate probe, then inverts their aggregate response. Polynomially decaying multiplicities make the refinement robust to imperfect previous estimates. An all-fixed-moments bound charges unfavorable histories and can be iterated a fixed number of times. This replaces the unsupported iteration of a single-center exponential-moment argument.

The resulting $R_r^*(N)=\Theta_r(N^{-(2-2^{1-r})})$ is a statement about **global risk at fixed feedback depth**. The prior probe design, adaptive principle, entropy-area ingredient, fixed-$r$ converse, and two-batch result are not new in this extension. Neither the present fixed-$r$ constants nor earlier many-update examples establish an $O(\log\log N)$-batch, $O(N^{-2})$ schedule with a uniform constant.

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
- **J. López González, M. Mehboudi, A. Sanpera and M. García Díaz**, *Quantum thermometry with $k$-local Hamiltonians*, [arXiv:2611.18327v1](https://arxiv.org/abs/2611.18327v1), submitted 13 November 2026: Sec. II.2 defines precision through local QFI and large-sample Cramér–Rao estimation; Sec. II.3 and the subsequent constructions optimize heat capacity under interaction-locality restrictions. This is a relevant route toward physically simpler probes, but it does not provide the finite-feedback global-risk theorem. A local sensitivity approximation cannot be substituted for the complete likelihood and tail bounds needed by the present array.

The array's concentration estimate uses the established bounded-independent-variable inequality of **W. Hoeffding**, *Probability Inequalities for Sums of Bounded Random Variables*, JASA **58**, 13–30 (1963), [DOI](https://doi.org/10.1080/01621459.1963.10500830). The new ingredient is its use with the hedged Gibbs response to propagate all fixed error moments, not a new concentration inequality.

## Recent physical-design comparator and access limitation

**J. Fan and S. Pang**, *Simultaneously achieving Heisenberg- and Landau-limited precision in equilibrium quantum thermometry*, npj Quantum Information (published 23 October 2026), [DOI](https://doi.org/10.1038/s41534-026-01397-7).

The publisher abstract describes a linearly coupled central-probe/ancilla design with Heisenberg scaling, low-temperature Landau behavior and local readout. The abstract and publication metadata were checked again on 18 November 2026; the official article and PDF routes did not provide the full technical text. Thus **only the abstract-level comparison is available**. It does not state a fixed-feedback global minimax hierarchy, but that absence is not a full-text exclusion of overlap. Its physical implementation claims are not transferred to the present many-body Gibbs blocks. A manuscript priority review should resolve this bounded full-text gap before asserting exhaustive novelty.

### Contribution boundary

| Ingredient or conclusion | Status here |
|---|---|
| Gibbs QFI equals heat capacity; entropy integrated over log temperature bounds sensitivity area | Established earlier; rederived for self-containment |
| Global log loss, Bayesian inference and nonadaptive extensive-information limit | Established earlier; cited |
| Degenerate two-level optimal local probe and adaptive gap tuning | Established earlier; used as a construction ingredient |
| Posterior Fisher-to-peak inequality coupled to thermal sensitivity area across **one feedback boundary** | Central analytical mechanism of this study |
| Tight $R_2^*(N)=\Theta(N^{-3/2})$ including arbitrary within-batch controls and uniformly charged pilot failures | Previously established two-batch result; retained |
| General fixed-$r$ converse and $\Omega(\log\log N)$ necessary depth for quadratic risk | Previously established here; retained |
| Finite hedged Gibbs array, inverse-response estimator and all-fixed-moment refinement | Added constructive mechanism |
| Tight $R_r^*(N)=\Theta_r(N^{-(2-2^{1-r})})$ for every fixed integer $r\ge1$ | Added matching hierarchy; constants may depend on $r$ |
| $O(\log\log N)$-batch sufficiency for $O(N^{-2})$ global risk | Not established by the fixed-$r$ construction |
| Local-interaction implementation or thermalization-time efficiency | Not established |

## Related public research models

The following source comparisons concern scientific assumptions and resources. Similar loss functions or exponents alone do not transfer their conclusions.

| Public account and inspected source | Different task or access model |
|---|---|
| [Quantum Thermometry Locality](https://github.com/GoGoKo699/Quantum-Thermometry-Locality/tree/a6fd4978295f1f09d28d2adc4819cf53858be17f), complete README and [model](https://github.com/GoGoKo699/Quantum-Thermometry-Locality/blob/a6fd4978295f1f09d28d2adc4819cf53858be17f/science/model_and_results.md), inspected 18 November 2026 | One initially thermal XX half-chain, contact restricted to its first $s$ sites and elapsed time $t$; attained squared log-temperature risk $\Theta((s+Jt/\hbar)^{-1})$. It supplies no fresh Gibbs replacements or arbitrary thermometer Hamiltonians. Its contact/time law neither gives nor contradicts the present charged-qubit/feedback hierarchy. |
| [Quantum Precision Limits](https://github.com/GoGoKo699/Quantum-Precision-Limits/tree/790f9106cde3f72c3c17f54e22d98fad63fcc763), README and science/model.md at the earlier inspected revision | Coherent Bures tomography and local multiparameter Holevo-bound evaluation with prepared-state/derivative-oracle access. Its $\varepsilon^{-3/2}$ query obstruction is a different estimation problem. |
| [Noise Rate Activated Sensing](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/tree/e4c8a7d4f15c3b35dda1507caf7e411502b9b100), README and science/model.md at the earlier inspected revision | Unknown Hamiltonian frequency and transverse error axis under collision/Markovian sensing with rate control and a time budget. Shared global-estimation techniques do not imply the equilibrium replacement theorem. |

## Checks and remaining uncertainty

The Mehboudi article's relevant main-text bounds, adaptive model and numerical limiting regime were rechecked against arXiv:2108.05932v2. The November 2026 $k$-local preprint was inspected through its thermometry model, local-QFI objective and spectral construction statements; no claim of a complete reconstruction of all numerical optimizations is made. Several peripheral papers retain primary-abstract-level comparison only. The Fan–Pang full-text gap remains explicit. The fixed-$r$ proof needs its own mathematical review; code tests and agreement between source accounts are not publication or priority certification. Hamiltonian locality, equilibration time and constants uniform in a growing number of batches remain separate research questions.
