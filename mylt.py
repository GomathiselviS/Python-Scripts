# -*- coding: utf-8 -*-
"""
Write a Python function to multiply all the numbers in a list.



@author: atg
"""

def multiply(lst):
    m=1
    for ele in lst:
        m=m*ele
    return m

print(multiply([1,2,3,-4]))


