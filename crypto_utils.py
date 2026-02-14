import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

SALT_FILE = "salt.bin"

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

def get_fernet(password, mode="encrypt"):
    if not os.path.exists(SALT_FILE):
        if mode == "encrypt":
            salt = os.urandom(16)
            with open(SALT_FILE, "wb") as f:
                f.write(salt)
        else:
            raise Exception("Salt file missing! Cannot decrypt.")
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()

    key = derive_key(password, salt)
    return Fernet(key)

