#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def collatz(n):
    if n == 1:
        return '1'
    seq = ""
    tmp = n
    while tmp != 1:
        seq += str(tmp) + ","
        if tmp % 2 == 0:
            tmp = int(tmp/2)
        else:
            tmp = int((tmp*3)+1)
    seq += "1"
    return seq
