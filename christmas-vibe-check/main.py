from flask import Flask, render_template, request, redirect, url_for
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

def encrypt_data(data_str, rng_engine):
    """Helper function to encrypt string data using a specific RNG instance."""
    plaintext = data_str.encode()
    ciphertext_bytes = bytearray()
    for byte in plaintext:
        key_byte = rng_engine.getrandbits(8)
        ciphertext_bytes.append(byte ^ key_byte)
    return binascii.hexlify(ciphertext_bytes).decode()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        wish = request.form.get('wish', 'No wish provided')
        # Generate timestamp
        timestamp = int(time.time())
        # Redirect to the view route, putting timestamp in the URL
        return redirect(url_for('view_result', ts=timestamp, wish=wish))
        
    return render_template('index.html')

@app.route('/view')
def view_result():
    ts_str = request.args.get('ts')
    wish = request.args.get('wish', '')

    if not ts_str:
        return redirect(url_for('index'))

    try:
        timestamp = int(ts_str)
    except ValueError:
         return redirect(url_for('index'))
         
    flag = get_flag()
    
    # Seed a local RNG instance with the timestamp from the URL
    rng = random.Random(timestamp)
    
    # 1. Encrypt the wish first
    enc_wish = encrypt_data(wish, rng)
    
    # 2. Encrypt the flag immediately after, using the same RNG stream
    enc_flag = encrypt_data(flag, rng)
    
    # Render result template. Timestamp is in the URL, not passed to body.
    return render_template('result.html', 
                           enc_wish=enc_wish, 
                           enc_flag=enc_flag)

if __name__ == '__main__':
    # Listen on 0.0.0.0 to allow external access via container mapping
    app.run(host='0.0.0.0', port=8080)