# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:08:28 2019

@author: Kasia
"""
import random
import string

strenght = input ("Do you need strong (S) or weak (W) password (default strong)?: ")
size = int(input("How many characters should password have (default 6): "))
    
def id_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    if strenght.lower == "s":
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    elif strenght.lower == "w":
        chars = string.ascii_lowercase
    
    return ''.join(random.choice(chars) for _ in range(size))

print (id_generator(size))


