#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:02:15 2020

@author: rafael
"""

def palindrome_index(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        tmp = s[:i]+s[i+1:]
        if tmp == tmp[::-1]:
            return i
    return -1
    