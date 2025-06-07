# Project Horcrux

This repository houses early work on the Horcrux protocol and the EchoVault reference implementation.

## Horcrux Protocol

Horcruxes are encrypted records containing arbitrary data and minimal
metadata. Clients derive a symmetric key from a user-provided passphrase
and encrypt the payload locally so that only ciphertext and
non‑sensitive metadata are uploaded. This design enables
zero‑knowledge sharing while allowing optional features such as secure
links and access revocation. The full specification lives in
[`HORCRUX_SPEC.md`](docs/HORCRUX_SPEC.md).

## EchoVault Reference Implementation

EchoVault demonstrates how the protocol can operate as a web service.
The planned Flask backend stores encrypted payloads and metadata and
issues secure sharing links to recipients. A more detailed architectural
overview is provided in [`ECHOVAULT_OVERVIEW.md`](docs/ECHOVAULT_OVERVIEW.md).

## Directory Overview
* The `echovault/` directory contains the EchoVault application documentation and assets.
* The `horcrux/` directory provides basic encryption utilities for Horcrux payloads.
* The `docs/` directory will store protocol specifications and other project documentation, including the [`HORCRUX_SPEC.md`](docs/HORCRUX_SPEC.md) file and other docs such as [ECHOVAULT_OVERVIEW.md](docs/ECHOVAULT_OVERVIEW.md).
* The `ai/` directory contains AI and LLM related usage guidelines.

## Governance
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [License](LICENSE)

## Running Tests

```bash
pip install -r requirements.txt
pytest
```
