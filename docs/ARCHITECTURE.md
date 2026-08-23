# Architecture

## System overview

This is a **static site generator disguised as a web app**. Flask never serves production
traffic; it is a build-time template engine whose output is committed to a branch that
GitHub Pages serves.

```
                 build time (local or CI)                    runtime (visitors)
 ┌──────────────────────────────────────────────┐      ┌──────────────────────────┐
 │  projects_data.py ──┐                        │      │                          │
 │                     ├─> app.py routes        │      │   GitHub Pages CDN       │
 │  templates/*.html ──┘        │               │      │        │                 │
 │                              v               │      │        v                 │
 │                        freeze.py             │      │   flat HTML + static     │
 │                    (Frozen-Flask walks       │      │   no server, no DB       │
 │                     every route)             │      │                          │
 │                              │               │      └──────────────────────────┘
 │                              v               │                  ^
 │                          build/  ────────────┼── git push ──> gh-pages branch
 └──────────────────────────────────────────────┘
```

## Components

| Component | Responsibility |
|---|---|
| `app.py` | Declares three routes: `/`, `/about/`, `/projects/`. Injects `now` for the footer year. Nothing else. |
| `projects_data.py` | The project catalogue: a dict of six categories, each holding a list of project dicts. |
| `freeze.py` | Frozen-Flask entry point. `FREEZER_RELATIVE_URLS = True` so output works both at the `/ai-security-portfolio/` sub-path and at a domain root. |
| `templates/` | Jinja templates extending `base.html`. |
| `tools/verify_catalogue.py` | Pre-commit checks: repo coverage, link liveness, entry schema. |
| `.github/workflows/deploy.yml` | Builds and publishes on push to `main`. |

## The one non-obvious thing in this codebase

**`templates/projects.html` is half hand-written HTML and half data-driven.** Read this
before editing it.

- The **Featured** block (ThreatPrism, AI DevSecOps, SecureCLI-Tuner) is hand-authored
  HTML with inline styles. It is not generated from `projects_data.py`.
- Everything below it is a `{% for key, category in projects.items() %}` loop over
  `projects_data.py`.

- The **MCP Ecosystem** category additionally renders a hand-written network diagram,
  `templates/_mcp_ecosystem.html`, included above its card grid.

The MCP diagram is worth understanding, because an earlier version of it caused a real
bug. It used to be a full hand-written *replacement* for the MCP category, and the loop
carried an `{% if key != 'mcp' %}` guard so it would not render twice. The effect was that
the `mcp` section of `projects_data.py` was dead data - edits to it silently changed
nothing on the published site.

It is now a **decoration, not a replacement**: the guard is gone, the diagram is included
*in addition to* the category's normal card grid, and MCP cards come from
`projects_data.py` like every other category. The projects the diagram depicts each link
their own repository from within the diagram, and `tools/verify_catalogue.py` scans every
template, so those repos still count as covered.

**Do not turn a category back into hand-written markup that replaces its cards** - that is
what created the dead-data trap. Adding decoration above the grid is fine.

## Category ordering contract

The filter bar in `templates/projects.html` hardcodes button order:

```
all · mcp · security · agents · ml · cloud · fun
```

The rendered sections come from `projects_data.py` in **dict insertion order**. These two
orderings must agree, or the page reads inconsistently with its own filter bar. There is
no code enforcing this — it is a convention, checked by eye and by
`tools/verify_catalogue.py`.

Each rendered group carries `data-category="{{ key }}"`, and the filter JavaScript matches
that against the button's `data-filter`. A button whose `data-filter` has no matching
category silently filters to an empty page — which is exactly what `ml` did before the
`ml` category was added.

## Data contract

```python
projects = {
    "<key>": {
        "title": str,          # section heading
        "icon": str,           # Font Awesome class
        "description": str,    # optional; only "mcp" uses one today
        "projects": [
            {
                "title": str,        # required
                "description": str,  # required
                "icon": str,         # required
                "tech": [str],       # optional -> renders tag pills
                "links": [           # required, non-empty
                    {"label": str, "url": str, "class": "btn-primary|btn-secondary|btn-success"}
                ],
            },
        ],
    },
}
```

`templates/projects.html` reads `project.links[0].url` as the card-title href **without a
guard**, so an entry with an empty `links` list raises at freeze time rather than
degrading gracefully. `tools/verify_catalogue.py` asserts against this.

A `badge` key appears on two legacy entries. The data-driven loop does not render it; it
is inert. Do not add it to new entries.

## Design decisions

**Why Frozen-Flask rather than a dedicated SSG (Hugo, Eleventy, Astro)?**
The site predates the question and the Jinja templates already existed. The trade is a
Python build dependency in exchange for not rewriting the templates. Revisit if the
catalogue outgrows a single Python dict.

**Why is `build/` not committed?**
It was, until generated output and source drifted. CI now regenerates it on every push to
`main`, so the artifact has exactly one producer.

**Why publish with plain `git` instead of a marketplace Action?**
The publish step needs write access to a branch. A third-party Action would be an
unaudited dependency holding that access, on a repository whose subject is security
engineering. Ten lines of `git` avoid the trade entirely.

**Why an orphan commit on every deploy?**
So that files deleted from source stop being served. A non-orphan publish leaves removed
routes live indefinitely — that is how a broken `/sagevault` placeholder stayed reachable
after its route stopped being meaningful.
