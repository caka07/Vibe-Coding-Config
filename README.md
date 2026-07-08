# Vibe Coding Config

This is a sanitized, portable configuration bundle for a new macOS coding setup.

It is intentionally not a full machine backup. It keeps common preferences,
installation lists, shell aliases, and AI coding tool templates, while excluding
local history, sessions, caches, databases, OAuth files, and API keys.

## Layout

- `homebrew/` - Homebrew `Brewfile` and install notes.
- `conda/` - Conda config and environment exports.
- `shell/` - zsh/bash startup templates and CLI tool configs.
- `terminal/iterm2/` - iTerm2 preference export and notes.
- `ai-tools/codex/` - Codex common config templates.
- `ai-tools/claude/` - Claude Code common config templates.
- `ai-tools/claude-mem/` - Claude-mem common config template.
- `ai-tools/ccswitch/` - ccswitch common config template.
- `editor/zed/` - Zed settings.
- `cli/` - GitHub CLI non-secret config.
- `macos/` - macOS setup notes.
- `scripts/` - helper scripts for bootstrap and secret scanning.
- `docs/` - placeholder and migration notes.

## Migration Order

1. Install Homebrew.
2. Install packages from `homebrew/Brewfile`.
3. Install Anaconda or Miniforge, then recreate Conda envs from `conda/envs/`.
4. Copy shell templates into the new machine's home directory after resolving placeholders.
5. Install Claude Code, Codex, ccswitch, iTerm2, and Zed.
6. Resolve placeholders in `ai-tools/*/*.template` using the new machine's paths and API keys.
7. Run `scripts/check-secrets.sh` before committing or pushing.

Do not commit real `auth.json`, `hosts.yml`, `.env`, sqlite databases, history,
or session folders.

