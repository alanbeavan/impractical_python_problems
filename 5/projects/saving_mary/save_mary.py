#!/usr/bin/env python3.6
"""Encrypt a message using a null cipher as follows.

The message will be read from the nth character of each word where
n = 2,3,2,3,...
Except for:
    The first word
    The word "Stuart"
    The word "Jacob"
The words must be taken from a list of Mary's allies.
"""
import random
import my_module as mod

def encrypt(text, vocab, null_words):
    """Return an encrypted message."""
    text = "".join(text.split()).lower()
    null_locations = [int(len(text)/3), int(2*len(text)/3)]
    random.shuffle(vocab)
    cipher = [vocab[0]]
    match = 1
    change = 1
    for i in range(len(text)):
        if i in null_locations:
            cipher.append(null_words[null_locations.index(i)])
        for word in vocab:
            if word not in cipher:
                if word[match] == text[i]:
                    cipher.append(word)
                    match += change
                    change = -1 * change
                    break
    return cipher


def main():
    """Do the things."""
    names = mod.get_file_data("supporters.txt")
    codewords = ["Stuart", "Jacob"]
    message = "Give your word and we rise"
    cipher = encrypt(message, names, codewords)
    print(" ".join(cipher))

if __name__ == "__main__":
    main()
