#!/usr/bin/env python3.6
"""silly_name_generator."""
import random
from colorama import Fore
from colorama import Style
import my_module as mod


def main():
    """
    main.

    prints amusing combinations of Greek first names and English second names
    until the user has had enough
    """
    first_name_lines = mod.get_file_data("first_names")
    first_names = []
    for line in first_name_lines:
        name = line.split()[0]
        if name.isupper():
            first_names.append(name.title())

    family_name_lines = mod.get_file_data("family_names")
    family_names = []
    i = 1
    for line in family_name_lines:
        if line.startswith(str(i)):
            name = line.split("\t")[1].split(" ")[-1]
            family_names.append(name)
            i += 1

    while True:
        print(f"\n\n{Fore.RED}" + random.choice(first_names) + " "
              + random.choice(family_names) + f"{Style.RESET_ALL}\n\n")

        #alternative
        #print("\n\n{} {}\n\n".format(random.choice(first_names),
        #                            random.choice(family_names)))

        opt = input("again?")
        if opt not in ["y", "yes"]:
            exit()

if __name__ == "__main__":
    main()
