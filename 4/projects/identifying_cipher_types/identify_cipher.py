#!/usr/bin/env python3.6
"""Identify the cipher used to generate some ciphertext.

The cipher can be be either letter substitution or letter transposition.
We will use the frequency of letters to guess which kind it is.
I'm think we used frequencies of letters before so I will look for it.
If it's letter transposition, we expect a similar frequency to english
If it's substitution, it would not necessarily have a similar distribution.
"""
import string
from collections import Counter
import my_module as mod

def read_frequency_table(filename):
    """Create a dictionary with the frequency of all letters in english."""
    freqs = {}
    lines = mod.get_file_data(filename)
    for line in lines:
        fields = line.split()
        freqs[fields[0]] = float(fields[1])
    return freqs

def letter_frequencies(text):
    """Return a dictionary of the frequencies of all letters in the text."""
    freqs = {}
    for letter in list(string.ascii_uppercase):
        freqs[letter] = 0
    for letter in text:
        freqs[letter] += 1
    for key in freqs:
        freqs[key] = freqs[key] / len(text)
    return freqs

def is_appropriately_similar(dictA, dictB, n_checks, threshold):
    """Determine if the 2 dictionaries are have similar compositions.
    
    How exactly to do this is a mystery. Here is my idea
    For the most common n_checks letters
    If more than threshold of them deviates from the frequency in English by
        more than 50%
    We will return 0
    Else return 1.
    """
    n_wrong = 0
    counts = Counter(dictA)
    highest = counts.most_common(n_checks)
    for key_val in highest:
        lower = key_val[1] - key_val[1] / 2
        upper = key_val[1] + key_val[1] / 2
        if lower > dictB[key_val[0]] or upper < dictB[key_val[0]]:
            n_wrong += 1
        if n_wrong > threshold:
            return 0
    return 1

def main():
    """Do the things."""
    lines = mod.get_file_data(input("Name of ciphertext file"))
    text = ""
    for line in lines:
        text += line
    base_frequencies = read_frequency_table("freq_table.tab")
    message_freqs = letter_frequencies(text)
    if is_appropriately_similar(base_frequencies, message_freqs, 10, 2):
        print("It is probably a transposition cipher")
    else:
        print("It is probably a substitution cipher")

if __name__ == "__main__":
    main()
