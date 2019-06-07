# -*- coding: utf-8 -*-
"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

@author: atg
"""

def almost_there(num):
    if abs(num-100) <= 10 or abs(num-200) <= 10:
        return True
    else:
        return False



r1=almost_there(90) 
r2=almost_there(104) 
r3=almost_there(150) 
r4=almost_there(209) 

print(r1,r2,r3,r4)

