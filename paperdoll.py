# -*- coding: utf-8 -*-
"""
PAPER DOLL: Given a string, return a string where for every 
character in the original there are three characters
@author: atg
"""

def paper_doll(text):
    return_text=""
    for t in text:
        return_text=return_text+t+t+t
    return return_text

r1=paper_doll('Hello')
print(r1)
r2=paper_doll('Mississippi')
print(r2)



