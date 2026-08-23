# Security Policy

## Scope

This repository builds a **static personal portfolio site**. Understanding the deployed
attack surface matters more than a long checklist here, so state it plainly:

| Property | Status |
|---|---|
| Server-side runtime in production | **None.** Flask runs only at build time; GitHub Pages serves flat files. |
| Database | None. |
| Authentication / authorization | None — every published page is intentionally public. |
| User input handling | None. No forms, no search, no comments, no request handlers. |
| Secrets / credentials | None. The project reads no environment variables. |
| Personal data collected | None by the application itself. |
| Third-party runtime dependencies | Font Awesome and Google Fonts via CDN (see below). |

Because there is no server-side execution path, the classic web vulnerability classes —
injection, broken access control, SSRF, insecure deserialization — do not have a reachable
sink in the deployed artifact. The realistic risk concentrates in three places instead:

1. **The build pipeline.** `requirements.txt` is pinned to exact versions specifically so a
   compromised or merely surprising upstream release cannot silently change published
   output. Deploy runs in GitHub Actions with `permissions: {}` at workflow level and
   `contents: write` granted only to the job that publishes `gh-pages`. No third-party
   marketplace actions are used in the publish step.
2. **Outbound CDN references.** `templates/base.html` loads Font Awesome from
   `cdnjs.cloudflare.com` and a webfont stylesheet from `fonts.googleapis.com`. A
   compromise at either would execute in visitors' browsers. Font Awesome is pinned with a
   Subresource Integrity hash and `crossorigin="anonymous"`, so a tampered file is
   rejected by the browser. The Google Fonts stylesheet **cannot** carry SRI — Google
   serves different CSS per user-agent, so no single hash is valid. Self-hosting the two
   font families would close that gap and is tracked in
   [docs/LIMITATIONS.md](docs/LIMITATIONS.md).
3. **Content accuracy.** Because this site presents security engineering work, an
   inaccurate claim is a real defect. Descriptions are sourced from each project's own
   README rather than written from memory, and `tools/verify_catalogue.py` fails the build
   on placeholder or dead links.

## Reporting a vulnerability

Report privately through GitHub's **Report a vulnerability** button under this
repository's *Security* tab (Private Vulnerability Reporting). Please do not open a public
issue for a security finding.

If Private Vulnerability Reporting is not yet enabled on this repository, enable it under
*Settings → Code security and analysis*.

Expected response: acknowledgement within 7 days. This is a personal project maintained
outside of business hours; there is no formal SLA and no bug bounty.

## Out of scope

- Findings against linked third-party projects — report those to their own repositories.
- Missing security headers (CSP, HSTS, X-Frame-Options). GitHub Pages does not permit
  custom response headers on `github.io` domains; this is a known and accepted limitation.
- Automated scanner output submitted without a demonstrated impact on this site.
