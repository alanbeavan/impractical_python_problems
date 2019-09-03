#!/usr/bin/env python3.6
"""Print all the anagrams from a dicitonary for a word."""
import load_dictionary

def is_anagram(query, word):
    """Return 1 is word is anagram of query."""
    if len(word) == len(query):
        if sorted(word) == query:
            return 1
    return 0

def main():
    """Ask the user for a word and print the anagrams."""
    words = set(load_dictionary.load("dictionary.txt"))
    while True:
        query_word = input("\ngizzus a word\n")
        query = sorted(query_word)
        anagrams = []
        for word in words:
            if word != query_word:
                if is_anagram(query, word):
                    anagrams.append(word)

        print("\nAnagrams:\n" + "\n".join(anagrams))

        choice = input("\nPlay again?\n")
        if choice.lower() in ["n", "no", "q", "quit"]:
            exit()

if __name__ == "__main__":
    main()
