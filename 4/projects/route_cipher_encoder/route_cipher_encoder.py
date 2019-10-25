#!/usr/bin/env python3.6
"""Encrypt a message accoding to a route cipher.

We will require some modification of this program by the user.
The bits that need modifying are clearly marked below.
There are also some codewords.
"""
import my_module as mod

class Message():
    """Class to deal with the ciphering of a message."""
    def __init__(self):
        """Initialise stuff."""
        ####################
        ##Begin user input##
        ####################
        self.plaintext = mod.get_file_data("message.txt")[0]
        self.key = "-1 3 -2 6 5 -4"
        self.nrow = 7
        self.ncol = 6
        self.codewords = self.read_codewords("codewords.txt")
        ####################
        ###End user input###
        ####################
        self.textlist = self.plaintext.split()
        self.keylist = list(map(int, self.key.split()))


    def read_codewords(self, filename):
        """Read the table of codewords for the encryption. Return as dict."""
        codes = {}
        for line in mod.get_file_data(filename):
            fields = line.split()
            codes[fields[0]] = fields[1]
        return codes

    def create_matrix(self):
        """Create the transition amtrix for traversal."""
        matrix = [[] for i in range(self.ncol)]
        tracker = 0
        while tracker < len(self.textlist):
            for j in range(self.ncol):
                matrix[j].append(self.textlist[tracker])
                tracker += 1
        return matrix

    def encrypt(self):
        """Encrypt message by traversing the matrix accordin to the key."""
        matrix = self.create_matrix()
        encrypted = []
        for i in self.keylist:
            if i < 0:
                for word in matrix[int(abs(i))-1][::-1]:
                    encrypted.append(word)
            else:
                for word in matrix[int(abs(i))-1]:
                    encrypted.append(word)
        return " ".join(encrypted)
        

def main():
    """Do the things"""
    my_message = Message()
    print(my_message.encrypt())

if __name__ == "__main__":
    main()
