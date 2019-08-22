#!/usr/bin/env python3.6
"""pig_latin.py.

takes a word as input and prints the pig latin version of it.
"""

def main():
    """
    main.

    ask the user for a word and use string indexing
    to print the pig latin version of it
    """
    while True:
        word = input("Gizzus a word lad\n\n")
        if word:
            if word.title()[0] in ["A", "E", "I", "O", "U"]:
                print(word.lower() + "way\n")
            elif len(word) > 1:
                print(word.lower()[1:] + word.lower()[0] + "ay\n")
            else:
                print("shit word")
        else:
            print("shit word")

        choice = input("Play again?\n")
        if choice not in ["y", "Y", "yes", "Yes"]:
            exit()

if __name__ == "__main__":
    main()
