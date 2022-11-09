# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:47:13 2019

@author: Kasia
"""
import collections


with open('names.txt', 'r') as open_file:
    all_text = open_file.read()
    
list_names = list(all_text.split('\n'))
    
counter = collections.Counter(list_names)
print (counter)

for pair in counter.items():
    print(pair)
   