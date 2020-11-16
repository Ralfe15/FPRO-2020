#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

distance = int(input())
fuel_with_100 = float(input())
price = float(input())

print(round(((distance*fuel_with_100)/100)*price,2))