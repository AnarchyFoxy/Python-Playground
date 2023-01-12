#!/usr/bin/env python3

print(len("abc"))
print("abc" + "def")
print("Ni!" * 5)
print("-" * 80)
'''
3
abcdef
Ni!Ni!Ni!Ni!Ni!
--------------------------------------------------------------------------------
'''

myjob = "hacker"
for c in myjob: print(c, end=' ')
#h a c k e r 
print()
print('k' in myjob)
print('z' in myjob)
print('jajko' in "asefwefewjajkoadsgqwdfgqy")
"""
True
False
True
"""

S = "abcdefghijklmnopqrstuwxyz"
print(S[1:24:2])
print(S[::2])
""""
bdfhjlnprtwy
acegikmoqsuxz
"""

S = "halo"
print(S[::-1])
#olah

S = "abcdefg"
print(S[5:1:-1])
#fedc

print("Mielonka"[1:3])
print("Mielonka"[slice(1, 3)])
print("Mielonka"[::-1])
print("Mielonka"[slice(None, None, -1)])
"""
ie
ie
aknoleiM
aknoleiM
"""