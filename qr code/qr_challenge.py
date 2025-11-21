#!/usr/bin/env python3
"""
QR Code + Vigenère Cipher Challenge Generator
"""

import qrcode
import base64
import random
import string
from PIL import Image

def generate_random_flag():
    """Generate a random flag (for testing only)"""
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
    return f"Enjoy_{random_part}"

def vigenere_encrypt(plaintext, key):
    """
    Encrypt text using Vigenère cipher
    
    Args:
        plaintext: Text to encrypt
        key: Encryption key (e.g., "christmas")
    
    Returns:
        Encrypted text
    """
    result = []
    key = key.upper()
    key_index = 0
    
    for char in plaintext:
        if 'A' <= char <= 'Z':
            # Uppercase letter
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(encrypted_char)
            key_index += 1
        elif 'a' <= char <= 'z':
            # Lowercase letter
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(encrypted_char)
            key_index += 1
        else:
            # Non-alphabetic character (keep as is)
            result.append(char)
    
    return ''.join(result)

def vigenere_decrypt(ciphertext, key):
    """
    Decrypt text using Vigenère cipher
    
    Args:
        ciphertext: Text to decrypt
        key: Decryption key (e.g., "christmas")
    
    Returns:
        Decrypted text
    """
    result = []
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            # Uppercase letter
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            result.append(decrypted_char)
            key_index += 1
        elif 'a' <= char <= 'z':
            # Lowercase letter
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabetic character (keep as is)
            result.append(char)
    
    return ''.join(result)

def create_qr_code(data, filename, fill_color="black", back_color="white"):
    """
    Create a QR code image from data
    
    Args:
        data: String data to encode in QR code
        filename: Output filename for the QR code image
        fill_color: Color of QR code modules (default: "black")
        back_color: Background color (default: "white")
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    print(f"[+] QR code saved to {filename}")

def generate_qr_challenge(flag, output_dir="."):
    """
    Generate QR code challenge files
    
    Args:
        flag: The flag to encrypt and encode in QR code
        output_dir: Directory to save output files (default: current directory)
    
    Returns:
        Dictionary containing challenge information (flag, key, encrypted data, file paths)
    """
    import os
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*70)
    print("QR Code + Vigenère Cipher Challenge Generator")
    print("="*70)
    
    print(f"\n[*] Original flag: {flag}")
    
    # Vigenère encryption key
    key = "christmas"
    print(f"[*] Vigenère key: {key}")
    
    # Stage 1: Vigenère encryption
    vigenere_encrypted = vigenere_encrypt(flag, key)
    print(f"[*] After Vigenère: {vigenere_encrypted}")
    
    # Stage 2: Base64 encoding
    base64_encoded = base64.b64encode(vigenere_encrypted.encode()).decode()
    print(f"[*] After Base64: {base64_encoded}")
    
    # Create QR code
    print("\n[*] Generating QR code...\n")
    
    # QR Code: The encrypted flag
    qr_path = os.path.join(output_dir, "qr_encrypted.png")
    create_qr_code(base64_encoded, qr_path, 
                   fill_color="blue", back_color="white")
    
    # Save encrypted text for manual solving (this is what players get)
    encrypted_path = os.path.join(output_dir, "encrypted.txt")
    with open(encrypted_path, 'w') as f:
        f.write(base64_encoded)
    
    return {
        'flag': flag,
        'key': key,
        'vigenere_encrypted': vigenere_encrypted,
        'base64_encoded': base64_encoded,
        'qr_encrypted': qr_path,
        'encrypted_txt': encrypted_path
    }

def main():
    import sys
    
    # If flag provided as argument, use it; otherwise generate test flag
    if len(sys.argv) > 1:
        flag = sys.argv[1]
    else:
        flag = generate_random_flag()
    
    result = generate_qr_challenge(flag)
    
    # Save solution (only in main/test mode)
    with open('solution.txt', 'w') as f:
        f.write("="*70 + "\n")
        f.write("SOLUTION\n")
        f.write("="*70 + "\n")
        f.write(f"Original flag: {result['flag']}\n")
        f.write(f"Vigenère key: {result['key']}\n")
        f.write(f"After Vigenère: {result['vigenere_encrypted']}\n")
        f.write(f"After Base64: {result['base64_encoded']}\n")
        f.write("="*70 + "\n")
    
    print("\n[+] Solution saved to 'solution.txt'")
    print("[+] Encrypted text saved to 'encrypted.txt'")
    print("\n" + "="*70)
    print("Generated Files:")
    print(f"{result['qr_encrypted']}  - Main QR code (encrypted flag)")
    print(f"{result['encrypted_txt']}     - Raw encrypted text")
    print("solution.txt      - Complete solution")
    print("="*70)
    

if __name__ == "__main__":
    main()