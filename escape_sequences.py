#!/usr/bin/env python3

#using escape sequence
s = "a\nb\tc"
print(s)
"""
a
b       c
"""

print(len(s))
#5

T = "a\ts\nt\x00ryda"
print(T)
'''
a       s
tryda
'''
