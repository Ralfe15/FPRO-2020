#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def dogs(h_age):
    d_age = 0
    for i in range(0, h_age):
        if i < 2:
            d_age+=10.5
        else:
            d_age+=4
    return d_age
