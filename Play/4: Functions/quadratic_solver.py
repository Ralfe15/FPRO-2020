#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

import math

def solver(a,b,c):
    l = []
    delta = b**2-4*a*c
    if delta < 0:
        return l
    elif delta == 0:
        l.append(-b/(2*a))
        return l
    else:
        l.append((-b+(math.sqrt(delta)))/(2*a))
        l.append((-b-(math.sqrt(delta)))/(2*a))
        l.sort()
        return l
