# -*- coding: utf-8 -*-
"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both 
words begin with same letter

@author: atg
"""
def animal_crackers(animal):
    check=animal.upper().split()
    
    if check[0][0]==check[1][0]:
        return True
    else:
        return False

result1=animal_crackers('Levelheaded JLlama') 
result2=animal_crackers('crazy CKangaroo') 
print(result1)
print(result2)

