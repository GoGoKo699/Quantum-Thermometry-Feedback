# Repository scientific integrity notes

Read [science/README.md](science/README.md) before changing any mathematical claim. Exact assumptions and quantifiers are in [science/model.md](science/model.md); sources and inherited results are in [references/RELATED_WORK.md](references/RELATED_WORK.md).

The central supported theorem is the sharp two-batch global minimax squared log-temperature risk $\Theta(N^{-3/2})$ under full Gibbs replacement and a pathwise total qubit budget. Its universal lower bound is [science/two_batch_converse.md](science/two_batch_converse.md); its matching constructive upper bound is [science/achievability.md](science/achievability.md).

The fixed-$r$ extension in [science/round_complexity.md](science/round_complexity.md) is **converse-only** for $r>2$. A necessary $\Omega(\log\log N)$ round count for quadratic risk is not a matching scheme.

Preserve the distinction between globally unknown temperature and a locally tuned probe, static full Gibbs samples and dynamical bath access, sample count and wall-clock/thermalization cost, and arbitrary many-body access and hardware-local couplings. Do not treat finite numerical checks or assistant agreement as independent proof certification.

For code, first run [verification/checks.py](verification/checks.py); keep the pinned expected output, relevant proof statements, and documentation consistent. When a mathematical result changes, update affected routes and literature comparisons together.

General learning materials may later be attached under learning/, once the author chooses one educational anchor. Keep personalized coaching instructions, assessments, answers and user progress **outside this public research repository**. Do not add manuscript-targeting or private venue judgments to the reader-facing account.