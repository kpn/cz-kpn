# Multiple Python versions testing setup

## Local development with pyenv and tox
> **NOTE:** The instructions in this section are only relevant for local testing with tox. CI/CD and GitHub Actions use their own environment and configuration.

1. Install pyenv (if not already installed):
```bash
curl https://pyenv.run | bash
```

2. Install multiple Python versions:
```bash
pyenv install 3.10.12
pyenv install 3.11.10
pyenv install 3.12.7
pyenv install 3.13.0
```

3. Set local Python versions for this project:
```bash
pyenv local 3.10.12 3.11.10 3.12.7 3.13.0
```

4. Test with tox (tests all configured Python versions):
```bash
./scripts/test
```

## GitHub Actions
The project is tested on:
- Python versions: 3.10, 3.11, 3.12, 3.13
- Operating system: Ubuntu (macOS/Windows are disabled)

In the release workflow, Python 3.13 is used via a global environment variable:

```yaml
env:
	PYTHON_VERSION: '3.13'
```
and in setup-python:
```yaml
python-version: ${{ env.PYTHON_VERSION }}
```

## Tox configuration
Local testing can be done with:
```bash
poetry run tox -p auto
```
or with the test script:
```bash
./scripts/test
```
Both methods will test all Python versions in parallel.

Available environments:
- `py310`, `py311`, `py312`, `py313` - Test with specific Python version
- `coverage` - Run tests with coverage report
- `docs` - Build documentation (placeholder)