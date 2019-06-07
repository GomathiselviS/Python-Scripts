# -*- coding: utf-8 -*-
"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶

@author: atg
"""

def blackjack(a,b,c):
    result=a+b+c
    if result >=21 and 11 in [a,b,c]:
        result=result-10
    if result >= 21:
        return "BUST"
    else:
        return result

r1=blackjack(5,6,7)
print(r1)
r2=blackjack(9,9,9)
print(r2)
r3=blackjack(9,9,11)
print(r3)



