<p align="right"><strong>EN</strong> · <a href="README.ru.md">RU</a></p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img src="assets/header-light.svg" alt="Geist-dev — software developer. Web applications, automation and useful tools." width="960">
</picture>

**Python · Web applications · Automation · GIS · LLM-assisted development**

I build personal projects that solve practical tasks: storing files, organizing team games, automating repetitive work, and sharing geographic data on the web. I work across backend logic, browser interfaces, desktop plugins, testing, and project setup.

I use **Codex and Claude** as development tools, from exploring an idea and building a prototype to debugging, refactoring, writing tests, and documenting the result. My goal is to turn an idea into software that another person can run and understand.

[Selected projects](#selected-projects) · [Technologies](#technologies-and-tools) · [LLM workflow](#working-with-llms) · [Contact](#contact)

## Selected projects

### [File Storage](https://github.com/Geist-dev/File-Storage)

A personal file library with account isolation, uploads, folders, tags, search, image previews, and trash recovery.

**Python · FastAPI · SQLAlchemy · SQLite · JavaScript**

- JWT authentication, bcrypt password hashing, and server-side ownership checks.
- Files on disk, metadata in SQLite, and thumbnails generated with Pillow.
- API tests, a browser regression scenario, and a single command to set up and run the app.

[Code and startup guide](https://github.com/Geist-dev/File-Storage#readme) · [Screenshots](https://github.com/Geist-dev/File-Storage#скриншоты) · [CI](https://github.com/Geist-dev/File-Storage/actions)

<details>
<summary>Preview: file library</summary>

![File Storage library](https://raw.githubusercontent.com/Geist-dev/File-Storage/main/docs/screenshots/02-library.png)

</details>

### [Close Bot](https://github.com/Geist-dev/close-discord)

A Discord bot that helps organize team matches and tournaments in CS2, Dota 2, and Valorant.

**Python · disnake · asyncio · SQLite · Discord API**

- Slash commands, buttons, registration, team selection, and match channels.
- Persistent match settings and temporary restrictions with recovery after interruptions.
- Configuration validation, an isolated test-server mode, and automated tests.

[Code and startup guide](https://github.com/Geist-dev/close-discord#readme) · [Screenshots](https://github.com/Geist-dev/close-discord#скриншоты) · [CI](https://github.com/Geist-dev/close-discord/actions)

### [Alias](https://github.com/Geist-dev/Alias)

A multiplayer browser word game: players form teams, explain words, and keep score against a timer.

**Node.js · Express · WebSocket · JavaScript · HTML / CSS**

- A word is sent only to the active explainer; the server checks host permissions and game actions.
- Pausing, score corrections, alternating turns, and session recovery after reconnection.
- Game-rule tests, real WebSocket tests, and a four-client browser scenario.

[Code and startup guide](https://github.com/Geist-dev/Alias#readme) · [Screenshots](https://github.com/Geist-dev/Alias#скриншоты) · [CI](https://github.com/Geist-dev/Alias/actions)

<details>
<summary>Preview: the explainer's turn</summary>

![Alias explainer view](https://raw.githubusercontent.com/Geist-dev/Alias/main/docs/screenshots/02-explainer.png)

</details>

### GIS tools for QGIS

I also develop Python plugins for geographic workflows and repetitive data-entry tasks.

| Project | Purpose | Technologies |
| --- | --- | --- |
| [AttributeTemplateFiller](https://github.com/Geist-dev/AttributeTemplateFiller) | Reusable attribute presets, autofill for new vector features, and JSON import/export. | Python · PyQGIS · PyQt · QSettings |
| [HTML Web Map Exporter](https://github.com/Geist-dev/html-web-map-exporter) | Export QGIS projects as interactive HTML maps with layers, labels, and a legend. | Python · PyQGIS · PyQt · HTML / JavaScript |

## Technologies and tools

The following reflects tools used across my projects and development workflow. Individual repositories show the actual implementation and scope.

| Area | Technologies and tasks |
| --- | --- |
| Languages and interfaces | Python, JavaScript, HTML5, CSS3; responsive layouts, DOM events, forms, browser storage, dark/light themes. |
| Backend and APIs | FastAPI, Uvicorn, Pydantic, Express, Node.js, HTTP / REST, JSON, request validation, WebSocket communication, asynchronous Python. |
| Data and files | SQLite, SQLAlchemy, SQL queries, filesystem storage, metadata, filtering, pagination, image thumbnails with Pillow. |
| Authentication and application checks | JWT, bcrypt, ownership and role checks, input validation, upload limits, environment variables, `.env` configuration, safe text rendering. |
| Bots and integrations | Discord API, disnake, slash commands, interactive components, channels and roles; Telegram bot projects and automation. |
| GIS and desktop tooling | QGIS, PyQGIS, PyQt, Qt widgets, QSettings, attribute templates, vector/raster layers, coordinate transformations, HTML map export. |
| Testing and debugging | pytest, unittest, Node.js test runner, API and WebSocket checks, Playwright / Chromium, browser developer tools, regression scenarios. |
| Development and delivery | Git, GitHub, branches, pull requests, GitHub Actions, CI, Bash, Python `venv`, pip, npm, lockfiles, setup scripts, GitHub Pages. |
| LLM tools | Codex, Claude, task decomposition, prompting, working with repository context, iterative implementation and review. |

<details>
<summary>Additional experience and environments</summary>

React, Docker, and Java are also part of my broader technology experience. I work with Linux, macOS, and Windows, and account for shell and environment differences in setup instructions.

My project interests include Telegram bots, community tools, VPN-related tooling, and small utilities. The featured repositories above are the clearest examples to explore first.

</details>

## Working with LLMs

I use LLM coding tools as part of an iterative development process:

1. Break an idea into concrete behavior, constraints, and small tasks.
2. Work with the existing code and give the model relevant repository context.
3. Implement and revise features, investigate errors, and review suggested changes.
4. Check behavior with automated tests and hands-on application runs.
5. Prepare setup instructions, screenshots, configuration examples, and changes for GitHub.

My current focus is **building and improving software with Codex and Claude**. I am interested in practical LLM applications and in making this workflow more reliable through clearer tasks and verification.

## What you can inspect here

The featured repositories include startup instructions, configuration examples, real screenshots, and tests. Their READMEs explain architecture and current limitations. I care about making projects reproducible: download the code, follow the instructions, and try the result.

<details>
<summary>All public repositories</summary>

This catalog is refreshed automatically. The two language versions share one set of curated project descriptions.

<!-- PROJECTS:START -->
| Repository | What it does | Technologies |
| --- | --- | --- |
| [File-Storage](https://github.com/Geist-dev/File-Storage) | Personal file storage with authentication, upload, tags, search and trash recovery. | Python · FastAPI · SQLite · JavaScript |
| [close-discord](https://github.com/Geist-dev/close-discord) | Discord bot for organizing team matches and tournaments in CS2, Dota 2 and Valorant. | Python · disnake · SQLite |
| [Alias](https://github.com/Geist-dev/Alias) | Browser word game with teams, private words, a timer, scoring and reconnect support. | Node.js · Express · WebSocket |
| [AttributeTemplateFiller](https://github.com/Geist-dev/AttributeTemplateFiller) | QGIS plugin for reusable attribute presets and automatic filling of new vector features. | Python · PyQGIS · PyQt |
| [html-web-map-exporter](https://github.com/Geist-dev/html-web-map-exporter) | QGIS plugin for exporting projects as interactive HTML web maps. | Python · PyQGIS · HTML / JavaScript |
| [geist-dev.github.io](https://github.com/Geist-dev/geist-dev.github.io) | Personal website with information, projects and contact links. | HTML · CSS · JavaScript |
| [geist-discord.github.io](https://github.com/Geist-dev/geist-discord.github.io) | Developer portfolio with two themes and optional live Discord and Spotify presence. | HTML · CSS · JavaScript · Express |
<!-- PROJECTS:END -->

</details>

## Contact

I am interested in software development opportunities and collaboration on useful projects.

**Telegram:** [@flipgood](https://t.me/flipgood)

**Email:** [aeromax.live@mail.ru](mailto:aeromax.live@mail.ru)

**GitHub:** [Geist-dev](https://github.com/Geist-dev)
