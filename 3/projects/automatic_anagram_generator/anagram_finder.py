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
import collections
import load_dictionary
import my_module as mod

def get_anagrams(phrase, word_list, left, index = [0], chosen = [], anagrams = [], nest = 0):
    """Return all anagrams from the word and the word list."""
    print("phrase - ", end = "")
    print(phrase)
    print("word_list (len) - ", end = "")
    print(len(word_list))
    print("left - ", end = "")
    print(left)
    print("index - ", end = "")
    print(index)
    print("chosen - ", end = "")
    print(chosen)
    print("anagrams - ", end = "")
    print(anagrams)
    print("nest - ", end = "")
    print(nest)




    sub_anagrams = get_sub_anagrams(left, word_list)
    print(sub_anagrams)
    if sub_anagrams:
        if index[nest] < len(sub_anagrams):
            if len(sub_anagrams) > 0:
                for sub_anagram in sub_anagrams[index[nest]:]:
                    print(sub_anagram)
                    chosen.append(sub_anagram)
                    if len(left) - len(sub_anagram) == 0:
                        #anagram completed
                        anagrams.append(chosen)
                        print("opt 1 " + " ".join(chosen))
                        chosen = chosen[:len(chosen)]
                        index[nest] += 1
                        get_anagrams(phrase, word_list, left, index = index,
                                     anagrams = anagrams, chosen = chosen, nest = nest)
                    else:
                        #anagram not yet completed
                        for letter in sub_anagram:
                            left.remove(letter)
                        print("opt 2 " + " ".join(chosen))
                        nest += 1
                        if len(index) > nest:
                            index[nest] = 0
                        else:
                            index.append(0)
                        get_anagrams(phrase, word_list, left, index = index, 
                                     chosen = chosen, anagrams = anagrams, nest = nest)
        else:
            if left == phrase:
                #all words exhausted
                return anagrams
            else:
                #run out of words for this nest and this chosen
                print("opt 3 " + " ".join(chosen))
                index[0] += 1
                get_anagrams(phrase, word_list, phrase.copy(), index = index, anagrams = anagrams, nest = 0)
    else:
        #no sub anagrams found
        print("opt 4")
        index[0] += 1
        get_anagrams(phrase, word_list, phrase.copy(), index = index, anagrams = anagrams, chosen = [], nest = 0)

def get_sub_anagrams(phrase, word_list):
    """Return all words in list that can be made from word."""
    counts = collections.Counter("".join(phrase))
    print(counts)
    anagrams = []
    for word in word_list:
        test = ""
        word_counts = collections.Counter(word.lower())
        for letter in word:
            if word_counts[letter] <= counts[letter]:
                test += letter
        if collections.Counter(test) == word_counts:
            anagrams.append(word)
    return anagrams

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
    
    anagrams = get_anagrams(phrase, word_list, phrase.copy())
    to_print = min(500, len(anagrams))
    print("\n".join(anagrams[1:to_print]))

if __name__ == "__main__":
    main()
