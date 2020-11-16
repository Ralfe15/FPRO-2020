#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

solution = float(input()) 
n = solution # upper bound
m = 0 # lower bound
midpoint = (n+m)/2
while midpoint*midpoint != n and round(n,5) != round(m,5):
    if midpoint*midpoint > solution:
        n = midpoint
    elif midpoint*midpoint  < solution:
        m = midpoint
    midpoint = (m+n)/2
print(round(midpoint,5))