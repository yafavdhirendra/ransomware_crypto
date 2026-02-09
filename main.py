import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_utils import get_fernet
from file_utils import collect_files

selected_files = []

def select_file():
    selected_files.clear()
    listbox.delete(0, tk.END)
    file = filedialog.askopenfilename()
    if file:
        selected_files.append(file)
        listbox.insert(tk.END, file)

def select_folder():
    selected_files.clear()
    listbox.delete(0, tk.END)
    folder = filedialog.askdirectory()
    if not folder:
        return
    files = collect_files(folder)
    for f in files:
        selected_files.append(f)
        listbox.insert(tk.END, f)

def encrypt_files():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Password required")
        return

    fernet = get_fernet(password)
    for file in listbox.get(0, tk.END):
        with open(file, "rb") as f:
            data = f.read()
        if data.endswith(b"# ENCRYPTED"):
            continue
        encrypted = fernet.encrypt(data)
        with open(file, "wb") as f:
            f.write(encrypted + b"\n# ENCRYPTED")

    messagebox.showinfo("Success", "Encryption completed")

def decrypt_files():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Password required")
        return

    fernet = get_fernet(password)
    for file in listbox.get(0, tk.END):
        with open(file, "rb") as f:
            data = f.read()
        if not data.endswith(b"# ENCRYPTED"):
            continue
        data = data[:-11]
        decrypted = fernet.decrypt(data)
        with open(file, "wb") as f:
            f.write(decrypted)

    messagebox.showinfo("Success", "Decryption completed")

root = tk.Tk()
root.title("File Encryption Tool")

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Select File", command=select_file).pack()
tk.Button(root, text="Select Folder", command=select_folder).pack()

listbox = tk.Listbox(root, width=80, height=15)
listbox.pack()

tk.Button(root, text="Encrypt", command=encrypt_files).pack()
tk.Button(root, text="Decrypt", command=decrypt_files).pack()

root.mainloop()
