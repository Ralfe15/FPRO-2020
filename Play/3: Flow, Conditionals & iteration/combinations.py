#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

def C(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))