# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 21:19:03 2019

@author: Kasia
"""
import random

print("Hello my friend!\nImagine the number between 0 and 100.")
print("If computer guessed the number, type OK, if the number was too high, type H, if was too low, type L.")
print("P.S. Remember that if you want to quit, just type 'exit'.")
count = 0


while True:
    com_guess = random.randint(0,100)
    print(com_guess)
    num = input("Type: OK / H / L: ")
    count += 1
    if num.lower == "ok":
        print("Computer chose exactly right!")
        break

    elif num.lower == "h":
        print("Computer guessed too high.")
        continue
    
    elif num.lower == "l":
        print("Computer guessed too low.")
        continue
    
    elif num.lower == "exit":
        break
    
    tracker = []
