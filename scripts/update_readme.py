#!/usr/bin/env python3
"""Refresh only the marked repository catalog in both language versions."""
import argparse
import html
import json
import os
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- PROJECTS:START -->'
END = '<!-- PROJECTS:END -->'
ORDER = ['File-Storage', 'close-discord', 'Alias', 'AttributeTemplateFiller', 'html-web-map-exporter']


def fetch_repos(user, token=None):
    headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'Geist-profile-catalog'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    repos = []
    for page in range(1, 101):
        request = Request(f'https://api.github.com/users/{quote(user, safe="")}/repos?per_page=100&page={page}&sort=full_name', headers=headers)
        with urlopen(request, timeout=20) as response:
            chunk = json.load(response)
        if not isinstance(chunk, list):
            raise ValueError('Unexpected repository response')
        repos.extend(chunk)
        if len(chunk) < 100:
            return repos
    raise ValueError('Repository pagination exceeded limit')


def select_repos(repos, username):
    selected = [r for r in repos if not r.get('private') and r.get('visibility', 'public') == 'public' and not r.get('fork') and not r.get('archived') and r.get('name', '').casefold() != username.casefold() and r.get('owner', {}).get('login', '').casefold() == username.casefold()]
    def key(repo):
        name = repo['name']
        return (ORDER.index(name) if name in ORDER else len(ORDER), name.casefold())
    return sorted(selected, key=key)


def escape_cell(value):
    # HTML escape first; Markdown table delimiters must be escaped independently.
    return html.escape(str(value or '—'), quote=True).replace('|', '&#124;').replace('\r', ' ').replace('\n', ' ')


def format_table(repos, language, descriptions, username):
    if language == 'ru':
        lines = ['| Репозиторий | Что делает | Технологии |', '| --- | --- | --- |']
    else:
        lines = ['| Repository | What it does | Technologies |', '| --- | --- | --- |']
    for repo in repos:
        name = repo['name']
        info = descriptions.get(name, {})
        description = info.get(language) or repo.get('description') or ('Описание в репозитории.' if language == 'ru' else 'See the repository for details.')
        stack = info.get('stack') or repo.get('language') or '—'
        # Construct links from the known owner and encoded name, never from description HTML.
        url = f'https://github.com/{quote(username, safe="")}/{quote(name, safe="")}'
        lines.append(f'| [{escape_cell(name)}]({url}) | {escape_cell(description)} | {escape_cell(stack)} |')
    return '\n'.join(lines)


def replace_section(markdown, block):
    if markdown.count(START) != 1 or markdown.count(END) != 1:
        raise ValueError('Expected exactly one PROJECTS marker pair')
    a = markdown.index(START) + len(START)
    b = markdown.index(END)
    if a > b:
        raise ValueError('PROJECTS markers are reversed')
    return markdown[:a] + '\n' + block + '\n' + markdown[b:]


def update_documents(root, repos, username):
    descriptions = json.loads((root / 'scripts/projects.json').read_text(encoding='utf-8'))
    selected = select_repos(repos, username)
    if not selected:
        raise ValueError('No public repositories found; keeping existing catalogs')
    updates = {}
    # Validate both files before writing either one.
    for filename, language in [('README.md', 'en'), ('README.ru.md', 'ru')]:
        path = root / filename
        before = path.read_text(encoding='utf-8')
        after = replace_section(before, format_table(selected, language, descriptions, username))
        if after != before:
            updates[path] = after
    for path, content in updates.items():
        path.write_text(content, encoding='utf-8')
    return len(updates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixture', type=Path, help='Offline repository metadata for development')
    args = parser.parse_args()
    username = os.environ.get('USERNAME', 'Geist-dev')
    repos = json.loads(args.fixture.read_text(encoding='utf-8')) if args.fixture else fetch_repos(username, os.environ.get('GITHUB_TOKEN'))
    count = update_documents(ROOT, repos, username)
    print(f'Updated {count} README file(s)')


if __name__ == '__main__':
    main()
