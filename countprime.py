# -*- coding: utf-8 -*-
"""
COUNT PRIMES: Write a function that returns the number of prime numbers
 that exist up to and including a given number

@author: atg
"""

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        print("in while for {}".format(x))
        for y in range(3,x,2):
            print("---",end="")# test all odd factors up to x-1
            print(x,y)
            if x%y == 0:
                print(x,y)
                x += 2
                break
        else:
            print("Appending {}".format(x))
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(10))