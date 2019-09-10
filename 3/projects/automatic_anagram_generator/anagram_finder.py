#!/usr/bin/env python3.6
"""Print a number of anagram phrases.

Interactively ask the user for a phrase and minumum word size.
Load dictionary
While there are letters left are there are sub_algorithms left
    Convert word to list of letters
    Obtain sub_algorithms
    Update anagram
If the letters are exhausted
    update anagrams with anagram

"""
import sys
import collections
import load_dictionary
import my_module as mod
sys.setrecursionlimit(1500)

def get_anagrams(phrase, word_list, left, index = [0], chosen = [], anagrams = [], nest = 0):
    """Return all anagrams from the word and the word list."""
    if index[nest] < len(word_list):
        sub_anagram = word_list[index[nest]]
        if is_sub_anagram(sub_anagram, left):
            chosen.append(sub_anagram)
            if len("".join(chosen)) == len("".join(phrase)):
                #anagram completed
                anagrams.append(chosen)
                chosen = chosen[:len(chosen)-1]
                index[nest] += 1
                get_anagrams(phrase, word_list, left, index = index,
                             anagrams = anagrams, chosen = chosen, nest = nest)
            else:
                #anagram not yet completed
                for letter in sub_anagram:
                    left.remove(letter)
                nest += 1
                if len(index) > nest:
                    index[nest] = 0
                else:
                    index.append(0)
                get_anagrams(phrase, word_list, left, index = index, 
                             chosen = chosen, anagrams = anagrams, nest = nest)
        else:
            index[nest] += 1
            get_anagrams(phrase, word_list, left, index, chosen, anagrams, nest)
    else:
        if collections.Counter("".join(left)) == collections.Counter("".join(phrase)):
            #all words exhausted
           return anagrams
        else:
            #run out of words for this nest and this chosen
            for letter in chosen[len(chosen)-1]:
                left.append(letter)
            chosen = chosen[:len(chosen)-1]
            nest = nest - 1
            index[nest] += 1
            get_anagrams(phrase, word_list, left, index, chosen, anagrams, nest)
    return anagrams

def get_sub_anagrams(phrase, word_list):
    """Return all words in list that can be made from word."""
    anagrams = []
    for word in word_list:
        if is_sub_anagram(word, phrase):
            anagrams.append(word)
    return anagrams

def is_sub_anagram(word, phrase):
    """Return 1 is word is subanagram of phrase."""
    counts = collections.Counter("".join(phrase))
    test = ""
    word_counts = collections.Counter(word.lower())
    for letter in word:
        if word_counts[letter] <= counts[letter]:
            test += letter
    if collections.Counter(test) == word_counts:
        return 1
    return 0
   

def get_user_input():
    """Ask the user for their word and min word size."""
    phrase = input("Enter your phrase to anagram.")
    min_word_size = int(input("Enter your minimum word size."))
    phrase = "".join(phrase.split(" "))
    return phrase, min_word_size

def main():
    """Call functions to show the user their anagrams."""
    phrase, min_word_size = get_user_input()
    phrase = list(phrase)
    
    word_list = load_dictionary.load("dictionary.txt")
    word_list = set([word for word in word_list if len(word) >= min_word_size])
    word_list = get_sub_anagrams(phrase, word_list)
    
    anagrams = get_anagrams(phrase, word_list, phrase.copy())
    print(anagrams)
    to_print = min(500, len(anagrams))
    for anagram in anagrams[0:to_print]:
        print(" ".join(anagram))

if __name__ == "__main__":
    main()
