#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

import math

def caesar(message):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_msg = ""
    for i in range(len(message)):
        curr_fib = int((pow(1+math.sqrt(5),i) - pow(1-math.sqrt(5),i))/(pow(2,i)*math.sqrt(5)))
        if message[i].isalpha():
            new_msg += alph[(alph.index(message[i])-curr_fib)%26]
        else:
            new_msg += message[i]
        print(curr_fib)
    return new_msg
