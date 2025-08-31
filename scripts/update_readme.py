#!/usr/bin/env python3
import os, re, sys, html
import requests
from datetime import datetime, timezone

USERNAME = os.getenv("USERNAME", "").strip() or "Geist-dev"
MAX_REPOS = int(os.getenv("MAX_REPOS", "6"))
FEATURED_TOPIC = os.getenv("FEATURED_TOPIC", "featured").strip()
EXCLUDE_FORKS = os.getenv("EXCLUDE_FORKS", "true").lower() == "true"
EXCLUDE_ARCHIVED = os.getenv("EXCLUDE_ARCHIVED", "true").lower() == "true"

API = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
# GITHUB_TOKEN даёт больше лимит и доступ к topics
token = os.getenv("GITHUB_TOKEN")
if token:
    HEADERS["Authorization"] = f"Bearer {token}"
    HEADERS["Accept"] = "application/vnd.github+json; application/vnd.github.mercy-preview+json"

def fetch_repos(user):
    repos = []
    page = 1
    while True:
        r = requests.get(f"{API}/users/{user}/repos", headers=HEADERS, params={
            "per_page": 100, "page": page, "sort": "pushed"
        })
        r.raise_for_status()
        chunk = r.json()
        if not chunk:
            break
        repos.extend(chunk)
        page += 1
    return repos

def pick_stack(repo):
    # Стек: берём topics (если есть), иначе — основная language
    topics = repo.get("topics") or []
    if topics:
        return ", ".join(topics[:5])
    lang = repo.get("language")
    return lang or "—"

def esc(s): return html.escape(s or "")

def format_table(repos):
    lines = []
    lines.append("| Проект | Описание | Стек | Ссылка |")
    lines.append("|--------|----------|------|--------|")
    for r in repos:
        name = r["name"]
        desc = r.get("description") or "—"
        url = r["html_url"]
        stack = pick_stack(r)
        # Можно добавить эмодзи по topic'ам
        lines.append(f"| **{esc(name)}** | {esc(desc)} | {esc(stack)} | [GitHub]({url}) |")
    return "\n".join(lines)

def sort_repos(repos):
    # Сначала featured topic, потом по pushed_at (desc)
    def key(r):
        featured = 0
        topics = r.get("topics") or []
        if FEATURED_TOPIC and FEATURED_TOPIC in topics:
            featured = -1  # выше
        pushed = r.get("pushed_at") or r.get("updated_at") or "1970-01-01T00:00:00Z"
        return (featured, pushed)
    return sorted(repos, key=key, reverse=True)

def filter_repos(repos):
    out = []
    for r in repos:
        if EXCLUDE_FORKS and r.get("fork"):
            continue
        if EXCLUDE_ARCHIVED and r.get("archived"):
            continue
        out.append(r)
    return out

def replace_section(md, new_block):
    start = "<!-- PROJECTS:START -->"
    end = "<!-- PROJECTS:END -->"
    pat = re.compile(rf"({re.escape(start)})(.*)({re.escape(end)})", re.DOTALL)
    if not pat.search(md):
        # если маркеры забыли — добавим секцию в конец
        return md.rstrip() + f"\n\n### 🧩 Проекты\n\n{start}\n{new_block}\n{end}\n"
    return pat.sub(rf"\1\n{new_block}\n\3", md)

def main():
    repos = fetch_repos(USERNAME)
    repos = filter_repos(repos)

    # получить topics для репо (некоторые endpoints не отдают topics без отдельного запроса)
    # попробуем обогатить только первые 30, чтобы не шуметь
    for r in repos[:30]:
        try:
            rr = requests.get(f"{API}/repos/{USERNAME}/{r['name']}", headers=HEADERS)
            if rr.ok:
                r.update(rr.json())
        except Exception:
            pass

    repos = sort_repos(repos)[:MAX_REPOS]
    table = format_table(repos)

    path = "README.md"
    with open(path, "r", encoding="utf-8") as f:
        md = f.read()
    new_md = replace_section(md, table)

    if new_md != md:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_md)
        print("README updated ✔")
    else:
        print("No changes")

if __name__ == "__main__":
    main()
