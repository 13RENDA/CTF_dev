#!/usr/bin/env python3
"""
Solver for QR Code + Vigenère Cipher Challenge
"""

import base64
import sys
from qr_challenge import vigenere_decrypt

def decode_qr_from_file(qr_file):
    # Decode QR code from image file

    try:
        # Try using pyzbar (optional dependency)
        try:
            from pyzbar.pyzbar import decode as qr_decode
            from PIL import Image
            
            img = Image.open(qr_file)
            decoded_objects = qr_decode(img)
            if decoded_objects:
                return decoded_objects[0].data.decode('utf-8')
        except ImportError:
            print("pyzbar not installed. Install with: pip install pyzbar")
            print("Or provide the encrypted data directly from encrypted.txt")
            return None
    except Exception as e:
        print(f"Error decoding QR code: {e}")
        return None

def solve_challenge(encrypted_data, key="christmas"):
    # Solve the challenge by decrypting the encrypted data

    try:
        # Step 1: Decode Base64
        print(f"Base64 encoded data: {encrypted_data}")
        base64_decoded = base64.b64decode(encrypted_data).decode('utf-8')
        print(f"After Base64 decode: {base64_decoded}")
        
        # Step 2: Decrypt Vigenère
        print(f"Decrypting with Vigenère key: {key}")
        decrypted = vigenere_decrypt(base64_decoded, key)
        print(f"Decrypted flag: {decrypted}")
        
        return decrypted
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    print("QR Code + Vigenère Cipher Challenge Solver\n")

    # Try to get encrypted data from command line argument
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python solver.py 'encrypted_data'")
        print("  python solver.py qr_image.png")
        print("  python solver.py encrypted.txt")
        sys.exit(1)
    
    input_arg = sys.argv[1]
    encrypted_data = None
    
    # Check if it's a file
    import os
    if os.path.isfile(input_arg):
        # Check if it's an image file
        if input_arg.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print(f"Reading QR code from: {input_arg}")
            encrypted_data = decode_qr_from_file(input_arg)
            if not encrypted_data:
                print("Could not decode QR code.")
                print("Tip: You can scan the QR code manually or read from encrypted.txt")
                sys.exit(1)
        else:
            # Assume it's a text file
            print(f"Reading encrypted data from: {input_arg}")
            with open(input_arg, 'r') as f:
                encrypted_data = f.read().strip()
    else:
        # Assume it's the encrypted data directly
        encrypted_data = input_arg
    
    if not encrypted_data:
        print("Could not get encrypted data. Exiting.")
        sys.exit(1)
    
    # allow custom key
    key = sys.argv[2] if len(sys.argv) > 2 else "christmas"
    
    # Solve the challenge
    flag = solve_challenge(encrypted_data, key)
    
    if flag:
        print()
        print("="*70)
        print("SOLUTION FOUND!\n")
        print(f"Flag: {flag}")
        print("="*70)
        return flag
    else:
        print()
        print("Failed to solve challenge.")
        sys.exit(1)

if __name__ == "__main__":
    main()

