# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:42:13 2019

@author: Kasia
"""

import random


def check (your_number, your_list):
    
    # Create list
    if your_number in your_list:
        return True
    
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l:
        mid = int(l + (r - l)/2)
        print("l ", l)
        print("r ", r)
        print("mid ", mid)
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

if __name__ == "__main__":
    
    list_range = int(input("Provide the range of list: "))
    items = int(input("How many items should list contain: "))
    created_list = sorted(random.sample(range(list_range), items))
    print(created_list)

    number = int(input("Provide the number which will be checked if in the list: "))
        
    result = binarySearch(created_list, 0, len(created_list), number)
    if result != -1:
        print("Using binarySearch: Number is on the list with index %d." % result)
    else: 
        print("Using binarySearch: The number is not in the list.")

"""    if check(number, created_list) == True:
        print("Using check: The number is in the list.")
    else:
        print("Using check: The number is not in the list")"""