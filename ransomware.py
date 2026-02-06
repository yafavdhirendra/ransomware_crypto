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

# 📁 collect files (recursive)
def collect_files(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in SKP_DIRS]
        for f in files:
            if f.endswith(".py") or f in SKIP_FILES:
                continue
            file_list.append(os.path.join(root, f))  # full path
    return file_list

# 📄 select single file
def select_file():
    selected_files.clear()
    listbox.delete(0, tk.END)

    file = filedialog.askopenfilename()
    if file:
        selected_files.append(file)
        listbox.insert(tk.END, file)

# 📁 select folder
def select_folder():
    selected_files.clear()
    listbox.delete(0, tk.END)

    folder = filedialog.askdirectory()
    if not folder:
        return

    files = collect_files(folder)
    if not files:
        messagebox.showerror("Error", "No valid files found")
        return

    for f in files:
        selected_files.append(f)
        listbox.insert(tk.END, f)

# 🔒 encrypt selected files
def encrypt_files():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Password required")
        return

    chosen = listbox.curselection()
    if not chosen:
        messagebox.showerror("Error", "Select at least one file")
        return

    files = [listbox.get(i) for i in chosen]