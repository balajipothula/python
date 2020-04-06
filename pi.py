from __future__ import print_function
from math import pi, e
from sys import path
import decimal

print("PI:", pi)
print("E :", e)
#print(path)

print((1.1 + 2.2))

print((1.1 + 2.2) == 3.3)

print(float(1.1 + 2.2) == float(3.3))

print(decimal.Decimal(1.1 + 2.2) == decimal.Decimal(3.3))

print(decimal.Decimal(1.1) + decimal.Decimal(2.2) == decimal.Decimal(3.3))
