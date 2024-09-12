## Contributing

### Requirements

- Python 3.910+
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
docker run --rm -v $(pwd):/app -w /app --name cz-kpn kpnnl/cz-kpn:3.2.10 'cz ls'
```

### Testing

```bash
pytest tests
```
