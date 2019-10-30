#!/usr/bin/env python3.6
"""Solve null cipher.

Load message from text file.
Get n from user.
Decrypt and inform user.
"""

import string
import my_module as mod

def decrypt_null(message, n):
    """Decrypt a null cipher, taking characters n after a punctuation mark."""
    solved = ""
    message = message.replace(" ", "")
    counter = n+1
    for char in message:
        if char in string.punctuation:
            counter = 0
        elif counter == n:
            solved += char
        counter += 1
    return solved

def main():
    """Do the things."""
    message = mod.get_file_data("message.txt")[0]
    n = int(input("gizzus n"))
    solved = decrypt_null(message, n)
    print(solved)

if __name__ == "__main__":
    main()
