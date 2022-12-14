#!/usr/bin/env python3

#Reference to the same list object
L1 = [2, 3, 4]
L2 = L1
print(L1, L2)
#[2, 3, 4] [2, 3, 4]

L1[0] = 30
print(L1, L2)
#[30, 3, 4] [30, 3, 4]


#how to copy an object
L3 = [30, 60, 90]
print(L3)
#[30, 60, 90]
L4 = L3[:]
print(L4)
#[30, 60, 90]
L3[2] = 180
print(L3, L4)
#[30, 60, 180] [30, 60, 90]

#using copy module
import copy
L5 = {"Programmer": "Asta", "Location": "Earth", "Status": "Invincible"}
L6 = copy.copy(L5)
print(L6)

#comparison
A = [1, 2, 3]
M = A
print(A ==  M)
#True                                                
#if refer is to the same object:                                                                                                      
print(A is M)                                       
#True
#if not:
A = [1, 2, 3]
M = [1, 2, 3]
print(A == M)
#True
print(A is M)
#False
#but small numbers:
x = 42
y = 42
print(x == y)
#True
print(x is y)
#True

#check all references
import sys
print(sys.getrefcount(1))
#2723