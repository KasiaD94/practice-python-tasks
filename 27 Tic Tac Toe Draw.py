# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:34:20 2019

@author: Kasia
"""

import numpy

gameboard = [(["-"]*3) for i in range(3)]
turn = 1
row_col = [0]

def check_input(values):
	# input has only two values
    if len(values) != 2:
        print ("Input must be two numbers in format row,col e.g.  1,2 ")
        return 0
    # input is a number between 1 and 3 (inclusive)
    try:
        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
            # checks if the position on the board is alreay filled
            if gameboard[int(values[0])-1][int(values[1])-1] != '-':
                print ("Position on board already taken.")
                return 0
            return 1
        else:
            print ("Input values must be numbers between 1 and 3 (inclusive)")
            return 0
    except ValueError:
        print ("Input values must be numbers between 1 and 3 (inclusive)")
        return 0
    
#draw a gameboard with new positions X and O 
def draw_board(value, player):
    #assign input values to position on gameboard 
    gameboard[(int(value[0]))-1][(int(value[1]))-1] = player
    
    #print new gameboard
    for row in gameboard:
        print(row)
        
#check if game is over(winner or no more empty posiotions)
def game_over():
    sign = "-"
    
    #check win by row
    for i in range(3):
        if len(set(gameboard[i])) == 1:
            if gameboard[i][1] == "-":
                continue
            elif gameboard[i][1] == "X":
                print("Game over - player 1 has won.")
            else:
                print("Game over - player 2 has won.")
            return 1
    
    #check win by col
    for i in range(3):
        if len(set(numpy.transpose(gameboard[i]))) == 1:
            if gameboard[0][i] == "-":
                continue
            elif gameboard[0][i] == "X":
                print("Game over - player 1 has won.")
            else:
                print("Game over - player 2 has won.")
            return 1
        
    #check win by diagonal
    if gameboard[1][1] != "-":
        if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]) or (gameboard[0][2] == gameboard[1][1] == gameboard[2][0]):
            if gameboard[0][0] == "X":
                print("Game over - player 1 has won.")
            else:
                print("Game over - player 2 has won.")
            return 1
    
    #check if board is full
    for row in gameboard:
        if sign in row:
            return 0
    print("Game over - board is full.")
    return 1

#check if the board is not full
while not game_over():
    sign = "-"
    
    #check correctness of input data
    while not check_input(row_col):
        player = turn % 2
        if player == 0:
            player = 2
            sign = 'O'
        else:
            sign = 'X'
        user_input = input("Player " + str(player) + " input: ")
        row_col = user_input.strip().split(",")
        
        #draws board with user input
        draw_board(row_col, sign)
        
        row_col = [0]
        turn += 1
        

