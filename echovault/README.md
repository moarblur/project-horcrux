# EchoVault Overview

EchoVault is a reference application demonstrating how the Horcrux protocol can be used to securely store and share encrypted payloads. The app remains in an early planning phase.

EchoVault is built around the Horcrux protocol. Each record created in the app is a Horcrux — an encrypted package that captures user data along with the metadata needed for revocation and access control. The repository shows how Horcrux concepts can be tied into a real application workflow.

For full architecture notes and the historical project document, see [../docs/ECHOVAULT_OVERVIEW.md](../docs/ECHOVAULT_OVERVIEW.md).

## Running EchoVault

Implementation of the user interface and backend is still in progress. When the
application is ready, you will be able to install the dependencies and launch
the app with commands similar to:

```bash
pip install -r requirements.txt
python -m echovault
```

This section will be updated with precise steps once the initial release lands.

## Governance
- [Code of Conduct](../CODE_OF_CONDUCT.md)
- [Security Policy](../SECURITY.md)
