"""Deterministic finite checks of the hedged Gibbs-array estimator.

The implemented observations use the finite grouped Poisson-binomial law,
evaluated in floating point. There is no Monte Carlo, asymptotic fit, or
deliberate probability-mass pruning. These
checks validate finite implementations and proof ingredients, not the universal
moment-propagation theorem or a growing-round conclusion.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
import math
from itertools import product

import numpy as np
from scipy.optimize import brentq
from scipy.special import expit
from scipy.stats import binom

MIN_REFINEMENT_BLOCK_ALLOWANCE = 2 ** 16


def log_degeneracy(k: int) -> float:
    """Evaluate log(2**k-1) without constructing an exponential-size spectrum."""
    if k < 2:
        raise ValueError("The finite checks use the asymptotic construction at k>=2")
    z = k * math.log(2.0)
    return z + math.log1p(-math.exp(-z))


def excitation_probabilities(L: float, centers: np.ndarray, x: float) -> np.ndarray:
    # The meaningful variable is the logit, not exp(E/T) or the degeneracy.
    delta = centers - x
    with np.errstate(over="ignore"):
        logits = -L * np.expm1(delta)
    return expit(logits)


@dataclass(frozen=True)
class HedgedArray:
    width: float
    budget: int
    center: float
    a: float
    b: float
    k: int
    L: float
    M: int
    J: int
    offsets: np.ndarray
    multiplicities: np.ndarray
    centers: np.ndarray
    left: float
    right: float

    @property
    def count(self) -> int:
        return int(self.multiplicities.sum())

    @property
    def used_qubits(self) -> int:
        return self.k * self.count

    def probabilities(self, x: float) -> np.ndarray:
        return excitation_probabilities(self.L, self.centers, x)

    def mean(self, x: float) -> float:
        return float(np.dot(self.multiplicities, self.probabilities(x)))

    def derivative(self, x: float) -> float:
        d = self.centers - x
        z = -self.L * np.expm1(d)
        # expit(z)*expit(-z), rather than p*(1-p), keeps rare tails stable.
        derivatives = self.L * np.exp(d) * expit(z) * expit(-z)
        return float(np.dot(self.multiplicities, derivatives))

    def estimate(self, count: float) -> float:
        """Clip to the attainable mean interval, then invert its monotone mean."""
        low_mean, high_mean = self.mean(self.left), self.mean(self.right)
        if count <= low_mean:
            return self.left
        if count >= high_mean:
            return self.right
        return float(brentq(lambda t: self.mean(t) - count,
                            self.left, self.right, xtol=1e-14, rtol=1e-14))

    def exact_count_law(self, x: float) -> np.ndarray:
        """Convolve the actual independent binomial groups; retain all counts."""
        law = np.array([1.0])
        for m, p in zip(self.multiplicities, self.probabilities(x)):
            if m:
                local = binom.pmf(np.arange(int(m) + 1), int(m), float(p))
                law = np.convolve(law, local)
        assert len(law) == self.count + 1
        return law


def make_array(width: float, budget: int, center: float,
               a: float = 0.0, b: float = math.log(2.0)) -> HedgedArray:
    if not (0.0 < width <= 0.5 and a <= center <= b):
        raise ValueError("Require 0<width<=0.5 and a range-valued preceding estimate")
    k = math.ceil(1.0 / width)
    M = budget // k
    if M < 4:
        raise ValueError("The asymptotic array requires a nonempty central group")
    # This integer correction avoids accepting a floating root on the wrong side.
    J = int(M ** (1.0 / 8.0))
    while (J + 1) ** 8 <= M:
        J += 1
    while J ** 8 > M:
        J -= 1
    offsets = np.arange(-J, J + 1, dtype=int)
    multiplicities = np.array([M // (4 * (1 + abs(int(j))) ** 2)
                               for j in offsets], dtype=np.int64)
    centers = center + offsets * width
    return HedgedArray(width, budget, center, a, b, k, log_degeneracy(k),
                       M, J, offsets, multiplicities, centers,
                       max(a, center - J * width), min(b, center + J * width))


def plan_refinement(width: float, budget: int, center: float) -> HedgedArray | None:
    """Return None for the proof's paid fixed-gap/unchanged-estimate fallback."""
    if width > 0.5 or budget // math.ceil(1.0 / width) < MIN_REFINEMENT_BLOCK_ALLOWANCE:
        return None
    return make_array(width, budget, center)


