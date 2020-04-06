import fractions
from fractions import Fraction as fr

print(fractions.Fraction(1.5)) # 3/2

print(fractions.Fraction(5)) # 5

print(fractions.Fraction(1,3)) # 1/3

print(fractions.Fraction(1.1))

print(fractions.Fraction('1.1')) # 11/10

print(fr(1,3) + fr(1,3)) # 2/3

print(1 / fr(5,6)) # 6/5

print(fr(-3,10) > 0) # False

print(fr(-3,10) < 0) # True
