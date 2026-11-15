#!/usr/bin/env python3
"""Refresh or check the content fingerprints of Enterprise Agentgateway skills."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'skills/catalog.json'


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if package metadata is stale')
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text())
    for name in catalog['skills']:
        if name not in ('agentgateway-enterprise-standalone', 'agentgateway-enterprise-kubernetes'):
            raise SystemExit(f'Unexpected skill in catalog: {name}')
        folder = ROOT / 'skills' / name
        path = folder / 'package.json'
        if not re.search(rf'^name: {re.escape(name)}\s*$', (folder / 'SKILL.md').read_text(), re.M):
            raise SystemExit(f'Skill name differs from directory: {name}')
        current = json.loads(path.read_text())
        files = {}
        for file in sorted(folder.rglob('*')):
            if file.is_symlink():
                raise SystemExit(f'Symlink in skill package: {file}')
            if not file.is_file() or file.name == 'package.json':
                continue
            relative = file.relative_to(folder).as_posix()
            if relative.startswith('.') or file.suffix not in ('.md', '.yaml', '.py', '.json'):
                raise SystemExit(f'Unexpected skill file: {file}')
            if file.suffix == '.md':
                for target in re.findall(r'\]\(([^)]+)\)', file.read_text()):
                    if re.match(r'\w+://|mailto:|#', target):
                        continue
                    resolved = (file.parent / target.split('#')[0]).resolve()
                    if not resolved.is_relative_to(folder.resolve()) or not resolved.is_file():
                        raise SystemExit(f'Broken skill reference: {file}: {target}')
            files[relative] = digest(file.read_bytes())
        expected = dict(current)
        expected['channel'] = catalog['channel']
        expected['files_sha256'] = files
        expected['source'] = dict(current['source'], repository='https://github.com/solo-io/doc-examples',
                                  path=f'skills/{name}', commit=None, state='content-addressed',
                                  content_sha256=digest(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()))
        if args.check:
            if current != expected:
                raise SystemExit(f'Stale package metadata: {path.relative_to(ROOT)}')
        else:
            path.write_text(json.dumps(expected, indent=2) + '\n')
    print(f"{'Checked' if args.check else 'Refreshed'} {len(catalog['skills'])} Enterprise skill identities")


if __name__ == '__main__':
    main()
