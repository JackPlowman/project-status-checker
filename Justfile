# ------------------------------------------------------------------------------
# Common Commands
# ------------------------------------------------------------------------------

# Install all python dependencies
install:
    poetry install

# Run the checker
run:
    poetry run python -m checker

# Run the checker with the default full example
run-with-defaults:
    INPUT_DATABASE_FILE_PATH="status-checker-database.db" \
    INPUT_CONFIG_FILE_PATH="examples/full_example.json" \
    poetry run python -m checker

# ------------------------------------------------------------------------------
# Test Commands
# ------------------------------------------------------------------------------

# Run unit tests
unit-test:
    poetry run pytest checker --cov=. --cov-report=xml

# Run GitHub Summary tests
test-github-summary:
    poetry run pytest tests/github_summary

# ------------------------------------------------------------------------------
# Cleaning Commands
# ------------------------------------------------------------------------------

# Clean up all cache and temporary files
clean:
    find . \( \
      -name '__pycache__' -o \
      -name '.coverage' -o \
      -name '.mypy_cache' -o \
      -name '.pytest_cache' -o \
      -name '.ruff_cache' -o \
      -name '*.pyc' -o \
      -name '*.pyd' -o \
      -name '*.pyo' -o \
      -name 'coverage.xml' -o \
      -name 'db.sqlite3' \
    \) -print | xargs rm -rfv

# ------------------------------------------------------------------------------
# Docker Commands
# ------------------------------------------------------------------------------

# Build the Docker image
docker-build:
    docker build -t jackplowman/project-status-checker:latest .

# Run the Docker image
docker-run:
    docker run \
        --env INPUT_CONFIG_FILE_PATH="examples/full_example.json" \
        --env INPUT_DATABASE_FILE_PATH="status-checker-database.sqlite" \
        --volume "$(pwd)/github/workspace/examples:/examples" \
        --rm jackplowman/project-status-checker:latest

# ------------------------------------------------------------------------------
# Ruff - Python Linting and Formatting
# Set up ruff red-knot when it's ready
# ------------------------------------------------------------------------------

# Fix all Ruff issues
ruff-fix:
    just ruff-format-fix
    just ruff-lint-fix

# Check for Ruff issues
ruff-lint:
    poetry run ruff check .

# Fix Ruff lint issues
ruff-lint-fix:
    poetry run ruff check . --fix

# Check for Ruff format issues
ruff-format:
    poetry run ruff format --check .

# Fix Ruff format issues
ruff-format-fix:
    poetry run ruff format .

# ------------------------------------------------------------------------------
# Prettier
# ------------------------------------------------------------------------------

prettier-check:
    prettier . --check

prettier-format:
    prettier . --check --write

# ------------------------------------------------------------------------------
# Justfile
# ------------------------------------------------------------------------------

format:
    just --fmt --unstable

format-check:
    just --fmt --check --unstable

# ------------------------------------------------------------------------------
# Git Hooks
# ------------------------------------------------------------------------------

# Install pre commit hook to run on all commits
install-git-hooks:
    cp -f githooks/pre-commit .git/hooks/pre-commit
    cp -f githooks/post-commit .git/hooks/post-commit
    chmod ug+x .git/hooks/*
