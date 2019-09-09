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

def prep_words(name, word_list):
    """Return filtered dicitonary.
    
    The applied filter removes words with a different
    number of letters to the name."""
    length = len(name)
    good_words = []
    for word in word_list:
        if len(word) == length:
            good_words.append(word)

    return good_words

def cv_map(word):
    """Return the cv map for a word."""
    mapped = ""
    for letter in word:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            mapped += "v"
        else:
            mapped += "c"
    return mapped

def cv_map_words(word_list):
    """Enumerate the CV maps in a list of words."""

    cv_maps = set()
    for word in word_list:
        motif = cv_map(word)
        if motif not in cv_maps:
            cv_maps.add(motif)

    return cv_maps

def cv_map_filter(name, cv_maps):
    """Filter anagrams to remove CV maps that don't occur in English."""
    perms = permutations(name)
    filtered = set()
    for perm in perms:
        if cv_map(perm) in cv_maps:
            filtered.add(perm)
    return filtered

def get_trigrams(word):
    """Enumerate the trigrams of a word."""
    trigrams = []
    word = "".join(word)
    for i in range(0, len(word)-2):
        trigrams.append(word[i:i+3])
    return trigrams

def trigram_filter(perms, bad_trigrams):
    """Filter out anagrams with trigrams in the list given."""
    removed = set()
    for perm in perms:
        trigrams = get_trigrams(perm)
        for trigram in trigrams:
            if trigram in bad_trigrams:
                removed.add(perm)
                break
    filtered = perms - removed
    return filtered

def digram_filter(perms):
    """Filter anagrams containing unlikely digrams.
    
    Here the digrams are hard coded. I guess this could be changed."""
    removed = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
               'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd',
                          'rl', 'rm', 'rt', 'rv', 'tl', 'tm']

    for perm in perms:
        perm = "".join(perm)
        if perm[0:2] in first_pair_rejects or perm[0:2] in rejects:
            removed.add(perm)
        else:
            for i in range(1, len(perm)-1):
                if perm[i:i+2] in rejects:
                    removed.add(perm)
                    break
    filtered = perms - removed
    return filtered

def view_by_letter(name, anagrams):
    """Show the user anagrams beginning with a letter of their choice."""
    flag = 1
    while flag:
        letter = input("What letter do you want to start with?\n").lower()
        for anagram in anagrams:
            if anagram[0] == letter:
                print("".join(anagram))
        if input("\n\nThat's it!\nAnother letter?\n").lower() not in ["y", "yes", "p"]:
            flag = 0


def main():
    """Call funtions to limit the anagrams and help the user find one."""
    name = "tmvoordle"
    name = name.lower()

    word_list = load_dictionary.load("dictionary.txt")
    bad_trigrams = load_dictionary.load("least_likely_trigrams.txt")

    word_list = prep_words(name, word_list)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigram_filter(filter_1, bad_trigrams)
    filter_3 = digram_filter(filter_2)
    view_by_letter(name, filter_3)

if __name__ == "__main__":
    main()
