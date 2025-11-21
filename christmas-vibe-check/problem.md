# Christmas Vibe Check

- Namespace: 18739
- Type: custom
- Category: crypto
- Points: 100

## Description

Santa's elves have built a secure system to collect Christmas wishes.
Make a wish, and the system will encrypt it along with a special flag using a key rotated every second based on the server's clock.

Can you feel the Christmas vibe and decrypt the message?

You can download the source code here: {{url_for("main.py", "Source Code")}}

## Details

Access the Christmas Vault here: {{link_as("website", "/", "Make a Wish")}}

## Hints

- Python's `random` library is not secure.
- XOR encryption is reversible.
- Nobody looks at the URL right?

## Tags

- cryptography

## Attributes

- Author: Shiyu Chen
- event: 18739-ctf