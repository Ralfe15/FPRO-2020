#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

import math

le = int(input())
re = int(input())
pe = int(input())
te = int(input())

if le > 100 or le < 0 or re > 100 or re < 0 or pe > 100 or pe < 0 or te > 100 or te < 0:
    print("Input error")
elif pe < 40 or te < 40:
    print("RFC")
else:
    grade = (le+re+(5*pe)+(3*te))/50
    if grade-int(grade) == 0.5:
        print(math.ceil(grade))
    else:
        print(round(grade))