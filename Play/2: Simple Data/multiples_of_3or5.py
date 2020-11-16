#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def sum_multiples(n):
    s = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s