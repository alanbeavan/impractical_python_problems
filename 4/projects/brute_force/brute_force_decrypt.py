#!/usr/bin/env python3.6
"""Solve a cipher.

From a user specified cypher text, print all possible decrypted strings.
This involves looping through the possible keys

The user must specify the cypher text, nrows and ncols vvvv
"""
from all_possible_keys import key_permutations

class Cipher():
    """Object representing the key to solve the cipher."""

    def __init__(self):
        """Initialise cipher solving sensations."""
        ####################
        ##Start user input##
        ####################
        #replace self.cyphertext with your text to be solved
#        self.cyphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
        self.cyphertext = "'Argh!', grufallo, the it 'Just one to hamster thoughtfully screamed the eating to me.' cornetto. Give Said the chocolate. eagle."
        self.nrows = 5 #Replace with the number of rows in the route
        self.ncols = 4 #Replace with the number of columns in the route
        ####################
        ###End user input###
        ####################

        self.cypherlist = self.cyphertext.split()


    def create_translation_matrix(self, key):
        """Create the translation matrix for this cipher using nrows and ncols.

        The translation matrix is the order the columns of the matrix
        with each in the order it should be read according to the key.
        """
        matrix = [[]] * self.ncols
        collength = len(self.cypherlist) / self.ncols
        
        tracker = 0
        for i in key:
            to_add = []
            if i < 0:
                j = collength - 1
                while j >= 0:
                    to_add.append(self.cypherlist[int((abs(i) - 1)
                                                      * self.nrows + j)])
                    j -= 1
            else:
                j = 0
                while j < collength:
                    to_add.append(self.cypherlist[int((abs(i) - 1)
                                                      * self.nrows + j)])
                    j += 1
            matrix[tracker] = to_add
            tracker += 1
        return matrix

    def solved_string(self, key):
        """Print the correctly orderred list of words."""
        translation_matrix = self.create_translation_matrix(key)
        plaintext = []
        for i in range(self.nrows):
            for j in range(self.ncols):
                plaintext.append(translation_matrix[j][i])
        plaintext = " ".join(plaintext)
        return plaintext

    def validate_input(self):
        """Ensure the user inputted settings that are possible.

        Check > 1 column.
        Check > 1 row.
        Check row * column = len ciphertext.
        """
        if self.nrows < 2:
            print("There must be greater than 1 row in the route matrix")
            exit()
        if self.ncols < 2:
            print("There must be greater than 1 column in the route matrix")
            exit()
        if self.ncols * self.nrows != len(self.cypherlist):
            print("The dimentions of your grid don't fit the length of your" +
                  " ciphertext exactly. Check your numbers")
            exit()



def main():
    """Do the things."""
    my_cipher = Cipher()
    keys = key_permutations(my_cipher.ncols)
    my_cipher.validate_input()
    for key in keys:
        solved = my_cipher.solved_string(key)
        print(solved)

if __name__ == "__main__":
    main()
