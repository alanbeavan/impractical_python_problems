#!/usr/bin/env python3.6
"""Remove all the single letter words from the dictionary.

Arguments:
Dictionary list

Returns:
Modified dictionary
"""

def single_letters_removed(words):
    """Return dictionary that doesn't contain sinlge letter words."""
    copy = words.copy()
    for word in words:
        if len(word) == 1:
            copy.remove(word)
    return(copy)
