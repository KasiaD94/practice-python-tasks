# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:54:12 2019

@author: Kasia
"""

import random


def compare_numbers(number, guess):
    cowsbulls = [0, 0]
    for i in range(len(guess)):
        if number[i] == guess[i]:
            cowsbulls[1] += 1
        elif guess[i] in number:
            cowsbulls[0] += 1
    return cowsbulls

if __name__=="__main__":
    play = True
    num = str((random.randint(1000,9999)))
    number = list(num)
    print ("Welcome to the \"Bulls - Cows\" game!")
    print ("You need to guess a 4 digit number.")
    print ("For every digit guessed correctly in the correct place is a \"bull\".")
    print ("For every digit guessed correctly in the wrong place is a \"cow\".")
    print ("If you want to quit the game, type \"exit\".")
    guesses = 0
    while play:
        guess = input("Enter a 4-digit number: ")
        if guess.lower() == "exit":
            break
        cowbullcount = compare_numbers(number, guess)
        guesses += 1
        
        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
        
        if cowbullcount[1] == 4:
            play = False
            print("You win the game after " + str(guesses) + " tries! The number was "+str(num), ".")
            break
        else:
            print("Your guess isn't quite right, try again.")
            