def check_finite_budget_fallback() -> int:
    cases = 0
    for width in [0.02, 0.1, 0.5]:
        k = math.ceil(1. / width)
        assert plan_refinement(width, k * MIN_REFINEMENT_BLOCK_ALLOWANCE - 1, 0.31) is None
        accepted = plan_refinement(width, k * MIN_REFINEMENT_BLOCK_ALLOWANCE, 0.31)
        assert accepted is not None and accepted.M == MIN_REFINEMENT_BLOCK_ALLOWANCE
        assert accepted.used_qubits <= accepted.budget
        cases += 2
    assert plan_refinement(1.0, 10_000_000, 0.31) is None
    return cases + 1


def check_gibbs_law_and_stability() -> int:
    cases = 0
    for k in [2, 3, 5, 8]:
        L = log_degeneracy(k)
        for c in [-0.1, 0.2, 0.8]:
            energies = np.r_[0.0, np.full(2 ** k - 1, L * math.exp(c))]
            for x in [0.0, 0.3, math.log(2.0)]:
                weights = np.exp(-math.exp(-x) * energies)
                direct = float(weights[1:].sum() / weights.sum())
                reduced = float(excitation_probabilities(L, np.array([c]), x)[0])
                assert abs(direct - reduced) < 3e-15
                cases += 1
    # No 2**k is formed for this check. Under/overflow limits are valid outcomes.
    L = log_degeneracy(100_000)
    p = excitation_probabilities(L, np.array([-1000., 0., 1000.]), 0.)
    assert np.array_equal(p, np.array([1., 0.5, 0.])) and np.isfinite(p).all()
    return cases + 1


def check_budget_floors_and_local_derivatives() -> tuple[int, float]:
    cases, smallest_scaled_derivative = 0, math.inf
    for width in [0.01, 0.02, 0.05, 0.1]:
        k = math.ceil(1.0 / width)
        for M in [16, 31, 64, 255, 256, 1024, 4096, 65_536]:
            for center in [0.0, 0.21, math.log(2.0)]:
                array = make_array(width, M * k + k - 1, center)
                assert array.M == M
                assert array.count <= M and array.used_qubits <= array.budget
                assert array.left <= center <= array.right
                assert array.multiplicities[array.J] == M // 4
                assert array.estimate(0.) == array.left
                assert array.estimate(float(array.count)) == array.right
                if M >= 256:
                    # Reconstruct the actual nearest-center step on the good set.
                    cap = min(M ** (1.0 / 16.0), 0.69 / width)
                    for D in np.linspace(-cap, cap, 17):
                        x = center + float(D) * width
                        if not (array.a <= x <= array.b):
                            continue
                        j = int(np.argmin(np.abs(array.centers - x)))
                        assert abs(array.centers[j] - x) <= width * (0.5 + 1e-12)
                        assert array.multiplicities[j] >= M / (32. * (1. + abs(D)) ** 2)
                        for t in np.linspace(max(array.left, x - width),
                                             min(array.right, x + width), 9):
                            d = float(array.centers[j] - t)
                            z = -array.L * math.expm1(d)
                            scaled = width * array.L * math.exp(d) * expit(z) * expit(-z)
                            smallest_scaled_derivative = min(smallest_scaled_derivative, scaled)
                            assert scaled >= 0.01
                            assert array.derivative(float(t)) >= (
                                0.01 * M / (32. * width * (1. + abs(D)) ** 2))
                cases += 1
    return cases, smallest_scaled_derivative


