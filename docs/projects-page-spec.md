# Projects Page Maintenance Notes

This portfolio presents cybersecurity as Michael Williams' professional foundation and AI security / guardrail engineering as the visible technical direction.

## Current Featured Framing

- ThreatPrism: production-deployed SOC investigation pipeline.
- AI DevSecOps Platform: validated security research, not an operational deployment.
- SecureCLI-Tuner: security research for safer agentic DevOps command generation.

## Naming And Links

- Use `ThreatPrism` for the SOC investigation pipeline.
- Link ThreatPrism to `https://github.com/mwill20/threatprism`.
- Do not reintroduce old project names or old repository links.

## Category Rules

- Keep `Just for Fun`.
- Do not add a `Tools` category.
- Do not add unready or placeholder projects.
- Keep project imagery consistent: either all featured cards have images or none do. The current page uses no featured project images.

## AI DevSecOps Accuracy

AI DevSecOps Platform was validated as AI security engineering research across 57 adversarial test cases with zero false negatives. It should not be described as deployed or release-ready.

## Build

After source edits, regenerate the static site with:

```powershell
python freeze.py
```

The generated output lives in `build/`.
