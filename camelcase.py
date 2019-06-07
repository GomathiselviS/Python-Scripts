# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:25:12 2019

@author: atg
"""

def myfunc(word):
    result_str=""
    i=0
    for c in word:
        if i%2==0:
            result_str=result_str+c.upper()
        else:
            result_str=result_str+c
        i=i+1
    return result_str

print(myfunc("gjkjjk;lm.lmlkgf"))