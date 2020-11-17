#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:02:15 2020

@author: rafael
"""

def repeated_letter(s):
    for i in range(len(s)):
        if s[i] in s[:i]+s[i+1:]:
            return s[i]
    return None