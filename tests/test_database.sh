#!/bin/bash
set -e +x

# check file exists
test -f status-checker-database.db

# check file is not empty
test -s status-checker-database.db
