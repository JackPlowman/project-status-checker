#!/bin/sh
set -e +x

if [ "$CI" = "true" ]; then
  # if running in GitHub Actions, change to the root of the repository
  cd ..
  cd ..
fi

# Run the checker
python -m checker

# if [ "$CI" = "true" ]; then
#   # if running in GitHub Actions, copy the output to the output directory
#   cp original_files github/workspace/output_files
# fi
