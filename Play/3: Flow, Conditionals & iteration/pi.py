#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

from math import factorial, sqrt

k = 50
result_somatorio = 0
for k in range(k+1):
    result_somatorio += (factorial(4*k)*(1103+26390*k))/(pow(factorial(k),4)*pow(396,4*k))
result = ((2*sqrt(2))/9801)*result_somatorio
print(round(pow(result,-1),8))