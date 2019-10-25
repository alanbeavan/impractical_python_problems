#!/usr/bin/env python3.6
"""Solve a cipher with hard-coded key and text."""

class Cipher():
    """Object representing the key to solve the cipher."""

    def __init__(self):
        """Initialise cipher solving sensations."""
        self.cyphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
        self.nrows = 5
        self.ncols = 4
        self.key = "-1 2 -3 4"
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

def main():
    """Do the things."""
    my_cipher = Cipher()
    solved = my_cipher.solved_string()
    print(solved)

if __name__ == "__main__":
    main()
