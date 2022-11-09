# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:24:03 2019

@author: Kasia
"""

import random

a = random.sample(range(40),15)
b = random.sample(range(40),18)

print([c for c in a if c in b])