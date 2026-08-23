# ai-security-portfolio

Source for **[mwill20.github.io/ai-security-portfolio](https://mwill20.github.io/ai-security-portfolio/)** —
the personal portfolio site of Michael Williams, covering security engineering, AI/ML
security, and agent tooling work.

## What this is

A small Flask application that is **never deployed as a server**. Flask is used only as a
build-time template engine: [Frozen-Flask](https://pythonhosted.org/Frozen-Flask/) walks
every route, renders it, and writes flat HTML into `build/`. GitHub Pages serves that
output.

```
templates/*.html  ──┐
                    ├──> app.py (routes) ──> freeze.py ──> build/ ──> gh-pages ──> Pages
projects_data.py  ──┘
```

The practical consequence: there is no server-side runtime in production, no database, no
authentication, and no user input handling. See [SECURITY.md](SECURITY.md).

## Quickstart

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows; use .venv/bin/activate on Linux/macOS
pip install -r requirements.txt
```

Run the site locally with live reload:

```bash
python app.py
```

Build the static output exactly as CI does:

```bash
./build.sh
```

Preview the built output:

```bash
python -m http.server -d build 8000
```

## Adding a project

Most content lives in `projects_data.py` as a dict of categories. Add an entry to the
relevant category's `projects` list:

```python
{
    "title": "Project Name",
    "description": "What it does, in one or two sentences.",
    "icon": "fas fa-shield-alt",          # Font Awesome 6 class
    "tech": ["Python", "FastAPI"],        # optional; renders as tag pills
    "links": [
        {"label": "View on GitHub", "url": "https://github.com/...", "class": "btn-primary"}
    ],
}
```

Required keys are `title`, `description`, `icon`, and a non-empty `links` list —
`templates/projects.html` dereferences `project.links[0].url` without a guard, so an
entry with no links will raise at build time.

**Category order matters.** The filter buttons in `templates/projects.html` are listed
`mcp, security, agents, ml, cloud, fun`; because Python preserves dict insertion order,
`projects_data.py` must declare its keys in that same order for the page to match the bar.

The `Featured` block at the top of `templates/projects.html` is hand-written HTML, not
data-driven. Editing it means editing that template directly.

Run the catalogue checks before committing:

```bash
python tools/verify_catalogue.py
```

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which installs pinned
dependencies, runs `freeze.py`, verifies the expected pages exist, and force-pushes
`build/` to the `gh-pages` branch as an orphan commit. GitHub Pages serves `gh-pages`.

`build/` is generated output and is **not** committed to `main`.

## Configuration

None. This project reads no environment variables and has no secrets, so there is no
`.env.example` — deliberately, rather than by omission. If configuration is ever
introduced, add `.env.example` with placeholder values at the same time.

## Repository layout

| Path | Purpose |
|---|---|
| `app.py` | Flask routes (build-time only) |
| `projects_data.py` | Project catalogue data |
| `freeze.py` | Frozen-Flask entry point |
| `templates/` | Jinja templates; `projects.html` is part hand-written, part data-driven |
| `static/` | CSS, JS, images, resume |
| `tools/verify_catalogue.py` | Coverage, link, and schema checks |
| `docs/` | Architecture, limitations, and page-maintenance notes |

## License

See [LICENSE](LICENSE).
