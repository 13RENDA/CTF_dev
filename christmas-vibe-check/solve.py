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
    random.seed(target_timestamp)

    #Processing wish to advance RNG state
    wish_bytes = binascii.unhexlify(wish_hex)
    
    for _ in wish_bytes:
        random.getrandbits(8) # Burn one random byte per wish byte

    # Decrypt the Flag
    flag_ciphertext = binascii.unhexlify(flag_hex)
    decrypted_chars = []

    for byte in flag_ciphertext:
        key_byte = random.getrandbits(8)
        plain_byte = byte ^ key_byte
        decrypted_chars.append(plain_byte)

    # Output
    flag = bytes(decrypted_chars).decode('utf-8', errors='ignore')
    print(f"\nThe Flag is: {flag}")

except ValueError:
    print("\nInvalid input. Ensure timestamp is an integer and hex strings are valid.")
except Exception as e:
    print(f"\nSomething went wrong: {e}")