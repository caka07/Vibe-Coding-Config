# ccswitch

Use `settings.json.template` as the portable preference template.

Use `providers.template.json` as a redacted reference when recreating providers
on a new machine. It is not meant to be copied over `cc-switch.db`.

Do not migrate:

- `copilot_auth.json`
- `codex_oauth_auth.json`
- `cc-switch.db`
- `backups/*.db`
- `logs/`

Provider IDs and OAuth files are machine/account-specific. Recreate providers on
the new machine, then replace `<PROVIDER_ID>`.
