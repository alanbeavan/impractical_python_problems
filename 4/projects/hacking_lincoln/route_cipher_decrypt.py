#!/usr/bin/env python3.6
"""Solve a cipher.

From a user specified cypher text, grid arrangement and route key, print
the solved message that was used to generate the cipher.

This program requires some user input.
All the things that need changing are contained within the __init__ function
    of the Cipher class (lines 39-49).
The things that can be changed have comments pointing them out.

Some background:

Example below is for 4x4 matrix with key -1 2 -3 4.
   Note "0" is not allowed.
   Arrows show encryption route; for negative key values read UP.
    ___ ___ ___ ___
   | ^ | | | ^ | | | MESSAGE IS WRITTEN
   |_|_|_v_|_|_|_v_|
   | ^ | | | ^ | | | ACROSS EACH ROW
   |_|_|_v_|_|_|_v_|
   | ^ | | | ^ | | | IN THIS MANNER
   |_|_|_v_|_|_|_v_|
   | ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
   |_|_|_v_|_|_|_v_|
   START        END
   Required inputs - a text message, # of columns, # of rows, key string

Regarding the key - the sign of th number suggests which way the column has
been arranged in the cyphertext.
"""

class Cipher():
    """Object representing the key to solve the cipher."""

    def __init__(self):
        """Initialise cipher solving sensations."""
        ####################
        ##Start user input##
        ####################
        #replace self.cyphertext with your text to be solved
        self.cyphertext = "THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"
        self.nrows = 6 #Replace with the number of rows in the route
        self.ncols = 4 #Replace with the number of columns in the route
        self.key = "-1 2 -3 4" #Replace with the key
        ####################
        ###End user input###
        ####################

        self.cypherlist = self.cyphertext.split()
        self.keylist = list(map(int, self.key.split()))


    def create_translation_matrix(self):
        """Create the translation matrix for this cipher using nrows and ncols.

        The translation matrix is the order the columns of the matrix
        with each in the order it should be read according to the key.
        """
        matrix = [[]] * self.ncols
        collength = len(self.cypherlist) / self.ncols

        for i in self.keylist:
            to_add = []
            if i < 0:
                j = collength - 1
                while j >= 0:
                    #we take the +ve value of the col number and add numbers
                    #starting from the end of it to the beginning of it
                    to_add.append(self.cypherlist[int((abs(i) - 1)
                                                      * self.nrows + j)])
                    j -= 1
            else:
                j = 0
                while j < collength:
                    to_add.append(self.cypherlist[int((abs(i) - 1)
                                                      * self.nrows + j)])
                    j += 1
            matrix[int(abs(i))-1] = to_add

        return matrix

    def solved_string(self):
        """Print the correctly orderred list of words."""
        translation_matrix = self.create_translation_matrix()
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
        Check key is the same length as ncol and all values are valid.
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
        if len(self.keylist) != self.ncols:
            print("Your key is not the same length as the number of columns")
            exit()
        i = 1
        while i <= len(self.keylist):
            if int(abs(self.keylist[i-1])) != i:
                print("There is something wrong with the key. Remember, it" +
                      " has to be in the same order as the columns")
                exit()
            i += 1 

def main():
    """Do the things."""
    my_cipher = Cipher()
    my_cipher.validate_input()
    solved = my_cipher.solved_string()
    print(solved)

if __name__ == "__main__":
    main()
