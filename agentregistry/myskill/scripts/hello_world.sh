#!/usr/bin/env bash
# Hello World Script - Template demonstrating script best practices
#
# Usage:
#   ./hello_world.sh --name "World"
#   ./hello_world.sh --name "World" --format json
#   ./hello_world.sh --name "World" --message "Welcome" --verbose

set -euo pipefail

NAME=""
MESSAGE="Hello"
FORMAT="text"
VERBOSE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)    NAME="$2";    shift 2 ;;
    --message) MESSAGE="$2"; shift 2 ;;
    --format)  FORMAT="$2";  shift 2 ;;
    --verbose) VERBOSE=true; shift   ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

if [[ -z "${NAME}" ]]; then
  echo "Error: --name is required" >&2
  exit 1
fi

GREETING="${MESSAGE}, ${NAME}!"
TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

case "${FORMAT}" in
  json)
    if ${VERBOSE}; then
      printf '{\n  "greeting": "%s",\n  "target": "%s",\n  "format": "json",\n  "timestamp": "%s"\n}\n' \
        "${GREETING}" "${NAME}" "${TIMESTAMP}"
    else
      printf '{\n  "greeting": "%s",\n  "target": "%s",\n  "format": "json"\n}\n' \
        "${GREETING}" "${NAME}"
    fi
    ;;
  xml)
    echo '<?xml version="1.0" encoding="UTF-8"?>'
    echo "<greeting>"
    echo "  <message>${GREETING}</message>"
    echo "  <target>${NAME}</target>"
    echo "  <format>xml</format>"
    ${VERBOSE} && echo "  <timestamp>${TIMESTAMP}</timestamp>"
    echo "</greeting>"
    ;;
  text|*)
    echo "${GREETING}"
    if ${VERBOSE}; then
      echo "Generated at: ${TIMESTAMP}"
      echo "Target: ${NAME}"
    fi
    ;;
esac
