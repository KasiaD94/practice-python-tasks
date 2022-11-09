# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:59:33 2019

@author: Kasia
"""
import numpy

game = [[2,2,1],
        [2,1,2],
        [2,1,1]]
        
def check_row(game):
    for i in range(3):
        set_row = set(game[i])
        if len(set_row) == 1 and game[[i][0]] != 0:
            return game[i][0]
    return 0

def check_col(game):
    trans = numpy.transpose(game)
    for i in range(3):
        set_col = set(trans[i])
        if len(set_col) == 1 and trans[i][0] != 0:
            return trans[i][0]
    return 0

def check_diagonal(game):
    if game[1][1] != 0:
        if game[0][0] == game[1][1] == game[2][2]:
            return game[1][1]
        if game[0][2] == game[1][1] == game[2][0]:
            return game[1][1]
    return 0

if check_row(game) > 0:
    print(str(check_row(game)) + str(" row wins!"))
    
if check_col(game) > 0:
    print(str(check_col(game)) + str(" column wins!"))
    
if check_diagonal(game) > 0:
    print(str(check_diagonal(game)) + str(" diagonal wins!"))
    