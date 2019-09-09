#!/usr/bin/env python3.6
"""Helps the user find an anagram

From a collection of letters, heuristically limit
the options using CV mapping, trigrams and digrams.
Finally show the user the options based on the letter they
want to start with.
"""


import sys
from itertools import permutations
import load_dictionary

def enumerate_digrams(word_list):
    """Returns a dictionary of the % of each digram"""
    freqs = {}
    count = 0
    for word in word_list:
        word = "".join(word)
        if len(word) > 1:
            for i in range(0, len(word)-2):
                digram = word[i:i+2]
                count += 1
                if digram in freqs:
                    freqs[digram] += 1
                else:
                    freqs[digram] = 1
    for key, value in freqs.items():
        freqs[key] = value/count * 100
    
    return freqs

def print_counts(word, digrams):
    """Prints the digram frequency of all digrams in the word."""
    for i in range(0, len(word) - 1):
        digram = word[i:i+2]
        if digram in digrams:
            print(digram + "\t" + str(digrams[digram]) + "%")
        else:
            print(digram + "\t0%")

def main():
    """Call funtions to limit the anagrams and help the user find one."""
    name = "tmvoordle"
    name = name.lower()

    word_list = load_dictionary.load("dictionary.txt")

    freqs = enumerate_digrams(word_list)
    print_counts(name, freqs)
    
if __name__ == "__main__":
    main()
