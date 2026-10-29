# Reproduce hosted-rendering evidence

The optional read-only [verification workflow](../.github/workflows/verify.yml) runs the existing scientific and learning checks, then opens the actual public GitHub pages at the tested commit. It captures README, all science and learning pages, related work and the verification guide. It does not log in, change repository settings, modify a remote file, or use private credentials.

The artifacts contain the exact source Git bundle, dependency versions, command output, rendered page text/HTML, screenshots and an accessible-mathematics JSON capture. Artifacts expire after seven days; they are diagnostic outputs, not a permanent scientific archive or a substitute for a recorded review.

To run the browser capture locally in a checkout of the desired commit:

```bash
python -m pip install playwright==1.64.1
python -m playwright install --with-deps chromium
python verification/capture_hosted.py --revision "$(git rev-parse HEAD)" --output /tmp/thermometry-hosted
```

A successful capture means the script found rendered mathematics with accessible representations. It does **not** establish that every source expression was captured, that an inequality or operand survived, that the layout is readable, or that a proof is correct. Compare the capture with the pinned source inventory, inspect representative screenshots and every flagged expression, and repeat affected checks after a material source change.

A network failure, unavailable renderer or blocked Actions run must remain a failed or blocked check. It is not a passing presentation review. The browser dependency is separate from the scientific dependencies in [requirements.txt](requirements.txt).
