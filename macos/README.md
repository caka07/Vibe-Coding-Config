# macOS Notes

The portable macOS layer is intentionally small:

- shell aliases live in `shell/zshrc.template`;
- `codexfull` and `yolo` are aliases, not standalone apps;
- Homebrew packages are managed by `homebrew/Brewfile`;
- iTerm2 profile/preferences are under `terminal/iterm2/`;
- GitHub CLI auth should be redone on the new machine with `gh auth login`.

Do not copy Keychain, browser cookies, or OAuth token files between machines.

