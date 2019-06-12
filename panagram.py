# -*- coding: utf-8 -*-
"""
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing 
every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
@author: atg
"""
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    check_str=(''.join(str1.split())).lower()
    print(check_str)
    for c in alphabet:
        if c not in check_str:
            print(c)
            return False
    return True
        
str1="The quick brown fox jumps over the lazy dog"
print(ispangram(str1))