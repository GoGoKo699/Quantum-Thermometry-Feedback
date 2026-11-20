"""Finite checks for the nested Gibbs-batch schedule and two-body star readout."""
from __future__ import annotations

import itertools
import json
import math
from collections.abc import Callable

from scipy.optimize import brentq
from scipy.special import expit

from fixed_round_checks import log_degeneracy


LOG_2 = math.log(2.0)
LOG_4 = 2 * LOG_2
SCHEDULE_SUM = 2 + (20 / 9) * LOG_2 + (LOG_2 - 2) / 3


def star_contrast(gap: float) -> float:
    return LOG_2 - math.log1p(math.exp(-gap))


def response(block_size: int, offset: float, star_gap: float | None) -> tuple[float, float]:
    """Return the binary outcome probability and its temperature derivative."""
    inverse_scale = math.exp(-offset)
    if star_gap is None:
        log_dimension = log_degeneracy(block_size)
        logit = -log_dimension * math.expm1(-offset)
        logit_derivative = log_dimension * inverse_scale
    else:
        hub_gap = star_contrast(star_gap)
        scaled_gap = star_gap * inverse_scale
        logit = (block_size - 1) * (star_contrast(scaled_gap) - inverse_scale * hub_gap)
        logit_derivative = (block_size - 1) * inverse_scale * (
            hub_gap - star_gap * float(expit(-scaled_gap))
        )
    probability = float(expit(logit))
    return probability, logit_derivative * probability * float(expit(-logit))


def slope_bound(radius: float, star_gap: float | None) -> float:
    size_bound = max(2 * radius, 1 + radius)
    if star_gap is None:
        logit_bound = size_bound * math.exp(radius) * LOG_2
        logit_slope = LOG_2 * math.exp(-radius) / 2
    else:
        hub_gap = star_contrast(star_gap)
        logit_bound = size_bound * math.exp(radius) * hub_gap
        logit_slope = hub_gap * math.exp(-radius) / 4
    return logit_slope * float(expit(logit_bound)) * float(expit(-logit_bound))


def check_star_gibbs_marginal() -> int:
    cases = 0
    for radius in (0.1, 0.5, math.log(10) / 2):
        star_gap = math.exp(radius) * (2 * radius + 10)
        hub_gap = star_contrast(star_gap)
        assert star_gap * math.exp(-star_gap * math.exp(-radius)) <= hub_gap / 2
        for block_size in (2, 3, 5, 8):
            for offset in (-radius, -radius / 5, 0.0, radius / 3, radius):
                partition = [0.0, 0.0]
                weighted_energy = [0.0, 0.0]
                for hub, *leaves in itertools.product((0, 1), repeat=block_size):
                    energy = (block_size - 1) * hub_gap if hub else star_gap * sum(leaves)
                    scaled_energy = math.exp(-offset) * energy
                    weight = math.exp(-scaled_energy)
                    partition[hub] += weight
                    weighted_energy[hub] += scaled_energy * weight
                normalizer = sum(partition)
                probability = partition[1] / normalizer
                derivative = (weighted_energy[1] - probability * sum(weighted_energy)) / normalizer
                observed_p, observed_derivative = response(block_size, offset, star_gap)
                assert math.isclose(observed_p, probability, rel_tol=5e-14, abs_tol=1e-14)
                assert math.isclose(observed_derivative, derivative, rel_tol=5e-14, abs_tol=1e-14)
                cases += 1
    return cases


def check_uniform_interval_slopes() -> int:
    cases = 0
    for radius in (0.05, 0.2, 0.5, math.log(10) / 2):
        for star_gap in (None, math.exp(radius) * (2 * radius + 10)):
            slope = slope_bound(radius, star_gap)
            for width in (radius, radius / 2, radius / 15, radius / 200):
                block_size = max(2, math.ceil(1 / width))
                for index in range(-10, 11):
                    offset = (index / 10) * width
                    probability, derivative = response(block_size, offset, star_gap)
                    assert 0.0 < probability < 1.0
                    assert derivative * width >= slope
                    cases += 1
    return cases


