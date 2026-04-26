# Deployment

This portfolio is a Flask + Frozen-Flask site. Source changes happen on `main`; static GitHub Pages output is generated into `build/`; the live site appears to be served from the `gh-pages` branch root.

## Manual Deployment Flow

1. Edit source templates, project data, and static assets on `main`.
2. Generate the static site:

   ```bash
   python freeze.py
   ```

3. Review the generated output:

   ```bash
   git status
   ```

   Confirm the expected generated pages changed:

   ```text
   build/index.html
   build/about/index.html
   build/projects/index.html
   ```

4. Deploy the contents of `build/` to the root of the `gh-pages` branch.
5. Verify the live site at:

   ```text
   https://mwill20.github.io/ai-security-portfolio/index.html
   ```

## Safe Command Sequence

Use a temporary worktree so `main` and `gh-pages` remain separate:

```bash
git checkout main
python freeze.py
git worktree add /tmp/ai-security-portfolio-gh-pages gh-pages
rsync -av --delete build/ /tmp/ai-security-portfolio-gh-pages/
cd /tmp/ai-security-portfolio-gh-pages
git status
git add .
git commit -m "Deploy ThreatPrism portfolio updates"
git push origin gh-pages
cd -
git worktree remove /tmp/ai-security-portfolio-gh-pages
```

On Windows, use Git Bash, WSL, or an equivalent copy command that preserves the same behavior as `rsync -av --delete build/ <gh-pages-worktree>/`.

## Notes

- Do not deploy resume changes unless the resume was intentionally updated outside this cleanup.
- Do not add image references unless the referenced files already exist.
- Keep deployment commits focused on generated `build/` output copied to `gh-pages`.
