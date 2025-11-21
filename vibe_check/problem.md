# Vibe Check

- Namespace: 18739
- Type: custom
- Category: crypto
- Points: 100

## Description

The admin has created a "secure" vault that encrypts the flag every time you visit.
The encryption key is rotated every single second based on the server's internal clock.

Can you catch the vibe and decrypt the message?

## Details

Access the Vibe Check Vault here: {{link_as("website", "/", "Launch Challenge")}}

## Hints

- Python's `random` library is not secure.
- Any problem to the random seeds?
- XOR encryption is reversible.

## Tags

- cryptography

## Attributes

- Author: Shiyu Chen
- event: 18739-ctf