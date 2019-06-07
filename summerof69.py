# -*- coding: utf-8 -*-
"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting 
with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9). Return 0 for no numbers.

@author: atg
"""

def summer_69(arr):
    pos6=""
    pos9=""
    if 6 in arr:
        pos6=arr.index(6)
        if 9 in arr:
            pos9=arr.index(9)
    s=0
    for num in arr:
        
        if pos6 != "" and pos9 != "" and arr.index(num) >= pos6 and arr.index(num) <= pos9:
            continue
        s=s+num
    return s

r1=summer_69([6, 3, 9])
r2=summer_69([4, 5, 6, 7, 8, 9])
r3=summer_69([2, 1, 6, 9, 11])
print(r1,r2,r3)