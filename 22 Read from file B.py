# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:01:53 2019

@author: Kasia
"""

import collections

with open('images.txt', 'r') as open_file:
    all_text = open_file.read()
 
list_images = list(all_text)

replace = all_text.replace('\n', '_')
list_images = list(replace.split('_'))
print(list_images)
    
counter = collections.Counter(list_images)
print (counter)
