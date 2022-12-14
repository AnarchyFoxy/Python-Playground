#!/usr/bin/env python3

# # Zbiory
# x = set("abcde")
# y = set("bdxyz")
# print(x)
# print(y)

# print(x - y)
# print(x | y)
# print(x & y)
# print(x ^ y)
# print(x > y, x < y)

# ###################
# print('e' in x)
# print('e' in "mielonka", 22 in [11, 22, 33])
# ###################

# z = x.intersection(y)
# print(z)
# z.add("ASTRYDZIA")
# print(z)
# z.update(set(['X', 'Y']))
# print(z)
# z.remove('b')
# print(z)

# for item in set("abc"):
#     print(item * 3)

# S = set([1, 2, 3])

# print(S | set([3, 4]))

# print(S.union([3, 4]))

# print(S.intersection((1, 3, 5)))

# print(S.issubset(range(-5, 5)))

# print(set([1, 2, 3, 4]))
# print(set("astrydzia"))
# print({1, 2, 3, 4, 5, 6, 7})

# S.add("Gazelka")
# print(S)

# S1 = {1, 2, 3, 4}
# print(S1 & {1, 3})

# print({1, 5, 3, 6} | S1)

# print(S1 - {1, 3, 4})

# print(S1 > {1, 3})

# print({1, 2, 3}.union([3, 4]))
# print({1, 2, 3}.union({3, 4}))
# print({1, 2, 3}.union(set([3, 4])))
# print({1, 2, 3}.intersection((1, 3, 5)))
# print({1, 2, 3}.issubset(range(-5, 5)))

# #zbiór składany
# print({x ** 2 for x in [1, 2, 3, 4]})

# print({x for x in "Astrydzia"})

# print({c * 4 for c in "Astrydzia"})

# print({c * 4 for c in "Gazelcia"})

# S = {c * 4 for c in "Astrydzia"}

# print(S | {"mmmm", "xxxx"})
# print(S & {"mmmm", "xxxx", 'AAAA'})

# #dlaczego zbiory
# L = [1, 2, 1, 2, 3, 2, 4, 5]
# print(L)
# print(set(L))

# L = list(set(L))
# print(L)

# L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
# print(L1 == L2)
# print(set(L1) == set(L2))
# print(sorted(L1) == sorted(L2))

# engineers = {"Astryda", "Gazela", "Anna", "Aleksandra"}
# managers = {"Astryda", "Astrydzioszka"}
# print("Gazela" in engineers)
# print(engineers & managers)
# print(engineers | managers)
# print(engineers - managers)
# print(managers - engineers)
# print(engineers > managers)
# print({"Astryda", "Gazela"} < engineers)
# print((managers | engineers) > managers)
# print(managers ^ engineers)
# print((managers | engineers) - (managers ^ engineers))