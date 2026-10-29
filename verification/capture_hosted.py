"""Capture actual GitHub-rendered mathematics at an exact source revision.

The output is evidence for source comparison and visual review, not an
automatic scientific or presentation-readiness certificate. No login is used.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from playwright.sync_api import sync_playwright

EXTRACT = r'''() => {
  const article = document.querySelector('article.markdown-body') || document.querySelector('.markdown-body');
  if (!article) throw new Error('No rendered Markdown article');
  let hosts = [...article.querySelectorAll('math-renderer')];
  if (!hosts.length) hosts = [...article.querySelectorAll('mjx-container')];
  if (!hosts.length) hosts = [...article.querySelectorAll('.katex')];
  if (!hosts.length) hosts = [...article.querySelectorAll('math')];
  const roots = node => {
    const result = [node];
    for (const element of node.querySelectorAll('*')) {
      if (element.shadowRoot) result.push(...roots(element.shadowRoot));
    }
    if (node.shadowRoot) result.push(...roots(node.shadowRoot));
    return result;
  };
  const math = hosts.map(host => {
    const rr = roots(host);
    const find = selector => rr.flatMap(root => [...root.querySelectorAll(selector)]);
    const errors = find('[data-mjx-error],mjx-merror,.katex-error').map(e => e.textContent || e.getAttribute('data-mjx-error'));
    let mm = host.tagName.toLowerCase() === 'math' ? host : find('math')[0];
    let text = '', text_source = 'mathml';
    if (mm) {
      mm = mm.cloneNode(true);
      mm.querySelectorAll('annotation,annotation-xml').forEach(e => e.remove());
      text = mm.textContent;
    } else {
      const labeled = find('svg[aria-label],[role="img"][aria-label]')[0];
      if (labeled) {text = labeled.getAttribute('aria-label'); text_source = 'renderer-accessibility';}
      else errors.push('No accessible rendered mathematics found');
    }
    const rendered = Boolean(mm || find('svg,.katex-html').length);
    if (!rendered) errors.push('Math host has not rendered');
    if (!text.trim()) errors.push('Empty accessible mathematics');
    return {rendered, errors, text_source, text: text || ''};
  });
  const errors = [...article.querySelectorAll('.katex-error,mjx-merror,[data-mjx-error]')].map(e=>e.textContent);
  return {math, errors, title: document.title, article_text: article.innerText};
}'''


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if not re.fullmatch('[0-9a-f]{40}', args.revision):
        raise ValueError('A full lowercase Git commit SHA is required')
    repo = 'GoGoKo699/Quantum-Thermometry-Feedback'
    root = Path(__file__).resolve().parents[1]
    actual = subprocess.check_output(['git','rev-parse','HEAD'], cwd=root, text=True).strip()
    if actual != args.revision:
        raise ValueError('Working revision differs from requested capture')
    pages = ['README.md']
    for directory in ['science', 'learning']:
        pages.extend(str(p.relative_to(root)) for p in sorted((root/directory).glob('*.md')))
    pages.extend(['references/RELATED_WORK.md', 'verification/README.md'])
    out = Path(args.output).resolve()
    out.mkdir(parents=True, exist_ok=True)
    capture = {'schema_version':1, 'repository':repo, 'revision':actual,
               'renderer_profile':'github', 'captured_at':datetime.now(timezone.utc).isoformat(),
               'capture_method':'Playwright Chromium, pinned public GitHub blob pages; accessible MathML without TeX annotations',
               'pages':[]}
    failed = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={'width':1440,'height':1000}, device_scale_factor=1)
        page = context.new_page()
        for index, path in enumerate(pages):
            source = subprocess.check_output(['git','show',f'{actual}:{path}'], cwd=root)
            url = f'https://github.com/{repo}/blob/{actual}/{quote(path, safe="/")}'
            item = {'path':path, 'url':url, 'revision':actual,
                    'source_sha256':hashlib.sha256(source).hexdigest(), 'errors':[], 'math':[]}
            stem = f'{index+1:02d}-'+path.replace('/','_')
            try:
                response = page.goto(url, wait_until='domcontentloaded', timeout=60000)
                if response is None or response.status != 200:
                    raise RuntimeError(f'HTTP status {None if response is None else response.status}')
                page.wait_for_selector('.markdown-body', timeout=45000)
                page.wait_for_timeout(4500)
                extracted = page.evaluate(EXTRACT)
                item['math'], item['errors'] = extracted['math'], extracted['errors']
                item['observed_url'] = page.url
                if page.url != url:
                    item['errors'].append('Unexpected redirect from pinned URL')
                (out/(stem+'.txt')).write_text(extracted['article_text'], encoding='utf-8')
                (out/(stem+'.html')).write_text(page.content(), encoding='utf-8')
                page.screenshot(path=str(out/(stem+'.png')), full_page=True)
                page.locator('.markdown-body').first.screenshot(path=str(out/(stem+'-article.png')))
                for j, host in enumerate(item['math'], 1):
                    if host['errors'] or not host['rendered']:
                        failed.append(f'{path}: math {j}: {host["errors"]}')
                print(f'{path}: {len(item["math"])} math hosts; {len(item["errors"])} page errors', flush=True)
            except Exception as exc:
                item['errors'].append(f'{type(exc).__name__}: {exc}')
                try:
                    page.screenshot(path=str(out/(stem+'-failure.png')), full_page=True)
                except Exception:
                    pass
            if item['errors']:
                failed.append(f'{path}: {item["errors"]}')
            capture['pages'].append(item)
            (out/'math-capture.json').write_text(json.dumps(capture, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        browser.close()
    (out/'hosted-status.json').write_text(json.dumps({'status':'fail' if failed else 'captured', 'failures':failed}, indent=2)+'\n')
    if failed:
        raise SystemExit('\n'.join(failed))
    print('Capture complete. Source comparison and visual review remain necessary.')


if __name__ == '__main__':
    main()
