# -*- coding: utf-8 -*-
"""
Write a Python function that takes a list and returns a new list with unique\
 elements of the first list.

@author: atg
"""

def unique_list(lst):
    s=set(lst)
    return list(s)

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))