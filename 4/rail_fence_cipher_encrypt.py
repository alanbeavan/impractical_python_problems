#!/usr/bin/env python3.6
"""Encrypt a message according to the rail fence cipher.

This program requires user input. Please see the marked lines in the Cipher
    class. Comments mark where user input is required.

Background and algorithm (from Vaughan 2019):
Example text to encrypt:  'Buy more Maine potatoes'
Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S
Read zigzag:       \/\/\/\/\/\/\/\/\/\/
Encrypted:  BYOEA NPTTE UMRMI EOSOS.
"""

class Cipher():
    """Class containing the text to be ciphered and methods to cipher it."""
    def __init__(self):
        """Initialise text."""
        ####################
        ##Begin user input##
        ####################
        self.plaintext = "Buy more Maine potatoes"

    def encrypt(self):
        """Encrypt message.

        1. Collapse to string of upper case letters.
        2. Scramble letters according to 2 rail fences.
        3. Pointlessly insert spaces so the message is in 4 parts.
        """
        collapsed = "".join(self.plaintext.split()).upper()
        first = ""
        second = ""
        i = 0
        while i < len(collapsed):
            first += collapsed[i]
            if i <= len(collapsed):
                second += collapsed[i+1]
            i += 2

        scrambled = list(first + second)
        quarter = len(scrambled) / 4
        boundaries = [0]
        i = 1
        encrypted = []
        while i < 5:
            boundaries.append(round(quarter * i))
            encrypted.append("".join(scrambled[boundaries[i-1]:boundaries[i]]))
            i += 1
        return " ".join(encrypted)

def main():
    """Perform the functions in a satisfactory order."""
    my_cipher = Cipher()
    print(my_cipher.encrypt())

if __name__ == "__main__":
    main()
