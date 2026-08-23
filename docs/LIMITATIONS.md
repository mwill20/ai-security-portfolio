# Limitations

What this project does not do, and when not to use it as a reference.

## By design

- **No server-side runtime.** There is no API, no database, no session state, and no way
  to accept user input. Anything requiring those is out of scope for this repository.
- **No search, pagination, or sorting.** The projects page renders every card at once and
  filters client-side by category. This is fine at the current catalogue size and will
  degrade — as page weight and scroll length, not as an error — well before it breaks.
- **Content is hand-maintained.** Project cards are written into `projects_data.py` by
  hand; nothing polls the GitHub API at build time. A repo renamed on GitHub goes stale
  here until someone updates it. `tools/verify_catalogue.py` detects that drift but does
  not repair it.
- **No analytics or tracking.** No visitor data is collected by the site itself. GitHub
  may log requests at the Pages layer; that is outside this repository's control.

## Known gaps

- **The Google Fonts stylesheet has no Subresource Integrity.** Google serves different
  CSS per user-agent, so no single hash is valid. Self-hosting Inter and Fira Code would
  remove the third-party origin entirely. Not yet done.
- **No security response headers.** Content-Security-Policy, HSTS, and X-Frame-Options
  cannot be set on `github.io` — GitHub Pages does not support custom headers. A CSP
  `<meta>` tag could cover part of the gap but has not been added.
- **The Featured block is not data-driven.** Three projects live as hand-written HTML with
  inline styles in `templates/projects.html`. They cannot be reordered, filtered, or
  validated by the catalogue checks the way `projects_data.py` entries can.
- **`static/videos/sagevault-demo.mp4` (4.6 MB) is unreferenced.** No template links it.
  It is copied into every build and published to `gh-pages` regardless. Either surface it
  on a real SageVault page or remove it.
- **No automated accessibility or visual-regression testing.** Contrast, focus order, and
  screen-reader behavior have not been formally audited.
- **No link checking of external destinations at build time.**
  `tools/verify_catalogue.py` verifies links when run, but CI does not currently fail on a
  third-party URL that rots after publication.

## Accuracy boundary

Project descriptions are derived from each project's own README or GitHub description.
Where a README states a metric, the card may repeat it; the metric is that project's
claim, reproduced, not an independent benchmark run for this site. Nothing here is an
audited or third-party-verified result.
