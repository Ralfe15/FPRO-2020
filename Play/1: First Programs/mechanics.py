#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)
speed = 18
g = 10

horizontal_speed = (speed*cos_angle) #horizontal component of vector speed
time_in_air = (2*speed*sin_angle)/g

print(str(round(horizontal_speed*time_in_air)))