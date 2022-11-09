# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:28:11 2019

@author: Kasia
"""

number = int(input("Please provide a number: "))
list_divisors = list(range(1, number+1))
list_of_divisors = [divisor for divisor in list_divisors if int(number) % divisor == 0]

def check_prime_number():
    
    if list_of_divisors == [1, number]:
        return ("This number is prime.")
    else:
        return ("This is not prime number.")
    
numb = check_prime_number()
print (numb)
