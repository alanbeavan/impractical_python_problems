#!/usr/bin/env python3.6
"""Enumerate possible keys for a route cipher given a number of columns."""

import itertools

def key_permutations(ncol):
    """Return a list of possible keys for the number of columns.
    
    Returns a list of lists.
    """
    cols = list(range(1, ncol + 1))
    initial_perms = list(itertools.permutations(cols))
    total_perms = []
    for perm in initial_perms:
        total_perms.append(list(perm))
        for i in range(1, ncol+1):
            combos = itertools.combinations(perm, i)
            for combo in combos:
                to_modify = list(perm)
                for j in combo:
                    to_modify[j-1] = to_modify[j-1] * -1
                total_perms.append(to_modify)
    return total_perms

def main():
    """Do the things."""
    ncol = int(input("How many columns?"))
    keys = key_permutations(ncol)
    for key in keys:
        print(" ".join(list(map(str, key))))

if __name__ == "__main__":
    main()
