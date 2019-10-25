#!/usr/bin/env python3.6
"""Decrypt a message using the rail fence cipher.

Take user input.
Decrypt according to the rail fence cipher.

Background and algorithm (from Vaughan 2019):
Example text to encrypt:  'Buy more Maine potatoes'
Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S
Read zigzag:       \/\/\/\/\/\/\/\/\/\/
Encrypted:  BYOEA NPTTE UMRMI EOSOS.
"""
import math

def load_ciphertext():
    """Take user input, returning a list of the letters (no spaces)."""
    text = input("Enter your cipher text\n")
    return "".join(text.split(" "))

def decrypt(text, key):
    """Decrypt ciphertext.
    
    Cycle = nrow * 2 - 2
    """
    msg_len = len(text)
    cycle = key * 2 - 2
    n_cycles = math.floor(msg_len/cycle)
    extra = msg_len % cycle
    rows = [[] for arbitrary in range(key)]
    i = 0
    current = 0
    while i < key:
        rows[i] += text[:n_cycles]
        text = text[n_cycles:]
        if i > 0 and i < key-1:
            rows[i] += text[:n_cycles]
            text = text[n_cycles:]
            if extra > i:
                if cycle - extra < i:
                    rows[i] += text[:2]
                    text = text[2:]
                else:
                    rows[i] += text[0]
                    text = text[1:]
        elif extra > i:
            rows[i] += text[0]
            text = text[1:]
        i += 1
    
    i = 0
    row = 0
    move = 1
    solved = ""
    while i < msg_len:
        if row == 0:
            move = 1
        elif row == len(rows) - 1:
            move = -1
        solved += rows[row][0]
        rows[row] = rows[row][1:]
        row += move
        i += 1

    return solved


def main():
    """Perform funcitons in sensible order."""
    ciphertext = load_ciphertext()
    key = int(input("What is the key?"))
    decrypted = decrypt(ciphertext, key)
    print(decrypted)

if __name__ == "__main__":
    main()
