# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:45:01 2019

@author: Kasia
"""

def reverse(text):
    splitting = text.split()
    return " ".join(reversed(splitting))

sentence = input("Write a long string containing multiple words: ")
print (reverse(sentence))

def reverseWord(w):
  return ' '.join(w.split()[::-1])

print (reverseWord(sentence))

