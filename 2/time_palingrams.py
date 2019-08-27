#!/usr/bin/env python3.6
import time
import optimised_palingrams
import load_dictionary
words = set(load_dictionary.load("dictionary.txt"))
start_time = time.time()
optimised_palingrams.find_palingrams(words)
end_time = time.time()
print("This took {} seconds".format(str(end_time - start_time)))
