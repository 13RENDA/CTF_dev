from flask import Flask, render_template
import random
import time
import binascii

app = Flask(__name__)

def get_flag():
    try:
        # Read from the location we defined in setup-challenge.py
        with open("/challenge/flag", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "picoCTF{flag_not_found_contact_admin}"

@app.route('/')
def index():
    flag = get_flag()
    
    # Vulnerability: Time-based seeding
    timestamp = int(time.time())
    random.seed(timestamp)
    
    # Encrypt
    plaintext = flag.encode()
    ciphertext_bytes = bytearray()
    for byte in plaintext:
        key_byte = random.getrandbits(8)
        ciphertext_bytes.append(byte ^ key_byte)
    
    ciphertext_hex = binascii.hexlify(ciphertext_bytes).decode()
    
    return render_template('index.html', 
                           ciphertext=ciphertext_hex, 
                           timestamp=timestamp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)