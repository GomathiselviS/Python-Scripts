# -*- coding: utf-8 -*-
"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

@author: atg
"""

def old_macdonald(name):
    name1=name.capitalize()
    name2=""
    i=0
    for c in name1:
        if i==3:
            c=c.upper()
        name2=name2+c
        i=i+1
    return name2


result=old_macdonald("macccccc")
print(result)


