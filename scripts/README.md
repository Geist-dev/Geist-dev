# Maintaining the profile

- `README.md` is the default English profile; `README.ru.md` is the Russian version.
- The EN / RU links open the corresponding Markdown file. There is no JavaScript switch in GitHub READMEs.
- Edit the introduction, selected projects, skills and contact text in both files together.
- `projects.json` contains the bilingual descriptions and stacks used in the generated catalogs.
- `update_readme.py` refreshes only the content between the `PROJECTS` markers in both documents. It preserves everything outside those markers.
- Public, non-fork, non-archived repositories belonging to Geist-dev are included. The profile repository itself is excluded. Known featured projects appear first; the remaining repositories are sorted by name.
- New repositories use their GitHub description and primary language until a curated entry is added to `projects.json`.
- The header SVGs are local static assets for dark/light themes. No external badge or image-generation service is required.

Python 3.10+ is sufficient; there are no third-party Python dependencies.

```bash
python -m unittest discover -s tests -v
python scripts/update_readme.py --fixture tests/repos.json
```

The fixture is a public metadata snapshot for offline development and tests. To fetch live metadata, omit `--fixture`; the username defaults to Geist-dev and optional `GITHUB_TOKEN` increases the API rate limit. The workflow provides its automatically generated GitHub token; no personal token needs to be committed or configured.

CI validates pull requests without write permissions. On main, a scheduled/manual run or relevant push can refresh and commit the two catalogs. If the API fails or markers are missing, the script fails rather than replacing handwritten sections with fallback content.

The repository code and local SVG assets are covered by the root MIT license.
