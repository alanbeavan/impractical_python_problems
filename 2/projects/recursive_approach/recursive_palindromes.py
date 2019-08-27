#!/usr/bin/env python3.6
"""Find palindromes (letter palingrams) in a dictionary file."""

import load_dictionary

word_list = sorted(set(load_dictionary.load('../../dictionary.txt')))

def pali_check(string):
    if len(string) <= 1:
        return 1
    elif string[0] == string[-1]:
        return pali_check(string[1:len(string)-1])
    else:
        return 0


pali_list = []
for word in word_list:
    if len(word) > 1 and pali_check(word):
           pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
