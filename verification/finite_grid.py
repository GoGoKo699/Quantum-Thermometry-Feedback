"""Finite exact-binomial validation of the two-round thermometer construction.

This grid test is not an asymptotic proof. Pilot terms below 1e-18 are omitted;
the missing contribution is explicitly bounded using the clipped risk range.
"""
import json
import numpy as np
from scipy.special import expit, logit
from scipy.stats import binom

lo = 0.0
hi = np.log(2.0)
pilot_gap = 1.5
rows = []
for total_qubits in [256, 512, 1024, 2048, 4096, 8192, 16384]:
    n1 = total_qubits // 2
    k = max(2, int(0.3 * np.sqrt(total_qubits)))
    blocks = (total_qubits - n1) // k
    log_deg = k * np.log(2.0) + np.log1p(-np.exp(-k * np.log(2.0)))
    pilot_counts = np.arange(n1 + 1)
    pilot_fraction = np.clip(
        pilot_counts / n1,
        expit(-pilot_gap * np.exp(-lo)),
        expit(-pilot_gap * np.exp(-hi)),
    )
    pilot_est = np.log(pilot_gap) - np.log(-logit(pilot_fraction))
    block_counts = np.arange(blocks + 1)
    z_hat = logit((block_counts + 1) / (blocks + 2))
    risks = []
    omitted_bounds = []
    for true_x in np.linspace(lo, hi, 9):
        pilot_p = expit(-pilot_gap * np.exp(-true_x))
        pilot_weights = binom.pmf(pilot_counts, n1, pilot_p)
        keep = pilot_weights > 1e-18
        centers = pilot_est[keep]
        weights = pilot_weights[keep]
        z = log_deg * (1 - np.exp(centers - true_x))
        block_p = expit(z)
        z_lo = log_deg * (1 - np.exp(centers - lo))
        z_hi = log_deg * (1 - np.exp(centers - hi))
        z_clip = np.maximum(z_lo[:, None], np.minimum(z_hi[:, None], z_hat[None, :]))
        estimates = centers[:, None] - np.log1p(-z_clip / log_deg)
        conditional_weights = binom.pmf(block_counts[None, :], blocks, block_p[:, None])
        risks.append(float(np.sum(weights[:, None] * conditional_weights * (estimates - true_x) ** 2)))
        omitted_bounds.append(float(np.sum(pilot_weights[~keep]) * (hi - lo) ** 2))
    row = {
        "total_qubits_budget": total_qubits,
        "used_qubits": n1 + blocks * k,
        "pilot_qubits": n1,
        "block_size": k,
        "block_count": blocks,
        "max_tested_risk": max(risks),
        "max_tested_risk_times_N_3_2": max(risks) * total_qubits ** 1.5,
        "max_omitted_risk_bound": max(omitted_bounds),
        "log_temperature_grid": np.linspace(lo, hi, 9).tolist(),
        "risk_on_grid": risks,
    }
    rows.append(row)
print(json.dumps({"numpy": np.__version__, "temperature_interval": [1, 2], "rows": rows}, indent=2))
