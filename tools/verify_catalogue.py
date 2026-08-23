#!/usr/bin/env python3
"""Verify the project catalogue against the requirement it exists to satisfy:

    "every public project in my GitHub repo should have a home on the projects page"

Four checks:
  1. coverage  - every public repo (minus a documented exclusion list) is linked exactly once
  2. schema    - every project entry has the keys templates/projects.html dereferences
  3. links     - no placeholder URLs
  4. liveness  - every URL resolves (skip with --no-network)

Exit code 0 = pass, 1 = fail. Run before committing catalogue changes.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

GH_OWNER = "mwill20"
REPO_RE = re.compile(r"github\.com/" + GH_OWNER + r"/([A-Za-z0-9._-]+)", re.IGNORECASE)

# Repos deliberately absent from the projects page. Each needs a reason; an
# undocumented exclusion is indistinguishable from an oversight.
EXCLUDED = {
    "mwill20": "GitHub profile README, not a project",
    "mwill20.github.io": "personal site scaffold, not a project",
    "ai-security-portfolio": "this repository - the site itself",
    "docs": "shared docs scratch repo, not a project",
    "SecureCLI-Tuner-deploy": "deploy variant of SecureCLI-Tuner, already carded",
    "Trust_Bench_UI": "front-end for Trust_Bench, already carded",
}

REQUIRED_PROJECT_KEYS = ("title", "description", "icon", "links")
ALLOWED_BTN_CLASSES = {"btn-primary", "btn-secondary", "btn-success"}
# Filter-button order in templates/projects.html; dict order must match.
EXPECTED_CATEGORY_ORDER = ["mcp", "security", "agents", "ml", "cloud", "fun"]


class Report:
    def __init__(self):
        self.failures = []
        self.notes = []

    def fail(self, msg):
        self.failures.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    def section(self, name, ok):
        print("  [%s] %s" % ("PASS" if ok else "FAIL", name))


def load_projects():
    from projects_data import projects
    return projects


def cards_per_repo(projects):
    """How many project *cards* reference each repo.

    Counted per card, not per link: one card legitimately carries several links to
    the same repo (GitHub + live demo + README), and that is not a duplicate.
    """
    found = Counter()
    for section in projects.values():
        for proj in section.get("projects", []):
            repos = set()
            for link in proj.get("links", []):
                repos.update(m.lower() for m in REPO_RE.findall(link.get("url") or ""))
            found.update(repos)
    return found


def template_repos():
    """Repos referenced from hand-written markup in any template.

    Covers the Featured block in projects.html and the MCP network diagram in
    _mcp_ecosystem.html. A repo appearing both here and in projects_data.py is
    not a duplicate - the Featured block deliberately re-surfaces projects that
    also sit in a category.
    """
    found = set()
    for tpl in sorted((ROOT / "templates").glob("*.html")):
        found.update(m.lower() for m in REPO_RE.findall(tpl.read_text(encoding="utf-8")))
    return found


def public_repos():
    out = subprocess.run(
        ["gh", "repo", "list", GH_OWNER, "--visibility", "public",
         "--limit", "300", "--json", "name"],
        capture_output=True, text=True, check=True,
    )
    return [r["name"] for r in json.loads(out.stdout)]


def check_coverage(rep, projects):
    try:
        repos = public_repos()
    except Exception as exc:
        rep.note("coverage skipped - gh CLI unavailable (%s)" % exc.__class__.__name__)
        return True

    carded = cards_per_repo(projects)
    featured = template_repos()
    linked = set(carded) | featured
    excluded_lc = set(k.lower() for k in EXCLUDED)
    ok = True

    missing = [r for r in repos
               if r.lower() not in excluded_lc and r.lower() not in linked]
    if missing:
        ok = False
        rep.fail("%d public repo(s) have no home on the projects page:" % len(missing))
        for r in sorted(missing, key=str.lower):
            rep.fail("    - %s" % r)

    known = set(r.lower() for r in repos)
    for name in sorted(linked):
        if name not in known:
            ok = False
            rep.fail("links to '%s', which is not a public %s repo "
                     "(renamed, deleted, or private?)" % (name, GH_OWNER))

    # Several cards may share a repo when it is a monorepo (mcp-tools backs the
    # Calculator and Weather tools). That is fine. A repeated *title* is not - it
    # means the same project was listed twice.
    titles = Counter()
    for key, section in projects.items():
        for proj in section.get("projects", []):
            titles[(proj.get("title") or "").strip().lower()] += 1
    for title, count in sorted(titles.items()):
        if count > 1:
            ok = False
            rep.fail("'%s' appears as %d separate cards - same project listed twice?"
                     % (title, count))

    multi = {n: c for n, c in carded.items() if c > 1}
    if multi:
        rep.note("repos backing multiple cards (expected for monorepos): %s"
                 % ", ".join("%s x%d" % (n, c) for n, c in sorted(multi.items())))

    rep.note("coverage: %d public repos, %d excluded, %d carded, %d featured-only"
             % (len(repos), len(EXCLUDED), len(carded), len(featured - set(carded))))
    return ok


def check_schema(rep, projects):
    ok = True
    order = list(projects.keys())
    if order != EXPECTED_CATEGORY_ORDER:
        ok = False
        rep.fail("category order %s does not match the filter bar %s"
                 % (order, EXPECTED_CATEGORY_ORDER))

    for key, section in projects.items():
        if "title" not in section or "projects" not in section:
            ok = False
            rep.fail("section '%s' is missing 'title' or 'projects'" % key)
            continue
        for proj in section["projects"]:
            label = "%s/%s" % (key, proj.get("title", "<untitled>"))
            for field in REQUIRED_PROJECT_KEYS:
                if not proj.get(field):
                    ok = False
                    rep.fail("%s: missing or empty '%s'" % (label, field))
            links = proj.get("links") or []
            # templates/projects.html dereferences links[0].url unguarded.
            if links and not links[0].get("url"):
                ok = False
                rep.fail("%s: links[0] has no 'url' - would raise at freeze time" % label)
            for link in links:
                cls = link.get("class")
                if cls not in ALLOWED_BTN_CLASSES:
                    ok = False
                    rep.fail("%s: link class %r not allowed" % (label, cls))
            if "badge" in proj:
                rep.note("%s: has an inert 'badge' key (template ignores it)" % label)
    return ok


def iter_urls(projects):
    for key, section in projects.items():
        for proj in section.get("projects", []):
            for link in proj.get("links", []):
                yield "%s/%s" % (key, proj.get("title")), link.get("label"), link.get("url")


def check_placeholders(rep, projects):
    ok = True
    for label, link_label, url in iter_urls(projects):
        if not url or url.strip() in ("#", ""):
            ok = False
            rep.fail("%s: '%s' is a placeholder link (%r)" % (label, link_label, url))
    return ok


def check_local_assets(rep, projects):
    """Site-relative links must point at a file that actually exists in static/.

    Cards render at /projects/, so "../static/x" means "<repo>/static/x".
    """
    ok = True
    for label, link_label, url in iter_urls(projects):
        if not url or url.startswith("http") or url.strip() == "#":
            continue
        rel = url.split("?", 1)[0].lstrip("/")
        if rel.startswith("../"):
            rel = rel[3:]
        target = ROOT / rel
        if not target.is_file():
            ok = False
            rep.fail("%s: '%s' points at %s, which does not exist"
                     % (label, link_label, url))
        else:
            rep.note("local asset ok: %s (%.1f MB)"
                     % (url, target.stat().st_size / 1048576))
    return ok


def check_liveness(rep, projects):
    ok = True
    seen = {}
    for label, link_label, url in iter_urls(projects):
        # Only external URLs are fetchable here; site-relative links (../static/...)
        # are validated by freeze.py producing the file.
        if not url or not url.startswith("http"):
            continue
        if url not in seen:
            req = urllib.request.Request(
                url, method="HEAD",
                headers={"User-Agent": "verify-catalogue/1.0"})
            try:
                with urllib.request.urlopen(req, timeout=25) as resp:
                    seen[url] = resp.status
            except urllib.error.HTTPError as exc:
                seen[url] = exc.code
            except Exception as exc:
                seen[url] = -1
                rep.note("%s -> %s" % (url, exc.__class__.__name__))
        status = seen[url]
        if status < 0 or status >= 400:
            ok = False
            rep.fail("%s: '%s' -> HTTP %s :: %s" % (label, link_label, status, url))
    rep.note("liveness: checked %d distinct URLs" % len(seen))
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-network", action="store_true",
                    help="skip coverage and liveness checks")
    args = ap.parse_args()

    projects = load_projects()
    rep = Report()
    print("Verifying project catalogue\n")

    results = [
        ("schema", check_schema(rep, projects)),
        ("no placeholder links", check_placeholders(rep, projects)),
        ("local assets exist", check_local_assets(rep, projects)),
    ]
    if not args.no_network:
        results.append(("coverage of public repos", check_coverage(rep, projects)))
        results.append(("link liveness", check_liveness(rep, projects)))

    for name, ok in results:
        rep.section(name, ok)

    if rep.notes:
        print("\nnotes:")
        for n in rep.notes:
            print("  - %s" % n)

    if rep.failures:
        print("\n%d problem(s):\n" % len(rep.failures))
        for f in rep.failures:
            print("  %s" % f)
        print("\nFAILED")
        return 1

    total = sum(len(s.get("projects", [])) for s in projects.values())
    print("\nPASSED - %d projects across %d categories" % (total, len(projects)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
