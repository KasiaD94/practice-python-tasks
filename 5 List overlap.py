# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:09:05 2018

@author: Kasia
"""
import random

d = range(1, random.randint(1,30))
e = range(1, random.randint(10,40)) 
f = []

for i in d:
    if i in e:
        if i not in f:
            f.append(i)
            
print("d = ", list(d), "\n", "e = ", list(e), "\n", "f =", f)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for item in a:
    if item in b:
        if item not in c:
            c.append(item)
        
print (c)

new = set(a) & set(b)
print (new)
