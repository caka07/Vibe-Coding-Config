# iTerm2

`com.googlecode.iterm2.common.plist` is an XML export of the source iTerm2
preferences. Before importing on a new machine, inspect paths and AI settings.

Typical import options:

1. iTerm2 Preferences -> General -> Preferences -> Load preferences from a custom folder.
2. Or copy selected profile/color settings manually from the plist.

Shell integration can be reinstalled from iTerm2:

```sh
curl -L https://iterm2.com/shell_integration/zsh -o ~/.iterm2_shell_integration.zsh
```

