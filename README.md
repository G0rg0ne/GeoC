## GeoC-Segmenter
## TODO :SUMMARY
This project uses "poetry" to manage and install dependencies. If your not familliar with this tool check out the following [documetation](https://python-poetry.org/docs/)

Poetry resolves all dependencies for you (in a multiplatform way) and creates a `poetry.lock` file with the found solution, which you can then share or just commit.

#### Adding dependencies

Run:

```bash
poetry add <package-name>
```

or manually edit [this file](./pyproject.toml), then run:

```bash
poetry lock
```

### Activate your work environment

To activate your poetry env, run:

```bash
poetry shell
```

