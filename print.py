from __future__ import print_function

import sys

print(1, 2, 3, 4, 5, sep="|", end='\n', file=sys.stdout)

sys.stdout.write("Hi...\n")

a = raw_input("enter a value: ")
print("given a value:", a)
