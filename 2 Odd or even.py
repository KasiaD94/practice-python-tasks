# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:16:19 2018

@author: Kasia
"""

number = input("Please provide number: ")
numb = int(number) % 4

if int(number) % 2:
    print("You have provided odd number")
elif numb == 0:
    print ("The number " + number + " is a multiple of 4.")
else:
    print ("you have provided even number")
    
num = input("Provide another number: ")
check= input("Provide the number to check division: ")
if int(num) % int(check):
    print ("The number " + num + " does not divide into " + check)
else:
    print ("The number " + num + " divides into " + check)