# Ransomware Tool Using Python
<br><hr>
A Python GUI application that allows you to **encrypt and decrypt files or entire folders** using a **password-derived key**. Built with **Tkinter** for the interface and **cryptography (Fernet + Scrypt)** for strong encryption.
<br><hr>
This project is ideal for learning **practical cryptography, secure file handling, and GUI development**, especially for **cybersecurity students**.-----
<hr><br>
## ✨ Features

* 🔑 **Password-based encryption** (no hardcoded secret key)
* 📄 Encrypt / decrypt **single files**
* 📁 Encrypt / decrypt **all files inside a folder (recursive)**
* 🚫 Skips system & unwanted directories (`.git`, `__pycache__`, `venv`, etc.)
* 🔁 **Prevents double encryption** using a marker
* 🔓 Safe decryption only if the correct password is provided
* 🧂 Uses **salt + Scrypt KDF** to derive a secure key
* 🖥️ Clean and interactive **Tkinter GUI**