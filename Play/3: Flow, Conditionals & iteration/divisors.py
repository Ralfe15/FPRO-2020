#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

n = int(input())
s = 0
for i in range(1,n+1):
    if n%i==0:
        s+=i
print(s)