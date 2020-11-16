#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

value = int(input())
recieved = int(input())
change = recieved-value
control=0
str_final = ""
values = [50, 20, 10, 5]
for i in values:
    while change >= i:
        control+=1
        change-=i
    str_final += "{} ".format(str(control))
    control = 0
print(str_final[:-1])