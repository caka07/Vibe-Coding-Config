#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Scanning ${ROOT}"

patterns=(
  'sk-[A-Za-z0-9_-]{16,}'
  'gho_[A-Za-z0-9_]{16,}'
  'github_pat_[A-Za-z0-9_]{16,}'
  'xox[baprs]-[A-Za-z0-9-]{16,}'
  'AKIA[0-9A-Z]{16}'
  'AIza[0-9A-Za-z_-]{20,}'
  'api[_-]?key[[:space:]]*[:=][[:space:]]*["'\'']?[A-Za-z0-9_-]{16,}'
  'token[[:space:]]*[:=][[:space:]]*["'\'']?[A-Za-z0-9._-]{16,}'
  '/Users/[A-Za-z0-9._-]+'
)

failed=0
for pattern in "${patterns[@]}"; do
  if rg -n --hidden --glob '!.git/*' --glob '!scripts/check-secrets.sh' -e "${pattern}" "${ROOT}" >/tmp/config-secret-scan.$$; then
    echo "Potential secret/path match for pattern: ${pattern}"
    cat /tmp/config-secret-scan.$$
    failed=1
  fi
done

rm -f /tmp/config-secret-scan.$$

if [ "${failed}" -ne 0 ]; then
  echo "Secret scan failed."
  exit 1
fi

echo "Secret scan passed."
