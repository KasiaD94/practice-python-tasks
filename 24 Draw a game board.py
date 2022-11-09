# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 20:34:45 2019

@author: Kasia
"""

def tictac(size):
    while True:
        size = input("Welcome to a game board! What size should be the board? ")
        for i in range(int(size)):
            print(" ---" * int(size))
            print("|   " * (int(size)+1))
        print(" ---" * int(size)) 
        try_again = input("Do you want to play again? Y/N ")
        if try_again.lower() == "y":
            continue
        else: 
            break
        
tictac(size = 3)
