#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

distance = 313
hours = int(input())
minutes = int(input())

total_time = hours+((minutes)/60)
average_vel = distance/total_time

print(round(average_vel))