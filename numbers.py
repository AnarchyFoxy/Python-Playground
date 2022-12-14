#!/usr/bin/env python3

# a = 3
# b = 4

# print(a + 1, a - 1)
# print(b * 3, b / 2)
# print(a % 2, b ** 2)
# print(2 + 4.0, 2.0 ** b)
# print(b / 2 + a)
# print(b / (2.0 + a))

# num = 1 / 3.0
# print(num)

# print('%e' % num)
# print('%4.2f' % num)
# print('{0:4.2f}'.format(num))

# print(repr("Astrydzia"))
# print(str("Astrydzia"))

# print(1 < 2)
# print(2.0 >= 1)
# print(2.0 == 2.0)
# print(2.0 != 2.0)

# X = 2
# Y = 4
# Z = 6

# print(X < Y < Z)
# print(X < Y and Y < Z)

# print(X < Y > Z)
# print(X < Y and Y > Z)

# print(1 < 2 < 3.0 < 4)
# print(1 > 2 > 3.0 > 4)

# print(1.1 + 2.2 == 3.3)
# print(1.1 + 2.2)
# print(int(1.1 + 2.2) == int(3.3))

# print(10 / 4)
# print(10 // 4.0)
# print(10 / 4)
# print(10 // 4.0)

# import math
# print(math.floor(2.5))
# print(math.floor(-2.5))
# print(math.trunc(2.5))
# print(math.trunc(-2.5))

# print(5 / 2, 5 / -2)
# print(5 // 2, 5 // -2)
# print(5 / 2.0, 5 / -2.0)
# print(5 // 2.0, 5 // -2.0)

# import math
# print(5 / -2)
# print(5 // -2)
# print(math.trunc(5 / -2))

# print(999999999999999999999999 + 1)
# print(2 ** 200)

# x = 30
# y = bin(x)
# print(y)
# z = int(y, 2)
# print(z)

# #bity
# x = 1
# print(x << 2)
# print(x | 2)
# print(x & 1)

# #inne operacje numeryczne
# import math
# print(math.pi, math.e)
# print(math.sin(2 * math.pi / 180))
# print(math.sqrt(144), math.sqrt(2))
# print(pow(2, 4), 2 ** 4, 2.0 ** 4.00)
# print(abs(-42.0,), sum((1,2,3,4)))
# print(min(3, 1, 2, 4), max(3, 1, 2, 4))

# print(math.floor(2.567), math.floor(-2.567))
# print(math.trunc(2.567), math.trunc(-2.567))
# print(int(2.567), int(-2.567))
# print(round(2.567), round(2.456), round(2.567, 2))
# print('%.1f' % 2.567, '{0:.2f}'.format(2.567))

# import math
# print(math.sqrt(144))
# print(144 ** .5)
# print(pow(144, .5))

# print(math.sqrt(1234567890))
# print(1234567890 ** .5)
# print(pow(1234567890, .5))

# import random
# print(random.random())
# print(random.random())
# print(random.randint(1, 10))
# print(random.randint(1, 10))
# print(random.choice(["Cyberpunk", "Neuromancer", "Zaratustra", "Atlas zbuntowany"]))
# print(random.choice(["Cyberpunk", "Neuromancer", "Zaratustra", "Atlas zbuntowany"]))
# suits = ["kier", "karo", "trefl", "pik"]
# random.shuffle(suits)
# print(suits)
# random.shuffle(suits)
# print(suits)

#Liczby dziesiętne
# print(0.1 + 0.1 + 0.1 - 0.3)
# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))

#globalne ustawianie precyzji liczb dziesiętnych
# import decimal
# print(decimal.Decimal(1) / decimal.Decimal(7))

# decimal.getcontext().prec = 4
# print(decimal.Decimal(1) / decimal.Decimal(7))

# print(decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3))

# import decimal
# decimal.getcontext().prec = 2
# pay = decimal.Decimal(str(1999 + 1.33))
# print(pay)

# #kontekst dziesiętny
# import decimal
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# with decimal.localcontext() as ctx:
#     ctx.prec = 2
#     print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# #Fraction - liczby ułamkowe
# from fractions import Fraction
# x = Fraction(1, 3)
# y = Fraction(4, 6)
# # print(x, y)

# print(x + y)
# print(x - y)
# print(x * y)

# print(Fraction('.25'))
# print(Fraction('1.25'))
# print(Fraction('.25') + Fraction('1.25'))

# from fractions import Fraction
# print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
from fractions import Fraction
print(Fraction(1, 3))
import decimal
decimal.getcontext().prec = 2
print(decimal.Decimal(1) / decimal.Decimal(3))

print((1 / 3) + (6 / 12))

print(Fraction(6, 12))

print(Fraction(1, 3) + Fraction(6, 12))

print(decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12)))

print(1000.0 / 1234567890)

print(Fraction(1000, 1234567890))

#### Konwersje ułamków, typy mieszane

print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)

x = Fraction(1, 3)
print(x + z)

print(float(x))
print(float(z))
print(float(x + z))
print(17 / 6)

print(Fraction.from_float(1.75))
print(Fraction(*(1.75).as_integer_ratio()))

print(x)
print(x + 2)
print(x + 2.0)
print(x + (1./3))
print(x + (4./3))
print(x + Fraction(4, 3))

print(4.0 /3)
print((4.0 / 3).as_integer_ratio())

print(x)
a = x + Fraction(*(4.0 / 3).as_integer_ratio())
print(a)
print(a.limit_denominator(10))