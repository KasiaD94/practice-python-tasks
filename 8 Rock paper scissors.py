# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 20:39:12 2019

@author: Kasia
"""
import random

choose = ["R", "S", "P"]

while True:
    player1 = (input("Do you want to play as a Rock (press R), Scissors (press S) or as a Paper (press P) ")).upper()
    player2 = random.choice(choose)
    if player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
        print ("You are the winner")
        break
    elif player1 == "R" and player2 == "R" or player1 == "S" and player2 == "S" or player1 == "P" and player2 == "P":
        print ("Draw! Try again!")
        try_again = input("Do you want to play again? Y/N ")
        if try_again.lower() == "y":
            continue
        else: 
            break
    elif player1 != "R" and "S" and "P" :
        print ("you typed something wrong. Please try again.")
        try_again = input("Do you want to play again? Y/N ")
        if try_again.lower() == "y":
            continue
        else: 
            break
    else:
        print ("Computer is the winner")
        try_again = input("Do you want to play again? Y/N ")
        if try_again.lower() == "y":
            continue
        else: 
            break
        