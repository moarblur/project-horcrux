"""Basic utilities for creating and decrypting Horcrux payloads."""

from __future__ import annotations

import nacl.secret
import nacl.utils
import nacl.pwhash

# Size constants
_SALT_BYTES = nacl.pwhash.argon2i.SALTBYTES
_KEY_SIZE = nacl.secret.SecretBox.KEY_SIZE

_DEF_OPS = nacl.pwhash.argon2i.OPSLIMIT_MODERATE
_DEF_MEM = nacl.pwhash.argon2i.MEMLIMIT_MODERATE


def _derive_key(passphrase: str, salt: bytes) -> bytes:
    """Derive a symmetric key from ``passphrase`` and ``salt``."""
    return nacl.pwhash.argon2i.kdf(
        _KEY_SIZE,
        passphrase.encode("utf-8"),
        salt,
        opslimit=_DEF_OPS,
        memlimit=_DEF_MEM,
    )


def encrypt(data: bytes, passphrase: str) -> dict:
    """Encrypt ``data`` with ``passphrase``.

    Returns a payload containing the salt and ciphertext as hex strings.
    """
    salt = nacl.utils.random(_SALT_BYTES)
    key = _derive_key(passphrase, salt)
    box = nacl.secret.SecretBox(key)
    encrypted = box.encrypt(data)
    return {"salt": salt.hex(), "ciphertext": encrypted.hex()}


def decrypt(payload: dict, passphrase: str) -> bytes:
    """Decrypt a payload produced by :func:`encrypt`."""
    salt = bytes.fromhex(payload["salt"])
    key = _derive_key(passphrase, salt)
    box = nacl.secret.SecretBox(key)
    encrypted = bytes.fromhex(payload["ciphertext"])
    return box.decrypt(encrypted)
