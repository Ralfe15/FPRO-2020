#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

import math
def time_until_lost_connection(direction_A, direction_B):
    max_distance = 35 #km
    speed = 5 #km/h
    angle = abs(direction_B-direction_A)
    aux_angle = (180 - angle)/2
    if aux_angle == 0:
        return ((max_distance/2)/5)*60
    
    sin_angle = math.sin(math.radians(angle))
    sin_aux_angle = math.sin(math.radians(aux_angle))
    
    walked_dist = (35*sin_aux_angle)/sin_angle
    time_walked = (walked_dist/5)*60
    return round(time_walked, 3)