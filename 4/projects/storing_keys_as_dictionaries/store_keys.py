#!/usr/bin/env python3.6
"""Ask the user for a key and store it as a dictionary column : order."""

import re

def main():
    """Do the things."""
    key = input("What's the key (the format would look like 1 -2 3 4")
    key_dict = {}
    for entry in key.split():
        if re.search("-", entry):
            key_dict[entry[1:]] = "reverse"
        else:
            key_dict[entry] = "forward"
    print(key_dict)

if __name__ == "__main__":
    main()
