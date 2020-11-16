#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

hour = int(input()) + 6
minute = int(input()) + 51

if minute >= 60:
    minute -= 60
    hour += 1
if hour > 24:
    hour -= 24
print("{}:{}".format(str(hour).zfill(2), str(minute).zfill(2)))