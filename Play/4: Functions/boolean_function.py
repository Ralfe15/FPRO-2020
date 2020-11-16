#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def validate(grade):
    return((type(grade) == int or type(grade) == float) and (grade>=0 and grade <=100))
