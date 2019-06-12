# -*- coding: utf-8 -*-
"""
Write a Python function that checks whether a passed 
in string is palindrome or not.
@author: atg
"""

def palindrome(s):
    palin_str=s[::-1]
    if s==palin_str:
        return True
    else:
        return False
    

print(palindrome('hellleh'))