# Encryption & Decryption Tool

A Python-based command-line tool that implements three encryption algorithms —
Caesar Cipher, Vigenère Cipher, and AES-256 — demonstrating both classical 
and modern cryptography concepts.

## Features
- Caesar Cipher — shifts each letter by a numeric key
- Vigenère Cipher — polyalphabetic encryption using a keyword
- AES-256 — industry standard encryption using CBC mode and PKCS7 padding
- Simple menu-driven CLI interface
- Encrypt and decrypt any text input

## Tech Used
- Python 3
- `cryptography` library (AES-256)
- `os` and `base64` modules (built-in)

## Requirements

Install the cryptography library:
   pip install cryptography

## How to Run

1. Clone the repository
   git clone https://github.com/aditya-27-cy/encryption-decryption-tool

2. Navigate to the folder
   cd encryption-decryption-tool

3. Run the script
   python encryption_tool.py

## Sample Output

=============================================
       Encryption & Decryption Tool
=============================================
1. Caesar Cipher
2. Vigenere Cipher
3. AES-256 Encryption
4. Exit
=============================================
Select option (1-4): 1

-- Caesar Cipher --
Enter text: Hello World
Enter shift value (e.g. 3): 3
Encrypt or Decrypt? (e/d): e

[+] Encrypted: Khoor Zruog

=============================================
Select option (1-4): 3

-- AES-256 Encryption --
Enter text: This is a secret message
Enter secret key: mypassword
Encrypt or Decrypt? (e/d): e

[+] Encrypted (base64): V2VsY29tZSB0byBzZWN1cml0eQ==

## Concepts Demonstrated
- Classical cryptography (Caesar, Vigenère)
- Symmetric key encryption (AES-256)
- CBC (Cipher Block Chaining) mode
- PKCS7 padding
- Base64 encoding of binary cipher output

## Ethical Note
This tool is built for educational purposes to demonstrate how encryption 
algorithms work. Do not use it to encrypt data for malicious purposes.

## Author
Aditya Ramesh Warrier — Dayananda Sagar University, B.Tech Cyber Security<img width="1017" height="753" alt="Screenshot (52)" src="https://github.com/user-attachments/assets/78f18170-c769-4642-890e-e63c53b7cb50" />
<img width="752" height="862" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/dc0b0d79-e9b8-4ba5-96bd-4eff40c30c4a" />
