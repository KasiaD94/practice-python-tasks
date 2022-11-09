# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 19:59:41 2019

@author: Kasia
"""

with open('prime_num.txt', 'r') as open_file:
    prime = open_file.read()
    
with open('happy_num.txt', 'r') as read_file:
    happy = read_file.read()
    
list_prime = list(prime.split('\n'))
list_happy = list(happy.split('\n'))

overlap = []
for i in list_prime:
    if i in list_happy:
        overlap.append(i)
        
print(overlap)
