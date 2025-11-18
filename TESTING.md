# Testing the QR Vigenère Challenge

## Prerequisites

Install required dependencies:
```bash
pip install qrcode[pil] pillow
```

Optional (for QR code decoding in solver):
```bash
pip install pyzbar
```

## Testing Steps

### 1. Generate the Challenge

Test the challenge generation with a sample flag:

```bash
python3 qr_challenge.py "picoCTF{test_flag_12345}"
```

Or let it generate a random test flag:
```bash
python3 qr_challenge.py
```

This will create:
- `qr_encrypted.png` - The QR code with encrypted flag
- `encrypted.txt` - The base64 encoded encrypted text
- `solution.txt` - The solution (for verification)

### 2. Test the Solver

#### Option A: From QR Code Image
```bash
python3 solver.py qr_encrypted.png
```

#### Option B: From Encrypted Text File
```bash
python3 solver.py encrypted.txt
```

#### Option C: From Base64 String Directly
```bash
python3 solver.py "YOUR_BASE64_STRING_HERE"
```

#### Option D: With Custom Key (if testing different keys)
```bash
python3 solver.py encrypted.txt "customkey"
```

### 3. Verify the Solution

Compare the output from the solver with `solution.txt`:
```bash
cat solution.txt
```

The flag should match!

### 4. Test with Setup Script (Full Integration)

To test the full setup process (simulating the CTF environment):

```bash
export FLAG="test12345"
python3 setup-challenge.py
```

This will:
- Read flag from environment variable
- Format it as `picoCTF{enjoy_winter_break_test12345}`
- Generate QR code in `cmgr/artifacts/`
- Create metadata.json

Then test solving:
```bash
python3 solver.py cmgr/artifacts/encrypted.txt
```

## Expected Output

### Challenge Generation:
```
======================================================================
QR Code + Vigenère Cipher Challenge Generator
======================================================================

[*] Original flag: picoCTF{enjoy_winter_break_test12345}
[*] Vigenère key: christmas
[*] After Vigenère: [encrypted text]
[*] After Base64: [base64 string]

[*] Generating QR code...

[+] QR code saved to qr_encrypted.png
[+] Solution saved to 'solution.txt'
[+] Encrypted text saved to 'encrypted.txt'
```

### Solver:
```
======================================================================
QR Code + Vigenère Cipher Challenge Solver
======================================================================

[*] Reading encrypted data from: encrypted.txt
[*] Base64 encoded data: [base64 string]
[*] After Base64 decode: [vigenere encrypted]
[*] Decrypting with Vigenère key: christmas
[*] Decrypted flag: picoCTF{enjoy_winter_break_test12345}

======================================================================
SOLUTION FOUND!
======================================================================
Flag: picoCTF{enjoy_winter_break_test12345}
======================================================================
```

## Troubleshooting

1. **QR code can't be decoded**: Install pyzbar or use `encrypted.txt` directly
2. **Import errors**: Make sure `qr_challenge.py` is in the same directory
3. **Wrong decryption**: Verify the key matches (should be "christmas")

## Manual Testing Checklist

- [ ] Challenge generates QR code successfully
- [ ] QR code contains valid base64 string
- [ ] Base64 decodes to Vigenère encrypted text
- [ ] Solver correctly decrypts with key "christmas"
- [ ] Final flag matches original flag format
- [ ] Setup script works with FLAG environment variable

