from tkinter import messagebox
from crypto_utils import get_fernet

MARKER = b"\n# ENCRYPTED"

def encrypt_files(password, files):
    if not password:
        messagebox.showerror("Error", "Password required")
        return

    if not files:
        messagebox.showerror("Error", "No file selected")
        return

    fernet = get_fernet(password, mode="encrypt")

    encrypted_count = 0
    skipped_count = 0

    for file in files:
        try:
            with open(file, "rb") as f:
                data = f.read()

            # Already encrypted check
            if data.endswith(MARKER):
                skipped_count += 1
                continue

            encrypted = fernet.encrypt(data)

            with open(file, "wb") as f:
                f.write(encrypted + MARKER)

            encrypted_count += 1

        except Exception as e:
            messagebox.showerror("Error", f"Failed: {file}\n{e}")
            return

    # Proper message handling
    if encrypted_count > 0:
        messagebox.showinfo(
            "Success",
            f"{encrypted_count} file(s) encrypted successfully."
        )

    if skipped_count > 0:
        messagebox.showwarning(
            "Skipped",
            f"That were already encrypted."
        )

