#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

a = int(input())
b = int(input())

print(((a+b)*2)*((a-b)%2==0) + (((a-b)%2)!=0) * ((a+b)+(a*b)))