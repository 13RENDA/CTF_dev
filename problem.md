# QR Vigenere Hunt

- Namespace: 18739
- Type: custom
- Category: crypto
- Points: 100

## Description

I found a mysterious QR code that contains an encrypted flag. Can you decode it and find the secret message?

Download the QR code from the challenge artifacts.


## Details

Scan the QR code to get the encrypted message. Decode it using Base64, then decrypt using the Vigenère cipher with the key hint provided.

## Hints
- The message is encrypted with Vigenère cipher, then Base64 encoded
- Have you heard of Vigenère? The key is a common holiday word (9 letters, starts with 'c') 🎄🎅

## Tags

- base64
- Vigenere

## Attributes

- Organization: ACI
- event: 18739-ctf # The name of the CTF event