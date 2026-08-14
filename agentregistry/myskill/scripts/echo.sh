#!/usr/bin/env bash
# Usage: ./echo.sh <message>

set -euo pipefail

if [[ $# -eq 0 ]]; then
  echo "Usage: echo.sh <message>" >&2
  exit 1
fi

echo "$@"
