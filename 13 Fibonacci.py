# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:01:13 2019

@author: Kasia
"""

def fibonacci():
    number = int(input("How many Fibonacci numbers you want to generate(more than 1): "))
    sequence = [1,1]
    for x in range(number - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return print(sequence)

fibonacci()

        