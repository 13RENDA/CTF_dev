import random
import binascii

print("=== Vibe Check Solver ===")
print("Please enter the data found on the challenge website.")

try:
    # 1. Input data
    # We treat inputs as strings first to strip whitespace
    ts_input = input("Enter the Timestamp: ").strip()
    hex_input = input("Enter the Ciphertext (Hex): ").strip()

    target_timestamp = int(ts_input)
    
    # 2. Replicate the environment
    print(f"[*] Seeding local random generator with: {target_timestamp}")
    random.seed(target_timestamp)

    # 3. Decrypt
    # Convert hex string back to raw bytes
    ciphertext = binascii.unhexlify(hex_input)
    decrypted_chars = []

    print("[*] Decrypting...")
    for byte in ciphertext:
        # Because the seed is the same, getrandbits(8) produces 
        # the EXACT same sequence as the server.
        key_byte = random.getrandbits(8)
        
        # Reverse the XOR: (Cipher ^ Key) = Plaintext
        plain_byte = byte ^ key_byte
        decrypted_chars.append(plain_byte)

    # 4. Output
    flag = bytes(decrypted_chars).decode('utf-8', errors='ignore')
    print(f"\n[SUCCESS] The Flag is: {flag}")

except ValueError:
    print("\n[ERROR] Invalid input. Please ensure Timestamp is a number and Ciphertext is valid Hex.")
except Exception as e:
    print(f"\n[ERROR] Something went wrong: {e}")