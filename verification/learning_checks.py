"""Check shared learning structure and the tutorial's finite example.

This is not a hosted-rendering check or a proof of an asymptotic claim.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_map() -> None:
    text = (ROOT / "learning/MILESTONES.md").read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^### (M\d{2}) — ", text)
    ids = blocks[1::2]
    require(ids == [f"M{i:02d}" for i in range(1, 31)], "Expected M01 through M30 exactly once")
    fields = ["Phase", "Central question", "Understanding target", "Dependencies", "Conceptual connection and story role", "Source pointers"]
    for i, body in enumerate(blocks[2::2], 1):
        for field in fields:
            require(f"**{field}:**" in body, f"M{i:02d} missing {field}")
        dependencies = body.split("**Dependencies:**", 1)[1].split("\n", 1)[0]
        require(all(int(x) < i for x in re.findall(r"M(\d{2})", dependencies)), "Dependency must precede target")
        phase = "Background/preliminaries" if i <= 14 else "Narrative/innovation"
        require(f"**Phase:** {phase}." in body, f"Wrong phase at M{i:02d}")
    anchor = (ROOT / "learning/ANCHOR.md").read_text(encoding="utf-8")
    require("1807.05762v1" in anchor and "De Pasquale" in anchor and "Stace" in anchor, "Selected anchor missing")
    print("PASS 30 complete milestones; backward dependencies; 14/16 phases; selected anchor")


def check_example() -> None:
    pilot_n, pilot_s, gap, k, blocks = 128, 34, 1.5, 4, 32
    t0 = gap / math.log((pilot_n - pilot_s) / pilot_s)
    L = math.log(2**k - 1)
    energy = L * t0
    p = 1 / (1 + math.exp(-(L - energy / 1.5)))
    require(pilot_n + k * blocks == 256, "Uncharged qubits")
    require(abs(t0 - 1.47502) < 5e-6, "Pilot rounding")
    require(abs(energy - 3.99443) < 5e-6, "Gap rounding")
    require(abs(p - 0.51127) < 5e-6, "Probability rounding")
    estimates = []
    for s in [0, 16, 32]:
        z = math.log((s + 1) / (blocks - s + 1))
        z = min(max(z, L * (1 - t0)), L * (1 - t0 / 2))
        estimates.append(t0 / (1 - z / L))
    require(all(abs(a - b) < 1e-12 for a, b in zip(estimates, [1., t0, 2.])), "Clipped estimator")
    print(f"PASS tutorial N=256 example: T0={t0:.8f}, E={energy:.8f}, p={p:.8f}; endpoint counts retained")


if __name__ == "__main__":
    check_map()
    check_example()
