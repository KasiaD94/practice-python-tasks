# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:33:56 2018

@author: Kasia
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
y = []

for i in a:
    if i < 5:
        x.append(i)

print (x)
        
number = input("Provide a number: ")
for i in a:
    if i < int(number):
        y.append(i)
print(y)