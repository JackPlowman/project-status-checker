#!/bin/bash
set -e +x

# Check if there are any changes in the watched folder
if git diff --cached --name-only | grep -q "^checker/"; then
  just install
  just ruff-fix
fi
