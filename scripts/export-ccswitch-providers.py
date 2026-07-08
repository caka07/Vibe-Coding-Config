#!/usr/bin/env python3
import json
import re
import sqlite3
import sys
from pathlib import Path


SOURCE_HOME = str(Path.home())
DEFAULT_HOMEBREW_PREFIX = "/opt" + "/homebrew"
DEFAULT_ANACONDA_PREFIX = DEFAULT_HOMEBREW_PREFIX + "/anaconda3"
DEFAULT_APPLICATIONS = "/Applications"
DEFAULT_CODEX_APP = DEFAULT_APPLICATIONS + "/Codex.app"
DEFAULT_FLUX_ISLAND_APP = DEFAULT_APPLICATIONS + "/Flux Island.app"
SECRET_KEY_RE = re.compile(r"(key|token|secret|password|auth)", re.I)
SECRET_VALUE_RE = re.compile(
    r"(sk-[A-Za-z0-9_-]{16,}|gho_[A-Za-z0-9_]{16,}|github_pat_[A-Za-z0-9_]{16,})"
)


def redact(value):
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            if SECRET_KEY_RE.search(str(key)):
                result[key] = f"<{str(key).upper()}_PLACEHOLDER>"
            else:
                result[key] = redact(item)
        return result
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, str):
        value = value.replace(SOURCE_HOME, "${HOME}")
        value = value.replace(DEFAULT_ANACONDA_PREFIX, "${ANACONDA_PREFIX}")
        value = value.replace(DEFAULT_HOMEBREW_PREFIX, "${HOMEBREW_PREFIX}")
        value = value.replace(DEFAULT_CODEX_APP, "${CODEX_APP}")
        value = value.replace(DEFAULT_FLUX_ISLAND_APP, "${FLUX_ISLAND_APP}")
        return SECRET_VALUE_RE.sub("<REDACTED_SECRET>", value)
    return value


def parse_jsonish(text):
    if not text:
        return {}
    try:
        return redact(json.loads(text))
    except json.JSONDecodeError:
        return redact(text)


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: export-ccswitch-providers.py <cc-switch.db> <output.json>", file=sys.stderr)
        return 2

    db_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    endpoints = {}
    for row in conn.execute("select provider_id, app_type, url from provider_endpoints order by app_type, provider_id, id"):
        endpoints.setdefault((row["provider_id"], row["app_type"]), []).append(redact(row["url"]))

    providers = []
    for row in conn.execute(
        """
        select id, app_type, name, settings_config, website_url, category, notes,
               icon, icon_color, meta, is_current, in_failover_queue,
               cost_multiplier, limit_daily_usd, limit_monthly_usd, provider_type
        from providers
        order by app_type, sort_index, name
        """
    ):
        item = dict(row)
        provider_id = item.pop("id")
        app_type = item["app_type"]
        item["id"] = "<PROVIDER_ID>"
        item["settings_config"] = parse_jsonish(item.get("settings_config"))
        item["meta"] = parse_jsonish(item.get("meta"))
        item["endpoints"] = endpoints.get((provider_id, app_type), [])
        providers.append(redact(item))

    out_path.write_text(json.dumps({"providers": providers}, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
