#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Config root: ${ROOT}"

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is not installed. Install it first from https://brew.sh/"
  exit 1
fi

brew bundle --file "${ROOT}/homebrew/Brewfile"

echo "Homebrew bootstrap finished."
echo "Next: resolve placeholders in shell and ai-tools templates before copying them into HOME."

