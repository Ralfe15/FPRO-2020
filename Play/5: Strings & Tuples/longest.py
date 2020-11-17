#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:02:15 2020

@author: rafael
"""

def longest(s):
    l = [len(word) for word in s.split()]
    return max(l)