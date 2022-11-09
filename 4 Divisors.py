# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:57:18 2018

@author: Kasia
"""

number = int(input("Please provide a number to divide: "))
list_of_divisors = []
list_divisors = list(range(1, number+1))

for divisor in list_divisors:
    if int(number) % divisor == 0:
        list_of_divisors.append(divisor)
    
print(list_of_divisors)
