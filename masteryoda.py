# -*- coding: utf-8 -*-
"""
MASTER YODA: Given a sentence, return a sentence with the words reversed

@author: atg
"""

def master_yoda(text):
    text_list=text.split()
    text_reverse_list=text_list[::-1]
    text_reverse=' '.join(text_reverse_list)
    return text_reverse

result1=master_yoda('I am home')
result2=master_yoda('We are ready')

print(result1,result2)

