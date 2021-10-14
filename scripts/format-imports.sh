#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort  --force-single-line-imports --apply app
sh ./scripts/format.sh