def conditional_risks(array: HedgedArray, x: float) -> tuple[np.ndarray, np.ndarray, dict]:
    law = array.exact_count_law(x)
    estimates = np.array([array.estimate(float(z)) for z in range(array.count + 1)])
    assert abs(float(law.sum()) - 1.) < 2e-12
    assert np.all(law >= 0.) and np.isfinite(law).all()
    assert abs(float(np.dot(np.arange(array.count + 1), law)) - array.mean(x)) < 2e-10
    assert np.all(np.diff(estimates) >= -2e-13)
    assert np.all(estimates >= array.left - 2e-13)
    assert np.all(estimates <= array.right + 2e-13)
    # Inversion of the mean itself must recover every feasible interior x.
    if array.left <= x <= array.right:
        assert abs(array.estimate(array.mean(x)) - x) < 2e-12
    errors = estimates - x
    v = array.width / math.sqrt(array.M)
    moments = {str(q): float(np.dot(law, (np.abs(errors) / v) ** q)) for q in [2, 4]}
    return law, estimates, moments


def check_exact_distributions_and_tail_events() -> dict:
    cases, checked_tail_events = 0, 0
    largest_normalized_second = 0.0
    example_rows = []
    for width in [0.02, 0.05]:
        for M in [64, 128, 256]:
            k = math.ceil(1.0 / width)
            for x in [0.0, 0.31, math.log(2.0)]:
                for nominal_D in [-6., -2.5, -1., -0.5, 0., 0.5, 1., 2.5, 6.]:
                    center = min(math.log(2.), max(0., x - nominal_D * width))
                    array = make_array(width, M * k, center)
                    D = (x - center) / width
                    law, estimates, moments = conditional_risks(array, x)
                    largest_normalized_second = max(largest_normalized_second, moments["2"])
                    assert np.all(np.abs(estimates - x) <= width * (array.J + abs(D)) + 2e-13)
                    if abs(D) <= M ** (1.0 / 16.0):
                        for u in [0.1 * width, 0.5 * width, width]:
                            for sign in [-1., 1.]:
                                target = x + sign * u
                                actual = float(law[sign * (estimates - x) > u + 2e-13].sum())
                                if not (array.left <= target <= array.right):
                                    assert actual < 2e-12
                                    continue
                                shift = abs(array.mean(target) - array.mean(x))
                                bound = math.exp(-2. * shift * shift / array.count)
                                assert actual <= bound + 2e-12, (M, width, D, x, u, actual, bound)
                                checked_tail_events += 1
                    if width == 0.02 and M == 256 and x == 0.31 and nominal_D in [0., 2.5, 6.]:
                        example_rows.append({"M": M, "width": width, "D": D,
                                             "blocks": array.count,
                                             "normalized_moments": moments})
                    cases += 1
    # Also integrate one whole array in the actual lemma regime. The smaller
    # grids above test the same finite component below the theorem's conservative
    # threshold, where the complete stated protocol would select its fallback.
    accepted = plan_refinement(0.02, 50 * MIN_REFINEMENT_BLOCK_ALLOWANCE, 0.31)
    assert accepted is not None
    _, _, large_moments = conditional_risks(accepted, 0.31)
    example_rows.append({"M": accepted.M, "width": accepted.width, "D": 0.0,
                         "blocks": accepted.count, "normalized_moments": large_moments})
    cases += 1
    return {"conditional_cases": cases, "one_sided_tail_events": checked_tail_events,
            "largest_normalized_second_moment_including_outliers": largest_normalized_second,
            "examples": example_rows}


