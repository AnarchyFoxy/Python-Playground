# #!/usr/bin/env python3

# S = "Mielonka"
# print(len(S))

# print(S[0])
# print(S[1])

# #slices
# print(S[1:3])

# print(S[1:])
# print(S)
# print(S[0:7])
# print(S[:7])
# print(S[:-1])
# print(S[:])

# print(S)
# print(S + "xyz")
# print(S)
# print((S + ' ') * 8)

# print(S)
# S = 'z' + S[1:]
# print(S)

# #Niezmienność
# Q = "taczka"
# L = list(Q)
# print(L)
# L[0] = 'p'
# print(''.join(L))

# B = bytearray(b'mini')
# B.extend(b'maraton')
# print(B)
# print(B.decode())


# #Metody specyficzne dla typu
# S = "Mielonka"
# print(S.find("l"))

# print(S.replace("ie", "XYC"))
# print(S)

# line = "aaa,bbb,ccccc,dd"
# print(line)
# print(line.split(','))
# line2 = line.split(',')
# print(line2)

# S = "Mielonka"
# S2 = S.upper()
# print(S2)

# line = "aaaa,bbbbbb,cc,ddddd\n"
# print(line)
# line2 = line.rstrip()
# print(line2)

# line3 = line.rstrip().split(',')
# print(line3)

# x = "%s, jajka i %s" % ("mielonka", "MIELONKA!")
# print(x)

# y = "{0}, jajca i {1}".format("mielonka", "MIELONKA!!!")
# print(y)

# z = "{}, jojeczka i {}".format("mieloneczka", "MIELONECZKA!!!!")
# print(z)

# a = "{:,.2f}".format(296999.2567)
# print(a)

# b = "%.2f | %+05d" % (3.14159, 42)
# print(b)

# #uzyskiwanie pomocy
# print(dir(S))

# print(S + "NI!")
# print(S.__add__("NI!!"))

# print(help(S.replace))

# #inne kodowanie znaków
# S = "A\nB\tC"
# print(len(S))

# print(ord('\n'))

# S = "A\0B\0C"
# print(len(S))
# print(S)

# msg = """
# AAAAAAAAAAAAAAAAAAAA
# bbbbbbbbbbbbbb
# 'ccccccc'ccccccc
# ddddddddddd
# """
# print(msg)

# path = r"C:\tekst\nowy\hehehe"
# print(path)

# #dopasowanie wzorców
# import re
# match = re.match("Witaj, [\t]*(.*)Astrydo", "Witaj, Lady   Astrydo")
# print(match.groups(1))

# match = re.match("[/:](.*)[/:](.*)[/:](.*)", "/usr/home:refrasta")
# print(match.groups())
# split = re.split("[/:]", "/usr/home/refrasta")
# print(split)