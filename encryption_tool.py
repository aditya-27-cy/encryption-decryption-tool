import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# ── Caesar Cipher ──────────────────────────────────────────
def caesar_encrypt(text: str, shift: int) -> str:
    """Shift each letter by the shift value."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt by shifting in reverse."""
    return caesar_encrypt(text, -shift)

# ── Vigenere Cipher ────────────────────────────────────────
def vigenere_encrypt(text: str, key: str) -> str:
    """Encrypt using a repeating keyword."""
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text: str, key: str) -> str:
    """Decrypt by reversing the keyword shifts."""
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# ── AES-256 Encryption ─────────────────────────────────────
def aes_encrypt(text: str, key: str) -> str:
    """
    Encrypt text using AES-256 in CBC mode.
    Key is padded/truncated to 32 bytes.
    Returns base64 encoded ciphertext.
    """
    key_bytes = key.encode().ljust(32)[:32]
    iv = os.urandom(16)

    padder = padding.PKCS7(128).padder()
    padded = padder.update(text.encode()) + padder.finalize()

    cipher = Cipher(
        algorithms.AES(key_bytes),
        modes.CBC(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()

    result = base64.b64encode(iv + ciphertext).decode()
    return result

def aes_decrypt(encrypted_text: str, key: str) -> str:
    """Decrypt AES-256 encrypted text."""
    try:
        key_bytes = key.encode().ljust(32)[:32]
        data = base64.b64decode(encrypted_text)
        iv = data[:16]
        ciphertext = data[16:]

        cipher = Cipher(
            algorithms.AES(key_bytes),
            modes.CBC(iv),
            backend=default_backend()
        )
        decryptor = cipher.decryptor()
        padded = decryptor.update(ciphertext) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        result = unpadder.update(padded) + unpadder.finalize()
        return result.decode()
    except Exception:
        return "Decryption failed — wrong key or corrupted data."

# ── Menu ───────────────────────────────────────────────────
def show_menu():
    print("\n" + "="*45)
    print("       Encryption & Decryption Tool")
    print("="*45)
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. AES-256 Encryption")
    print("4. Exit")
    print("="*45)

def caesar_menu():
    print("\n-- Caesar Cipher --")
    text = input("Enter text: ")
    shift = int(input("Enter shift value (e.g. 3): "))
    choice = input("Encrypt or Decrypt? (e/d): ").lower()

    if choice == 'e':
        result = caesar_encrypt(text, shift)
        print(f"\n[+] Encrypted: {result}")
    elif choice == 'd':
        result = caesar_decrypt(text, shift)
        print(f"\n[+] Decrypted: {result}")
    else:
        print("Invalid choice.")

def vigenere_menu():
    print("\n-- Vigenere Cipher --")
    text = input("Enter text: ")
    key = input("Enter key (letters only, e.g. SECRET): ")
    choice = input("Encrypt or Decrypt? (e/d): ").lower()

    if choice == 'e':
        result = vigenere_encrypt(text, key)
        print(f"\n[+] Encrypted: {result}")
    elif choice == 'd':
        result = vigenere_decrypt(text, key)
        print(f"\n[+] Decrypted: {result}")
    else:
        print("Invalid choice.")

def aes_menu():
    print("\n-- AES-256 Encryption --")
    text = input("Enter text: ")
    key = input("Enter secret key: ")
    choice = input("Encrypt or Decrypt? (e/d): ").lower()

    if choice == 'e':
        result = aes_encrypt(text, key)
        print(f"\n[+] Encrypted (base64): {result}")
    elif choice == 'd':
        result = aes_decrypt(text, key)
        print(f"\n[+] Decrypted: {result}")
    else:
        print("Invalid choice.")

# ── Entry Point ────────────────────────────────────────────
if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select option (1-4): ").strip()

        if choice == '1':
            caesar_menu()
        elif choice == '2':
            vigenere_menu()
        elif choice == '3':
            aes_menu()
        elif choice == '4':
            print("\nExiting. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")