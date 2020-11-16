#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def ugly(number):
    if number < 1:
        return False
    while True:
        if number % 2 == 0:
            number /= 2
        elif number % 3 == 0:
            number /= 3
        elif number % 5 == 0:
            number /= 5
        elif number != 1:
            return False
        else:
            return True