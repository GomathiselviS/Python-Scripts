# -*- coding: utf-8 -*-
"""
LESSER OF TWO EVENS: Write a function that returns the lesser of\
 two given numbers if both numbers are even, but returns the greater if one 
 or both numbers are odd

@author: atg
"""
def lesser_or_greater(a,b):
    if a%2==0 and b%2==0:
        return a if a<b else b
    else:
        return b if a<b else a

result=lesser_or_greater(110,6)
    
print(result)