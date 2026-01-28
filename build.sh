#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies (only flask/gunicorn/sklearn needed now)
pip install -r requirements.txt
