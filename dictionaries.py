#!/usr/bin/env python3

# D = {"jedzenie": "Mieloneczka", "ilość": 4, "kolor": "rózowy"}
# print(D["jedzenie"])

# D["ilość"] += 1
# print(D)

# A = {}
# A["imię"] = "Astryda"
# A["zawód"] = "spory"
# A["wiek"] = 30
# print(A)
# print(A['imię'])

# asta1 = dict(imie = "Astryda", zawod = "programistka", wiek = 30)
# print(asta1)

# asta2 = dict(zip(["imie", "zawod", "wiek"], ["Astryda", "programistka", 30]))
# print(asta2)

# #Zagniezdzanie
# rec = {"dane jednostkowe": {"imię": "Astryda", "nazwisko": "Malinowska"},
# "zawód": ['programistka', 'inzynierka', 'spory'],
# "wiek": 30}
# print(rec)
# print(rec['dane jednostkowe'])
# print(rec["dane jednostkowe"]["nazwisko"])
# print(rec["zawód"])
# print(rec["zawód"][-1])
# rec["zawód"].append("Pythonistka")
# print(rec["zawód"])

# #Brakujące klucze, testowanie ifem
# D = {'a': 1, 'b': 2, 'c': 3}
# print(D)
# D['e'] = 99
# print(D)
# #print(D['f'])
# print('f' in D)
# if not 'f' in D:
#     print("Not exist")
#     print("Really not exist")

# value1 = D.get('x', 0)
# print(value1)
# value2 = D['x'] if 'x' in D else 0
# print(value2)

# #Sortowanie kluczy forem
# D = {'a': 1, 'b': 2, 'c': 3}
# Ks = list(D.keys())
# print(Ks)
# Ks.sort()
# print(Ks)
# for key in Ks:
#     print(key, '=>', D[key])

# D = {'a': 1, 'b': 2, 'c': 3}
# for key in sorted(D):
#     print(key, '=>', D[key])

# for c in 'astrydzioszka':
#     print(c.upper())

# x = 4
# while x > 0:
#     print("Astryda! " * x)
#     x -= 1 

# squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
# print(squares)

# squares = []
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     squares.append(x ** 2)
#     print(squares)

# #Krotki
# T = (1, 2, 3, 4)
# print(T)
# print(len(T))

# print(T + (5, 6))
# print(T)
# print(T[0])
# print(T.index(4))
# print(T.count(4))
# # T[0] = 24
# T = (2,) + T[1:]
# print(T)
# T = "Astrydzia", 3.0, [11, 22, 33]
# print(T[1])
# print(T[2][1])
# # T.append(4)