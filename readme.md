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

<hr>
<br>## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI
* **cryptography** library

  * `Fernet` (AES-based symmetric encryption)
  * `Scrypt` (password-based key derivation)</br></hr>
---

## 📦 Requirements

Install dependencies using:

```bash
pip install cryptography
```

Tkinter comes pre-installed with most Python distributions.

---<br>
<hr>
<br>
## 🚀 How It Works (High-Level)

1. User selects a **file or folder**
2. User enters a **password**
3. A **salt** is generated (or reused)
4. Password + salt → **secure key** (via Scrypt)
5. Files are encrypted/decrypted using **Fernet**
6. A marker `# ENCRYPTED` prevents double encryption

---</br>
<hr><b>AUTHOR:- Dhirendra Yadav<br>1st sem Project..</br> </b>