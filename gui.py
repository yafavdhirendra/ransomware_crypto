import tkinter as tk

def create_gui(select_file, select_folder, encrypt, decrypt):
    root = tk.Tk()
    root.title("File Encryption Tool")
    root.geometry("700x500")   # Bigger window
    root.resizable(False, False)

    # Password
    tk.Label(root, text="Password:", font=("Arial", 11)).pack(pady=5)
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack(pady=5)

    # Select Buttons Frame
    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    tk.Button(top_frame, text="Select File",
              width=20,
              command=lambda: select_file(listbox)).grid(row=0, column=0, padx=10)

    tk.Button(top_frame, text="Select Folder",
              width=20,
              command=lambda: select_folder(listbox)).grid(row=0, column=1, padx=10)

    # Listbox
    listbox = tk.Listbox(root, width=90, height=15)
    listbox.pack(pady=10)

    # Encrypt / Decrypt Frame (BOTTOM)
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(pady=15)

    tk.Button(bottom_frame, text="Encrypt",
              width=25,
              height=2,
              bg="#d9534f",
              fg="white",
              command=lambda: encrypt(password_entry.get(), listbox)
              ).grid(row=0, column=0, padx=20)

    tk.Button(bottom_frame, text="Decrypt",
              width=25,
              height=2,
              bg="#5cb85c",
              fg="white",
              command=lambda: decrypt(password_entry.get(), listbox)
              ).grid(row=0, column=1, padx=20)

    return root

