import random
import binascii

print("=== Christmas Vibe Check Solver ===")
print("Please enter the data found on the result page/URL.")

try:
    # 1. Input Data
    ts_input = input("Enter the Timestamp (from URL): ").strip()
    wish_hex = input("Enter the Encrypted Wish (Hex): ").strip()
    flag_hex = input("Enter the Encrypted Flag (Hex): ").strip()

    target_timestamp = int(ts_input)
    
    # 2. Replicate the Environment
    print(f"[*] Seeding local random generator with: {target_timestamp}")
    random.seed(target_timestamp)

    # 3. Advance the RNG (The Critical Fix)
    # The server used the RNG to encrypt the wish first. 
    # We must do the same to get the RNG to the state it was in when the flag was encrypted.
    
    print("[*] Processing wish to advance RNG state...")
    wish_bytes = binascii.unhexlify(wish_hex)
    
    # We don't actually care what the decrypted wish is, 
    # we just need to consume the random numbers.
    for _ in wish_bytes:
        random.getrandbits(8) # Burn one random byte per wish byte

    # 4. Decrypt the Flag
    # Now the RNG is in the exact state it was when the flag was encrypted.
    print("[*] Decrypting Flag...")
    
    flag_ciphertext = binascii.unhexlify(flag_hex)
    decrypted_chars = []

    for byte in flag_ciphertext:
        key_byte = random.getrandbits(8)
        plain_byte = byte ^ key_byte
        decrypted_chars.append(plain_byte)

    # 5. Output
    flag = bytes(decrypted_chars).decode('utf-8', errors='ignore')
    print(f"\n[SUCCESS] The Flag is: {flag}")

except ValueError:
    print("\n[ERROR] Invalid input. Ensure timestamp is an integer and hex strings are valid.")
except Exception as e:
    print(f"\n[ERROR] Something went wrong: {e}")