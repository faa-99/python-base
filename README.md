# Python Codebase

## Description
This repository is a code base for python for the purpose of development and code reuse.

### Local Dev Poetry

To prepare the environment using poetry and python3.10
``` bash
make env
```

## Development

### Pushing your changes

You developed an amazing feature or fixed a bug, and you need to push you changes to git.
To make sure we have a consistent way of writing the code, scripts for formatting are ready to be used.

Before pushing you changes, we need to have your code formatted, checked by mypy, tested, and documented.
That's exactly what this command does:

```bash
make prepare
```

### Adding new Dependencies

To avoid running around requirements.txt files and adding dependencies manually, we use Poetry to manage the dependencies.

To add a new library to poetry:
``` bash
poetry add <name_of_library>
```

To specify a constraint when adding a package:
``` bash
# Specific library version
poetry add pendulum@^2.0.5
# Minimum library version
poetry add "pendulum>=2.0.5"
# Always use the latest version (not recommended)
poetry add pendulum@latest 
```

In order to get the latest versions of the dependencies and to update the poetry.lock file
``` bash
poetry update
```

If you just want to update a few packages and not all, you can list them as such:
``` bash
poetry update requests toml
```
## Cleanup

To keep the virtualenv and clean everything else
``` bash
make clean
```

For a deep cleaning
``` bash
make clean-all
```
