# Placeholder Rules

Use these placeholders in committed common config:

- `${HOME}` - new machine home directory.
- `${USER}` - new machine username.
- `${HOMEBREW_PREFIX}` - usually `${HOMEBREW_PREFIX}` on Apple Silicon.
- `${ANACONDA_PREFIX}` - usually `${HOMEBREW_PREFIX}/anaconda3`.
- `${CODEX_APP}` - usually `${CODEX_APP}`.
- `${FLUX_ISLAND_APP}` - usually `${FLUX_ISLAND_APP}`.
- `<WORKSPACE_ROOT>` - project root to trust on the new machine.
- `<ANTHROPIC_AUTH_TOKEN>` - Claude-compatible API key.
- `<OPENROUTER_API_KEY>` - OpenRouter or compatible API key.
- `<OPENAI_API_KEY>` - OpenAI API key.
- `<GITHUB_TOKEN>` - GitHub token, if using a token instead of browser auth.
- `<PROVIDER_ID>` - ccswitch provider id created on the new machine.

Hard-coded local paths such as `/Users/<old-user>/...` should not appear in this
repo. Replace them with placeholders and let the target machine resolve them.

