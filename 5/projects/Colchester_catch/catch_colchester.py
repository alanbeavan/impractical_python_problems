#!/usr/bin/env python3.6
"""Decrypt a message.

Take user input of n.
Take the nth letter of every nth word.
Tell user.
"""

import my_module as mod

def decrypt(text, n):
    """Do the decrypting."""
    message = ""
    words = text.split()
    i = 0
    while i < len(words):
        if (i+1) % n == 0:
            if len(words[i]) >= n:
                message = message + words[i][n-1]
            else:
                print("The message doesn't work with n.\nSo far the message" \
                      " reads {}".format(message))
                exit()
        i += 1
    return message

def main():
    """Do the things."""
    text = mod.get_file_data("message.txt")[0]
    n = int(input("gis n"))
    print(decrypt(text, n))

if __name__ == "__main__":
    main()
