import os, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

def derive_key(password, salt):
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def get_fernet(password):
    if not os.path.exists("salt.bin"):
        salt = os.urandom(16)
        with open("salt.bin", "wb") as s:
            s.write(salt)
    else:
        with open("salt.bin", "rb") as s:
            salt = s.read()

    key = derive_key(password, salt)
    return Fernet(key)
