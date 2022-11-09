# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:18:33 2019

@author: Kasia
"""
import random

print("Hello my friend! Let's start the game. \n Remember that if you want to quit, just type 'exit'.")
count = 0

while True:
    try:
        number = random.randint(1,9)
        guess = input("Choose a number 1-9: ")
        count += 1
        if number == guess:
            print("You chose exactly right!")
            continue
        elif int(guess) > number:
            print("You guessed too high.")
            continue
        elif int(guess) < number:
            print("You guessed too low.")
            continue
        tracker = []
    except ValueError:
        if guess.lower() == "exit":
            print("You have tried", count-1, "times!")
            break
        else:
            print ("You typed something wrong, try again!")
            continue
    
    