#!/usr/bin/env python3.6
"""Encrypt a message according to the rail fence cipher with 3 rows.

This program requires user input. Please see the marked lines in the Cipher
    class. Comments mark where user input is required.

Background and algorithm (from Vaughan 2019):
Example text to encrypt:  'Buy more Maine potatoes'

Rail fence style B   O   A   P   T
                  U M R M I E O A O S
                   Y   E   N   T   E
Read Zigzag:     \\//\\//\\//\\//\\/

Encrypted:  BOAPT UMRMI EOAOS YENTE

Cycle = nrow * 2 - 2
"""

class Cipher():
    """Class containing the text to be ciphered and methods to cipher it."""
    def __init__(self):
        """Initialise text."""
        ####################
        ##Begin user input##
        ####################
        self.plaintext = "Buy more Maine potatoes"
        self.nrails = 8
        #####################
        ###End user inuput###
        #####################

    def encrypt(self):
        """Encrypt message.

        1. Collapse to string of upper case letters.
        2. Scramble letters according to n rail fences.
        3. Pointlessly insert spaces so the message is in 4 parts.
        """
        collapsed = "".join(self.plaintext.split()).upper()
        strings = [ "" for abitrary in range(self.nrails)]

        i = 0
        row = 0
        move = 1
        while i < len(collapsed):
            if row == 0:
                move = 1
            elif row == self.nrails - 1:
                move = -1
            strings[row] = strings[row] + collapsed[i]
            row += move
            i += 1
        scrambled = list("".join(strings))
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
