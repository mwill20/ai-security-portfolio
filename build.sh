#!/usr/bin/env bash
# Build the static site into build/.
# Frozen-Flask walks every route in app.py and writes the rendered HTML to disk;
# GitHub Pages serves that output. Flask itself never runs in production.
set -o errexit
set -o nounset
set -o pipefail

pip install -r requirements.txt
python freeze.py

echo "Static site written to build/ ($(find build -type f | wc -l) files)."
