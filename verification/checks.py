"""Run exact finite-grid and selected foundational checks.

These checks validate code and finite consequences, not universal theorems.
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.special import expit, logsumexp
from scipy.stats import binom

BASE = Path(__file__).resolve().parent


def test_gibbs_entropy_area() -> None:
    # Integrate the exact classical Gibbs Fisher information in x = log T
    # against the entropy change. Numeric integration only.
    levels_list = [[0., 1.], [0., 0., 2., 2.], [0., .4, 1.5, 3.]]
    xs = np.linspace(-8., 8., 40001)
    for energies in levels_list:
        energies = np.asarray(energies, dtype=float)
        beta = np.exp(-xs)
        logw = -beta[:, None] * energies[None, :]
        probs = np.exp(logw - logsumexp(logw, axis=1, keepdims=True))
        mean = np.sum(probs * energies[None, :], axis=1)
        second = np.sum(probs * (energies[None, :] ** 2), axis=1)
        heat = beta ** 2 * (second - mean ** 2)
        heat = np.maximum(0., heat)  # floating-point variance roundoff
        entropy = -np.sum(np.where(probs > 0, probs * np.log(np.maximum(probs, 1e-300)), 0.), axis=1)
        area = float(simpson(heat, x=xs))
        entropy_change = float(entropy[-1] - entropy[0])
        assert abs(area - entropy_change) < 1e-5, (area, entropy_change)
        assert area <= math.log(len(energies)) + 1e-6
        n = math.ceil(math.log2(len(energies)))
        B = math.log(2) ** 2 + 2 * math.log(2) + 2
        assert np.max(heat) <= B * n ** 2 + 1e-6
    print("PASS Gibbs FI/entropy-area identities for 3 finite spectra")


def test_prior_geometry() -> None:
    a, b = 0., math.log(2.)
    xs = np.linspace(a, b, 25001)
    w = b - a
    u = math.pi * (xs - a) / w
    q = 2. / w * np.sin(u) ** 2
    qp = 4. * math.pi / w ** 2 * np.sin(u) * np.cos(u)
    # Analytic endpoint limits of q'^2/q, avoiding 0/0 at endpoints
    integrand = 8. * math.pi ** 2 / w ** 3 * np.cos(u) ** 2
    area = float(simpson(q, x=xs))
    I = float(simpson(integrand, x=xs))
    assert abs(area - 1.) < 1e-9
    assert abs(I - 4. * math.pi ** 2 / w ** 2) < 1e-8
    assert 2. * np.max(q) <= math.sqrt(I) + 1e-9
    print("PASS smooth prior normalization and peak/Fisher inequality")


def test_binomial_logit_bound() -> None:
    for M in [1, 2, 3, 10, 100, 200]:
        s = np.arange(M + 1, dtype=float)
        estimated = np.log((s + 1.) / (M - s + 1.))
        for p in [1e-4, .003, .025, .3, .5, .7, .975, .997, 1 - 1e-4]:
            probs = binom.pmf(s, M, p)
            target = math.log(p / (1. - p))
            squared = float(np.dot(probs, (estimated - target) ** 2))
            bound = 200. / (M * p * (1. - p))
            assert squared <= bound + 1e-9, (M, p, squared, bound)
    print("PASS uniform smoothed-logit inequality on 54 finite cases")


def test_exact_binomial_risk_grid() -> None:
    observed = json.loads(subprocess.check_output([sys.executable, str(BASE / "finite_grid.py")], text=True))
    expected = json.loads((BASE / "expected.json").read_text(encoding="utf-8"))
    assert len(observed["rows"]) == len(expected["rows"]) == 7
    for row, ref in zip(observed["rows"], expected["rows"]):
        assert row["total_qubits_budget"] == ref["total_qubits_budget"]
        assert row["used_qubits"] == ref["used_qubits"]
        assert row["used_qubits"] <= row["total_qubits_budget"]
        assert row["pilot_qubits"] == ref["pilot_qubits"]
        assert row["block_size"] == ref["block_size"]
        assert row["block_count"] == ref["block_count"]
        assert np.allclose(row["risk_on_grid"], ref["risk_on_grid"], rtol=2e-9, atol=1e-12)
        assert np.isclose(row["max_tested_risk_times_N_3_2"], ref["max_tested_risk_times_N_3_2"], rtol=2e-9, atol=1e-8)
        assert row["max_omitted_risk_bound"] < 1e-12
        assert row["max_tested_risk_times_N_3_2"] < 100.0
    print("PASS finite-grid exact-binomial risk at 7 budgets and 9 temperatures")
    for row in observed["rows"]:
        print(f"  N={row['total_qubits_budget']:5d}  k={row['block_size']:2d}  M={row['block_count']:3d}  "
              f"max(N^1.5 risk)={row['max_tested_risk_times_N_3_2']:.6f}  "
              f"omitted_bound={row['max_omitted_risk_bound']:.2e}")


if __name__ == "__main__":
    test_gibbs_entropy_area()
    test_prior_geometry()
    test_binomial_logit_bound()
    test_exact_binomial_risk_grid()
    print("All finite checks passed. These are not asymptotic proofs.")
