#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

n = input()
if len(n) == 1:
    print('Looping number')
else:
    for i in range(len(n)-1):
        if n[i] == '9' and n[i+1] == '0':
            continue
        if int(n[i])+1 != int(n[i+1]):
            print('Not a looping number')
            break
    else:
        print('Looping number')