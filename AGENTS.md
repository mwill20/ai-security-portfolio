# AGENTS.md

## Project Overview

This repository is Michael Williams' AI Security portfolio website. It is a Flask application that uses Frozen-Flask to generate static files for GitHub Pages.

## Repository Layout

- Source templates live in `templates/`.
- Project data lives in `projects_data.py`.
- Static assets live in `static/`.
- Static site output is generated with `python freeze.py`.
- Generated output lives in `build/`.
- GitHub Pages appears to serve from the `gh-pages` branch root.

## Build And Validation

Generate the static site:

```bash
python freeze.py
```

Expected generated pages include:

- `build/index.html`
- `build/about/index.html`
- `build/projects/index.html`

Safe local validation:

```bash
python freeze.py
```

If tests or linting are added later, run only local checks that do not require secrets or deployment credentials.

## Editing Rules

- Do not leave public-facing references to the former project name or repository slug.
- Use `ThreatPrism`, `threatprism`, and `github.com/mwill20/threatprism` for the renamed SOC analysis project.
- Preserve the identity framing: `AI Security Engineer · SOC Practitioner · Builder`.
- Do not invent metrics, production claims, or adoption claims.
- Do not edit resume content.
- Do not generate images.
- Do not add broken image references.
- Edit source files first, then regenerate `build/` with `python freeze.py`.
