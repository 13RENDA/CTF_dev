# Christmas Vibe Check

Crypto CTF challenge - decrypt the flag by exploiting Python's predictable random number generator.

## How It Works

1. Submit a wish on the web interface
2. Server encrypts your wish and the flag using XOR with random bytes
3. Random generator is seeded with the current timestamp
4. Encrypted wish and flag are displayed

## Principle

- Python's `random` module is deterministic when seeded with the same value
- The timestamp in the URL reveals the seed
- XOR encryption is reversible with the same key stream
- Since the RNG state is predictable, you can decrypt the flag

## Solver Usage

```bash
python solve.py
```

Input when prompted:
1. **Timestamp** - from the URL parameter (`?ts=...`)
2. **Encrypted Wish** - hex string from the result page
3. **Encrypted Flag** - hex string from the result page

The solver:
- Seeds the RNG with the timestamp
- Advances RNG state by decrypting the wish
- Decrypts the flag using the remaining RNG stream

