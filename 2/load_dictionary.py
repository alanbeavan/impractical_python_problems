#!/usr/bin/env python3.6
"""load a file as a list of the lines in lower case.

Arguements:
-dictionary file name

Exceptions:
-IOError if file not openable (ie. not found)

Returns:
-A list of the lines of the file in lower case

Requires:
-import sys
"""

import sys

def load(file):
    """Open a dictionary returning a list of the lower case words"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)