def check_rounded_budgets() -> tuple[int, int]:
    cases, largest_depth = 0, 0
    for radius in (0.05, 0.2, 0.5, math.log(10) / 2):
        for star_gap in (None, math.exp(radius) * (2 * radius + 10)):
            slope = slope_bound(radius, star_gap)
            size_bound = max(2 * radius, 1 + radius)
            cost_bound = size_bound * (1 / LOG_2 + 1 / (2 * slope**2))
            scale = max(1.0, 16 * cost_bound * SCHEDULE_SUM)

            def log_width_at(stage: int) -> float:
                return math.log(scale) + 2**stage + LOG_4 * stage

            for budget in (1, 100, 10**8, 10**16, 10**32, 10**64, 10**100):
                depth = 0
                log_budget = math.log(budget)
                while log_width_at(depth) < log_budget + math.log(radius):
                    depth += 1
                largest_depth = max(largest_depth, depth)
                used_qubits = 0
                for stage in range(depth, 0, -1):
                    log_width = min(math.log(radius), log_width_at(stage) - log_budget)
                    width = math.exp(log_width)
                    next_width = math.exp(log_width_at(stage - 1) - log_budget)
                    assert 0 < next_width <= width <= radius + 2e-16
                    block_size = max(2, math.ceil(1 / width))
                    log_two_over_miss = 2 * (2**stage - 1) + (5 * stage + 1) * LOG_2
                    block_count = math.ceil(
                        (width / next_width)**2 * log_two_over_miss / (2 * slope**2)
                    )
                    used_qubits += block_size * block_count
                assert used_qubits <= budget
                cases += 1
    return cases, largest_depth


def invert_count(
    law: Callable[[float], float], left: float, right: float, fraction: float
) -> float:
    if fraction <= law(left):
        return left
    if fraction >= law(right):
        return right
    return float(brentq(lambda x: law(x) - fraction, left, right))


def check_entire_toy_count_trees() -> tuple[int, int]:
    # Small, independently sized batches make exhaustive binomial sums possible.
    # These demonstrate the interval update and first-exit accounting, rather
    # than approximate the deliberately conservative asymptotic schedule.
    initial_radius = 0.35
    stages = ((0.14, 8), (0.065, 6), (0.03, 4))
    cases, total_leaves = 0, 0
    for star_gap in (None, math.exp(initial_radius) * (2 * initial_radius + 10)):
        for x in (-0.35, -0.23, -0.07, 0.0, 0.12, 0.25, 0.35):
            exits = [0.0] * len(stages)
            branches = [(-initial_radius, initial_radius, 1.0, None)]
            width = initial_radius
            for stage, (next_width, count) in enumerate(stages):
                block_size = max(2, math.ceil(1 / width))
                children = []
                for left, right, weight, first_exit in branches:
                    center = (left + right) / 2

                    def law(t: float) -> float:
                        return response(block_size, t - center, star_gap)[0]

                    probability = law(x)
                    for positive in range(count + 1):
                        estimate = invert_count(law, left, right, positive / count)
                        narrowed_left = max(left, estimate - next_width)
                        narrowed_right = min(right, estimate + next_width)
                        assert narrowed_left <= estimate <= narrowed_right
                        assert narrowed_right - narrowed_left <= 2 * next_width + 2e-16
                        branch_weight = weight * math.comb(count, positive) * (
                            probability**positive * (1 - probability)**(count - positive)
                        )
                        exit_stage = first_exit
                        if first_exit is None and not (narrowed_left <= x <= narrowed_right):
                            assert left <= x <= right
                            exits[stage] += branch_weight
                            exit_stage = stage
                        children.append((narrowed_left, narrowed_right, branch_weight, exit_stage))
                branches = children
                width = next_width
            assert math.isclose(sum(weight for _, _, weight, _ in branches), 1.0, abs_tol=1e-13)
            ancestor_radii = (initial_radius, *(value for value, _ in stages[:-1]))
            risk = 0.0
            for left, right, weight, first_exit in branches:
                error = abs((left + right) / 2 - x)
                cap = width if first_exit is None else 2 * ancestor_radii[first_exit]
                assert error <= cap + 2e-16
                risk += weight * error**2
            assert all(mass > 0 for mass in exits)
            assert risk <= width**2 + sum(
                mass * (2 * ancestor_radius)**2
                for mass, ancestor_radius in zip(exits, ancestor_radii)
            ) + 2e-15
            cases += 1
            total_leaves += len(branches)
    return cases, total_leaves


def run_checks() -> dict:
    budget_cases, deepest = check_rounded_budgets()
    tree_cases, tree_leaves = check_entire_toy_count_trees()
    report = {
        "direct_star_gibbs_spectra": check_star_gibbs_marginal(),
        "interval_slope_points": check_uniform_interval_slopes(),
        "rounded_budget_schedules": budget_cases,
        "maximum_schedule_depth_tested": deepest,
        "exhaustive_toy_count_trees": tree_cases,
        "exhaustive_toy_count_leaves": tree_leaves,
    }
    print("PASS nested interval updates, first exits, rounded budgets and star Gibbs readout")
    print(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    run_checks()
