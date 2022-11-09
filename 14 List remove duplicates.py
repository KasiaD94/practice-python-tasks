# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:04:25 2019

@author: Kasia
"""
a = [1,1,2,2,3,3,4,4,5,5,6,6,7,7]

def duplicates(y):
    b = []
    for x in y:
        if x not in b:
            b.append(x)
    return b

def duplicates2(y):
    return list(set(y))

print (duplicates(a))
print (duplicates2(a))
