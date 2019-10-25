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

def decrypt(text):
    """Decrypt ciphertext.

    Split second half from first half (rounded up).
    Merge the two lists.
    I don't think it's possible to split the words without a dictionary.
    """
    boundary = math.ceil(len(text)/2)
    first = text[:boundary]
    second = text[boundary:]
    decrypted = ""
    for i in range(len(first)):
        decrypted += first[i]
        if i < len(second):
            decrypted += second[i]
    return decrypted
    

def main():
    """Perform funcitons in sensible order."""
    ciphertext = load_ciphertext()
    decrypted = decrypt(ciphertext)
    print(decrypted)

if __name__ == "__main__":
    main()
