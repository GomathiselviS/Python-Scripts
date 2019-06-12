# -*- coding: utf-8 -*-
"""
Write a Python function that accepts a string and calculates the number 
of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

@author: atg
"""

def up_low(s):
    isup=0
    islow=0
    sent=''.join(s.split())
    for c in sent:
       
        if c.isupper():
            isup=isup+1
        elif c.islower():
            
            islow=islow+1
        else:
            continue
    result_list=[isup,islow]
    return result_list

input_str='Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(input_str))

