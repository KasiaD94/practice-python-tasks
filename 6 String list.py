# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 14:44:21 2018

@author: Kasia
"""

string = input ("Provide a word to check: ")

rvs = string[::-1]

if rvs == string:
    print("This is a palindrom.")
else:
    print("Not a palindrom")
    
