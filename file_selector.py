import tkinter as tk
from tkinter import filedialog
from file_utils import collect_files

def select_file(listbox, selected_files):
    selected_files.clear()
    listbox.delete(0, tk.END)

    file = filedialog.askopenfilename()
    if file:
        selected_files.append(file)
        listbox.insert(tk.END, file)

def select_folder(listbox, selected_files):
    selected_files.clear()
    listbox.delete(0, tk.END)

    folder = filedialog.askdirectory()
    if not folder:
        return

    files = collect_files(folder)

    for f in files:
        selected_files.append(f)
        listbox.insert(tk.END, f)

