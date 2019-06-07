# -*- coding: utf-8 -*-
"""
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

@author: atg
"""

def has_33(args):
    loc=args.index(3)
    if args[loc+1] == 3:
        return True
    else:
        return False
    
r1=has_33([1, 3, 3]) 
r2=has_33([1, 3, 1, 3]) 
r3=has_33([3, 1, 3])

print(r1,r2,r3)
