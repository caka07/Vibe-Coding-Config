# Conda

Current source machine used Anaconda under `${ANACONDA_PREFIX}`.

Recommended migration:

```sh
conda env create -f ./conda/envs/trans.from-history.yml
```

Use `trans.full.yml` only when you need a closer package snapshot. The full file
is less portable across macOS/Python versions.

