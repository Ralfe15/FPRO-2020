#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def isPrime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
            break
    else:
        return True
    
lower = int(input())
upper = int(input())
final = "Prime numbers between {} and {} are: ".format(str(lower),str(upper))
for i in range(lower, upper+1):
    if isPrime(i):
        final += "{} ".format(str(i))
print(final.strip())
