#!/usr/bin/env python3.6
"""Create a vocabulary list which can be decrypted with a null cipher."""

import random
import load_dictionary

def list_cipher(message, n):
    """Create a vocabulary list.
    
    The nth char in each word reads the message.
    """
    dictionary = load_dictionary.load("dictionary.txt")
    random.shuffle(dictionary)
    message = "".join(message.split()).lower()
    vocab = []
    for letter in message:
        for word in dictionary:
            if len(word) > 6:
                if word[n] == letter and word not in vocab:
                    vocab.append(word)
                    break
    return vocab

def main():
    """Do the things."""
    plaintext = "Panel at east end of chapel slides"
    n = 3
    vocabulary = list_cipher(plaintext, n)
    if len(vocabulary) != len("".join(plaintext.split())):
        print("The dictionary doesn't have enough words or some shit.")
    else:
        print("\n".join(vocabulary))

if __name__ == "__main__":
    main()
