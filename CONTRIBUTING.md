## Contributing

### Requirements

- Python 3.10+
- Poetry 1.2+
- Git 1.8+

### Install dependencies

```bash
python -m venv .venv
. .venv/bin/activate
pip install -U pip poetry
poetry install
```

### Publishing

```bash
./scripts/bump  # bump version
./scripts/release  # to pypi
./scripts/build  # docker image
./scripts/release  # to pypi
```

### Running docker locally

```bash
docker run --rm -v $(pwd):/app -w /app --name cz-kpn kpnnl/cz-kpn:4.0.1 'cz ls'
```

### Testing

For local testing across all supported Python versions, use:

```bash
poetry run tox -p auto
```
or the test script:
```bash
./scripts/test
```
Both methods will run tests for all Python versions in parallel.

For single-version testing:
```bash
pytest tests
```

For details about supported Python versions and local testing instructions, see [PYTHON_TESTING.md](./PYTHON_TESTING.md).