def check_grouped_law_against_outcome_enumeration() -> int:
    cases = 0
    for M in [16, 31]:
        array = make_array(0.1, 10 * M, 0.21)
        for x in [0.0, 0.31, math.log(2.0)]:
            probabilities = np.repeat(array.probabilities(x), array.multiplicities)
            direct = np.zeros(array.count + 1)
            for bits in product([0, 1], repeat=array.count):
                weight = math.prod(p if bit else 1. - p
                                   for bit, p in zip(bits, probabilities))
                direct[sum(bits)] += weight
            assert np.allclose(direct, array.exact_count_law(x), rtol=3e-13, atol=3e-15)
            cases += 1
    return cases


def check_rare_center_histories() -> dict:
    # This is a completely enumerated preceding-center distribution, deliberately
    # including centers outside the hedge radius. It is a finite diagnostic, not
    # a replacement for the all-moments induction in the proof.
    width, M, x = 0.02, 256, 0.31
    Ds = np.array([-8., -3., -1., -0.5, 0., 0.5, 1., 3., 8.])
    prior = (1. + np.abs(Ds)) ** -26
    prior /= prior.sum()
    arrays = [make_array(width, M * math.ceil(1. / width), x - D * width) for D in Ds]
    conditional = [conditional_risks(array, x)[2] for array in arrays]
    bad = np.abs(Ds) > M ** (1. / 16.)
    result = {"center_histories": len(Ds), "bad_history_probability": float(prior[bad].sum())}
    for q in [2, 4]:
        K = 12 * q
        actual_bad = sum(float(weight) * row[str(q)] for weight, row, is_bad
                         in zip(prior, conditional, bad) if is_bad)
        cap_bad = float(np.dot(prior[bad],
                              (math.sqrt(M) * (arrays[0].J + np.abs(Ds[bad]))) ** q))
        assert actual_bad <= cap_bad * (1. + 1e-12) + 1e-15
        C_K = float(np.dot(prior, np.abs(Ds) ** K))
        markov_bound = 2. ** max(q - 1, 0) * C_K * (
            M ** ((9. * q - K) / 16.) + M ** ((10. * q - K) / 16.))
        assert cap_bad <= markov_bound * (1. + 1e-12) + 1e-15
        result[f"normalized_moment_{q}"] = sum(float(w) * row[str(q)]
                                               for w, row in zip(prior, conditional))
        result[f"bad_normalized_moment_{q}"] = actual_bad
        result[f"bad_deterministic_bound_{q}"] = cap_bad
    return result


def check_fixed_round_recurrence() -> int:
    alpha = Fraction(1, 2)
    for r in range(1, 13):
        assert alpha == 1 - Fraction(1, 2 ** r)
        assert 2 * alpha == 2 - Fraction(1, 2 ** (r - 1))
        if r > 1:
            # The allocation is deterministic, including the unused remainder.
            N = 100_003
            B = N // r
            assert r * B <= N and 0 <= N - r * B < r
        alpha = (1 + alpha) / 2
    return 12


def run_checks() -> dict:
    small_spectra = check_gibbs_law_and_stability()
    floor_cases, min_slope = check_budget_floors_and_local_derivatives()
    distributions = check_exact_distributions_and_tail_events()
    enumerated = check_grouped_law_against_outcome_enumeration()
    rare = check_rare_center_histories()
    fallback = check_finite_budget_fallback()
    recurrence = check_fixed_round_recurrence()
    report = {
        "gibbs_probability_checks": small_spectra,
        "pathwise_floor_layouts": floor_cases,
        "minimum_tested_width_scaled_nearest_group_derivative": float(min_slope),
        "exact_hedged_array": distributions,
        "full_binary_record_enumerations": enumerated,
        "rare_center_history_diagnostic": rare,
        "finite_budget_fallback_cases": fallback,
        "exact_rational_recurrence_checks": recurrence,
        "scope": "Finite implementation and inequalities only; no asymptotic, growing-round, thermalization-time, continuum-supremum or priority certification.",
    }
    print("PASS hedged-array Gibbs law, budgets, clipping, exact count laws, tails and rare histories")
    print(json.dumps(report, indent=2, allow_nan=False))
    return report


if __name__ == "__main__":
    run_checks()
