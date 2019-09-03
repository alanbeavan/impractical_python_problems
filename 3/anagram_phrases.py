#!/usr/bin/env python3.6
"""Help a user to generate an anagram of their phrase."""

import collections
import sys
import load_dictionary

def get_anagrams(words, query):
    """Help user to build an anagram phrase."""
    counts = collections.Counter("".join(query.split()))
    anagrams = []
    for word in words:
        test = ""
        word_counts = collections.Counter(word.lower())
        for letter in word:
            if word_counts[letter] <= counts[letter]:
                test += letter
        if collections.Counter(test) == word_counts:
            anagrams.append(word)
    print(*anagrams, sep="\n")
    print("\nRemaining letters = {}".format(query))
    print("Number of remaining letters = {}".format(len(query)))
    print("Number of remaining (real word) anagrams",
          "= {}".format(len(anagrams)))

def process_choice(query, words):
    """Check if choice is valid, return choice and remaining letters."""
    while True:
        choice = input("Choose a word, hit RETURN to start over,",
                       "or \"#\" to quit: ")
        if choice == "":
            pipeline(words)
        elif choice == "#":
            exit()
        else:
            candidate = "".join(choice.lower().split())
            left = list(query)
            for letter in candidate:
                if letter in left:
                    left.remove(letter)
            if len(query) - len(left) == len(candidate):
                break
            else:
                print(query)
                print(left)
                print(candidate)
                print("Invallid word: Choose something that works",
                      file=sys.stderr)
    query = "".join(left)
    return choice, query

def pipeline(words):
    """Set up anagram finder and run."""
    original_query = input("Gizzus some kind of phrase. Maybe your name?\n")
    query = "".join(original_query.lower().split())
    phrase = ""
    while len("".join(phrase.split())) < len("".join(original_query.split())):
        get_anagrams(words, query)
        to_add, query = process_choice(query, words)
        phrase += to_add + " "


    print(phrase)
    answer = input("Play again?\n")
    if answer.lower() in ["y", "yes", "ye"]:
        pipeline(words)


def main():
    """Load dictionary and keep getting anagram phrases until told to stop."""
    words = load_dictionary.load("dictionary.txt")
    pipeline(words)

if __name__ == "__main__":
    main()
