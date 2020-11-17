#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:02:15 2020

@author: rafael
"""

def count_until(tup):
    for i in range(len(tup)):
        if type(tup[i]) == tuple:
            return i
    return -1