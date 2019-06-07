# -*- coding: utf-8 -*-
"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
 or if one of the integers is 20. If not, return False
@author: atg
"""


def makes_twenty(a,b):
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False
    
r1=makes_twenty(20,10)
r2=makes_twenty(12,8)
r3=makes_twenty(2,3)
r4=makes_twenty(20,20)

print(r1,r2,r3,r4)
