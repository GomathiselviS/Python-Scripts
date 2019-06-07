# -*- coding: utf-8 -*-
"""
SPY GAME: Write a function that takes in a list of integers
 and returns True if it contains 007 in order

@author: atg
"""
def spy_game(nums):
    if nums.count(0) != 2 and 7 not in nums:
        return False
    pos7=nums.index(7)
    pos0=[]
    i=0
    for n in nums:
        if n==0:
            pos0.append(i)
        i=i+1
    print (pos0)
    if pos0[0] < pos7 and pos0[1] < pos7:
        return True
    else:
        return False
    
r1=spy_game([1,2,4,0,0,7,5])
r2=spy_game([1,0,2,4,0,5,7])
r3=spy_game([1,7,2,0,4,5,0])

print(r1,r2,r3)
    
