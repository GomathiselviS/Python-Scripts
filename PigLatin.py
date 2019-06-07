# -*- coding: utf-8 -*-
"""
Pig Latin

@author: GomathiS
"""
def vowel_check(word):
    vowels=['a','e','i','o','u']
    if word[0] in vowels:
        return True
            
def pig_latin(word):
    if not vowel_check(word):
        new_word1=word[1:]
        new_word2=new_word1+word[0]+'ay'
    else:
        new_word2=word+'ay'
        
    return new_word2

result=pig_latin('apple')
print("Apple-> "+result)
result=pig_latin('grapes')
print("grapes-> "+result)
        
        
    

