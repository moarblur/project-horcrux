import os
import sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from horcrux import encrypt, decrypt


def test_roundtrip():
    secret = b"classified data"
    payload = encrypt(secret, "password")
    recovered = decrypt(payload, "password")
    assert recovered == secret
