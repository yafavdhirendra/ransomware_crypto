# Ransomware Tool Using Python

A Python GUI application that allows you to **encrypt and decrypt files or entire folders** using a **password-derived key**. Built with **Tkinter** for the interface and **cryptography (Fernet + Scrypt)** for strong encryption.
This project is ideal for learning **practical cryptography, secure file handling, and GUI development**, especially for **cybersecurity students**.

## Features
- **Password-based encryption** (no hardcoded secret key)
- Encrypt / decrypt **single files**
- Encrypt / decrypt **all files inside a folder (recursive)**
- Skips system & unwanted directories (`.git`, `__pycache__`, `venv`, etc.)
- **Prevents double encryption** using a marker
- Safe decryption only if the correct password is provided
- Uses **salt + Scrypt KDF** to derive a secure key
- Clean and interactive **Tkinter GUI**

## Technologies Used

- **Python 3**
- **Tkinter** – GUI
- **cryptography** library
  * `Fernet` (AES-based symmetric encryption)
  * `Scrypt` (password-based key derivation)</br></hr>

## Quick Start 
```bash 
# Clone the repository
git clone https://github.com/yafavdhirendra/ransomware_adv.git
cd ransomeware_adv

# run the main file
python3 ransomware.py
```

**Expected Output**
[ADD YOUR APPLICATION HOMEPAGE SCREENSHORT HERE]

## Project Structure
```
├── ransomware.py
├── readme.md
```

## Requirements

Install dependencies using:

```bash
pip install cryptography
```
Tkinter comes pre-installed with most Python distributions.

## How It Works (High-Level)

- User selects a **file or folder**
- User enters a **password**
- A **salt** is generated (or reused)
- Password + salt → **secure key** (via Scrypt)
- Files are encrypted/decrypted using **Fernet**
- A marker `# ENCRYPTED` prevents double encryption


## License
This project is licensed under MIT License. See more about [License](/LICENSE).

## Author
- Dhirendra Yadav - First Year Student
- Softwarica College of IT and E-Commerce