"""Check the common learning map and local Markdown navigation."""
from __future__ import annotations
import json
import math
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    text = (ROOT / 'learning/MILESTONES.md').read_text(encoding='utf-8')
    sections = re.split(r'^### M(\d\d) — ', text, flags=re.MULTILINE)
    ids = [int(sections[i]) for i in range(1, len(sections), 2)]
    if ids != list(range(1, 31)):
        raise ValueError(f'Expected exactly ordered M01–M30; found {ids}')
    phase2 = text.index('## Phase II')
    if len(re.findall(r'^### M\d\d — ', text[:phase2], re.MULTILINE)) != 12:
        raise ValueError('The background phase must contain 12 milestones')
    for i in range(1, len(sections), 2):
        number, body = int(sections[i]), sections[i+1]
        for field in ['Question', 'Target', 'Dependencies/story', 'Connection', 'Sources']:
            if f'**{field}:**' not in body:
                raise ValueError(f'M{number:02d} lacks {field}')
        dependency = re.search(r'\*\*Dependencies/story:\*\*(.*)', body).group(1)
        refs = [int(x) for x in re.findall(r'M(\d\d)', dependency)]
        if any(x >= number or x < 1 for x in refs):
            raise ValueError(f'M{number:02d} has a forward/invalid dependency')
    pages = sorted(ROOT.rglob('*.md'))
    link_count = 0
    for path in pages:
        content = path.read_text(encoding='utf-8')
        for destination in re.findall(r'\]\(([^)]+)\)', content):
            parts = urlsplit(destination)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (path.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.is_file():
                raise ValueError(f'Broken local link: {path.relative_to(ROOT)} -> {destination}')
            link_count += 1
    for path in ['README.md', 'llms.txt', 'learning/README.md', 'learning/ANCHOR.md', 'AGENTS.md']:
        if '1807.05762v1' not in (ROOT / path).read_text(encoding='utf-8'):
            raise ValueError(f'Selected version not recorded in {path}')
    # Recompute the numerical example from the actual estimator formulas.
    L, M, T0 = math.log(511), 56, 1.5
    estimates = []
    for s in [0, 28, 56]:
        z = math.log((s+1)/(M-s+1))
        clipped = min(max(z, L*(1-T0)), L*(1-T0/2))
        estimates.append(T0/(1-clipped/L))
    if any(abs(x-y) > 1e-12 for x, y in zip(estimates, [1, 1.5, 2])):
        raise ValueError('Worked estimator endpoints disagree')
    if 512+M*9 != 1016 or not math.isclose(L*L/4, 9.72307641640438):
        raise ValueError('Worked resource/information values disagree')
    print(json.dumps({'status':'pass','milestones':30,'background':12,'narrative':18,
                      'markdown_pages':len(pages),'local_links':link_count,
                      'example_estimates':estimates}, indent=2))


if __name__ == '__main__':
    main()
