# Project Horcrux

This repository houses early work on the Horcrux protocol and the EchoVault reference implementation.

* The `echovault/` directory contains the EchoVault application documentation and assets.
* The `horcrux/` directory provides basic encryption utilities for Horcrux payloads.
* The `docs/` directory will store protocol specifications and other project documentation, including the [`HORCRUX_SPEC.md`](docs/HORCRUX_SPEC.md) file and other docs such as [ECHOVAULT_OVERVIEW.md](docs/ECHOVAULT_OVERVIEW.md).
* The `ai/` directory contains AI and LLM related usage guidelines.

## Requirements

Install the project dependencies with:

```bash
pip install -r requirements.txt
```

The only required package currently is `pynacl`.

## Testing

After the requirements are installed, run the test suite using:

```bash
pytest -q
```
