#!/usr/bin/env python3

# x = set("Astrydzia")
# y = {'M', 'a', 'r', 'k', 'u', 's'}
# print(x, y)
# print(x & y)
# print(x | y)
# print(x - y)
# print(x > y)
# z = {x ** 2 for x in [1, 2, 3, 4]}
# print(z)

# print(list(set([1, 2, 3, 2, 1, 4, 5, 3, 4])))

# print(set("Astrydzia") - set("Markus"))
# print(set("Astrydzia") == set("aizdyrtsA"))

# print('A' in set("Astrydzia"), "a" in "Astrydzia", "Markus" in ["jajka", "Astrydzia", "Markus"])


print(1 / 3)
print((2 / 3) + (1 / 2))

import decimal
d = decimal.Decimal("3.141")
d += 1
print(d)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal("3.00"))

from fractions import Fraction
f = Fraction(2, 3)
print(f)
f += 1
print(f)
print(f + Fraction(1, 2))

L = [None] * 100
print(L)

print(type(type(L)))

if type(L) == type([]):
    print("Tak")

if type(L) == list:
    print("Tak")

if isinstance(L, list):
    print("Tak")