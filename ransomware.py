# Crucial module imports
import os
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

#  skipped files and directories defining for encrption...
SKP_DIRS = {".git", "__pycache__", "venv", "boss"}
SKIP_FILES = {"salt.bin"}

selected_files = []

# derive key from password + salt
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