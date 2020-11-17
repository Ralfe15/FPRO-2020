#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:02:15 2020

@author: rafael
"""

def count_chars(a_string):
    ch = 0
    num = 0
    symb = 0
    for i in a_string:
        if i.isalpha():
            ch+=1
        elif i.isdigit():
            num+=1
        else:
            symb+=1
    return(ch,num,symb)