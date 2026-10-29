# Repository scientific integrity notes

Read [science/README.md](science/README.md) before changing any mathematical claim. Exact assumptions and quantifiers are in [science/model.md](science/model.md); sources and inherited results are in [references/RELATED_WORK.md](references/RELATED_WORK.md).

The central supported theorem is the sharp two-batch global minimax squared log-temperature risk of order N to the power minus three halves, under full Gibbs replacement and a pathwise total qubit budget. Its universal lower bound is [science/two_batch_converse.md](science/two_batch_converse.md); its matching constructive upper bound is [science/achievability.md](science/achievability.md). The root-mean-square error has exponent minus three quarters.

The fixed-r extension in [science/round_complexity.md](science/round_complexity.md) is converse-only for more than two batches. The necessary log-log batch count for quadratic risk is not a matching scheme.

Preserve the distinctions between global risk and local sensitivity, full Gibbs samples and dynamical bath access, sample count and elapsed time, arbitrary many-body Hamiltonians and local laboratory couplings. Finite numerical checks and assistant agreement are not independent proof certification.

Run `python verification/checks.py` for code checks. Keep the expected output, proof statements and reproduction documentation consistent. A source/test pass does not establish correct rendering in GitHub's hosted viewer; inspect representative equations and their visible contents separately.

The single selected educational anchor is De Pasquale and Stace, Quantum Thermometry, arXiv:1807.05762v1 (2018). [learning/ANCHOR.md](learning/ANCHOR.md) owns its source bridge, [learning/MILESTONES.md](learning/MILESTONES.md) the 12-background/18-narrative map M01–M30, and [learning/WORKED_EXAMPLES.md](learning/WORKED_EXAMPLES.md) the common examples. Preserve the settled selection unless a substantive scientific change makes it unsuitable or the author changes it. Primary research citations do not add educational prerequisites.

Keep personalized coaching, assessments, answers, progress and private editorial records outside this public scientific repository. Do not add publication-targeting process text to the reader-facing account. Preserve source provenance and load-bearing limitations during cleanup.
