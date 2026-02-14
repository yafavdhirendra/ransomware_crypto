from gui import create_gui
from encryptor import encrypt_files
from decryptor import decrypt_files
from file_selector import select_file, select_folder

selected_files = []

def handle_select_file(listbox):
    select_file(listbox, selected_files)

def handle_select_folder(listbox):
    select_folder(listbox, selected_files)

def handle_encrypt(password, listbox):
    encrypt_files(password, selected_files)

def handle_decrypt(password, listbox):
    decrypt_files(password, selected_files)

root = create_gui(
    handle_select_file,
    handle_select_folder,
    handle_encrypt,
    handle_decrypt
)

root.mainloop()

