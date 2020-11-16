#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def greatest(num):
    num = str(num)
    greatest = ""
    g_digit = 0
    while num!= "":
        g_digit = 0
        for i in num:
            if int(i) >= g_digit:
                g_digit = int(i)
        greatest+=str(g_digit)
        num = num.replace(str(g_digit), "", 1)
    return int(greatest)
