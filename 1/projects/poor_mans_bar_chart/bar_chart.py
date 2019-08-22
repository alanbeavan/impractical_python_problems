#!/usr/bin/env python3.6
"""bar_chart.py.

take a string as input
print a bar_chart (with hashes i guess) to the screen
where the length of bars corresponds to the number of
times the letter appeared in the string
"""


def main():
    """
    main.

    promt the user for an input string
    for each letter coverred (in alphabetical order)
    print the letter and the number of hashes equal to the number of occurances
    """
    string = input("gizzus string\n")

    counts = {}
    for char in  string:
        if char != " ":
            if char.upper() in counts:
                counts[char.upper()] += 1
            else:
                counts[char.upper()] = 1

    for char in sorted(counts.keys()):
        print(char, end=" ")
        print('#' * counts[char])

if __name__ == "__main__":
    main()
