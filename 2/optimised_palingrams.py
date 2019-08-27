#!/usr/bin/env python3.6
"""Find palingrams in a dictionary.

loop through all 2-word combinations and print
palingrams in a sorted well presented list

requires load_dictionary
"""
import load_dictionary

def find_palingrams(words):
    """Return a list of space spearated word pairs that are palingrams."""
    palingrams = []
    for word in words:
        if len(word) > 1:
            for i in range(1, len(word)):
                if word[i:] == word[i:][::-1] and word[:i][::-1] in words:
                    palingrams.append(" ".join([word, word[:i][::-1]]))
                if word[:i] == word[:i][::-1] and word[i:][::-1] in words:
                    palingrams.append(" ".join([word[i:][::-1], word]))
    return palingrams

def main():
    """Find palingrams and print them."""
    words = set(load_dictionary.load("dictionary.txt"))
    to_print = find_palingrams(words)
    print("\n".join(sorted(to_print)))

if __name__ == "__main__":
    main()
