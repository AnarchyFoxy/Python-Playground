#!/usr/bin/env python3

# #Operacje na typach sekwencyjnych
# L = [123, "Mielonka", 1.23]
# print(len(L))

# print(L[0])
# print(L[:1])
# print(L + [4, 5, 6])
# print(L * 2)
# print(L)

# #Operacje specyficzne dla typu
# L.append("NI")
# print(L)
# L.pop(2)
# print(L)

# M = ["bb", "aa", "cc"]
# print(M)
# M.sort()
# print(M)
# M.reverse()
# print(M)

# #Zagniezdzanie
# M = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

# print(M)
# print(M[1])
# print(M[1][2])

# #Listy składane
# M = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
# col2 = [row[1] for row in M]
# print(col2)

# rowx = [row[1] + 1 for row in M]
# print(rowx)
# rowy = [row[1] for row in M if row[1] % 2 == 0]
# print(rowy)

# M = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]
# diag = [M[i][i] for i in [0, 1, 2]]
# print(diag)

# doubles = [c * 2 for c in "Mielonka"]
# print(doubles)

# x = list(range(4))
# print(x)

# y = list(range(-6, 7, 2))
# print(y)

# z = [[x * 2, x ** 3] for x in range(4)]
# print(z)

# a = [[x, x /2, x * 2] for x in range(-6, 7, 2) if x > 0]
# print(a)

# M = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

# G = (sum(row) for row in M)
# print(next(G))
# print(next(G))
# print(next(G))

# print(list(map(sum, M)))

# x = {sum(row) for row in M}
# print(x)

# y = {i : sum(M[i]) for i in range(3)}
# print(y)

# z = [ord(x) for x in "mielonka"]
# print(z)
# a = {ord(x) for x in "mieloonka"}
# print(a)
# a2 = {x : ord(x) for x in "mieloneczka"}
# print(a2)
# b = (ord(x) for x in "spaaaaam")
# print(b)