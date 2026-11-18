# Reproduce hosted mathematics

The read-only [verification workflow](../.github/workflows/verify.yml) checks the exact public pull-request revision. It runs a representative model-page probe, the scientific and learning checks, then captures every tracked Markdown page at widths 1440 and 760. Same-repository pull requests run with `contents: read`, without retained credentials or secret inputs.

The [collector](hosted_math/capture_hosted_math.cjs) inventories source expressions and compiles expected MathML with MathJax. It then compares those symbols and structures with the actual GitHub-rendered MathML, including scripts, fractions, labels, host counts and display geometry. The [checker](hosted_math/check_rendered_math.py) and [probe](hosted_math/probe_hosted_math.cjs) use the same source-bound contract. These are generic verification helpers; they do not establish mathematical correctness.

The artifact contains the source commit/tree, runtime versions, command outputs, page text/HTML, screenshots, individual page receipts and `hosted-report.json`. Artifacts expire after14days. A passing report still requires actual visual inspection of the principal claims, proof and learning route at both widths; it is not by itself a scientific or visual certificate.

For a local checkout of the exact public commit, install `playwright@1.56.1` and `mathjax-full@3.2.1` in a temporary directory outside the source, and install Chromium with the Playwright CLI. Then set `NODE_PATH` to that temporary `node_modules` directory and run:

```bash
node verification/hosted_math/probe_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Quantum-Thermometry-Feedback \
  --revision "$(git rev-parse HEAD)" --page science/model.md \
  --output /tmp/thermometry-probe
node verification/hosted_math/capture_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Quantum-Thermometry-Feedback \
  --revision "$(git rev-parse HEAD)" --output /tmp/thermometry-hosted
```

Use new empty output directories and retain failed attempts. A technical network failure, unavailable dependency or access denial remains a failed or blocked check. The older `capture_hosted.py` is a narrower legacy capture utility; its output does not replace the full structural report above.
