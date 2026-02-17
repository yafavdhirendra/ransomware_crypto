from tkinter import messagebox
from crypto_utils import get_fernet

def decrypt_files(password, files):
    if not password:
        messagebox.showerror("Error", "Password required")
        return

    fernet = get_fernet(password)

    for file in files:
        try:
            with open(file, "rb") as f:
                data = f.read()

            if not data.endswith(b"# ENCRYPTED"):
                continue

            data = data[:-11]
            decrypted = fernet.decrypt(data)

            with open(file, "wb") as f:
                f.write(decrypted)

        except Exception as e:
            messagebox.showerror("Error", f"Failed: {file}\n{e}")
            return

    messagebox.showinfo("Success", "Decryption completed")
