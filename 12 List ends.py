# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:57:37 2019

@author: Kasia
"""
import random

def list_ends (number):
    return int(input(number))

list_range = list_ends("Provide the range of list: ")
items = list_ends("How many items should list contain: ")
created_list = random.sample(range(list_range), items)
new_list = [x for x in created_list if x == created_list[0] or x == created_list[-1]]    

print (created_list)
print (new_list)
