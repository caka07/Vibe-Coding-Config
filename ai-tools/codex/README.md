# Codex

Use these as templates for `${HOME}/.codex/`:

- `config.toml.template` -> `${HOME}/.codex/config.toml`
- `hooks.json.template` -> `${HOME}/.codex/hooks.json`
- `default.rules.template` -> `${HOME}/.codex/rules/default.rules`

Do not migrate:

- `auth.json`
- `sessions/`
- `history.jsonl`
- `sqlite/`
- `cache/`
- `plugins/cache/`
- `logs_*.sqlite`

Reinstall plugins through Codex on the new machine instead of copying plugin
caches.

