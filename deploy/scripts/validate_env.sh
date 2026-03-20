#!/usr/bin/env bash
set -euo pipefail

required=(OPENAI_API_KEY ANTHROPIC_API_KEY)
missing=()

for var in "${required[@]}"; do
  if [ -z "${!var:-}" ]; then
    missing+=("$var")
  fi
done

if [ ${#missing[@]} -gt 0 ]; then
  echo "Missing required env vars: ${missing[*]}"
  exit 1
fi

echo "Required env vars are set."
