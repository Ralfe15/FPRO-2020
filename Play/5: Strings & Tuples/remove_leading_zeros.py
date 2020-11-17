#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:02:15 2020

@author: rafael
"""

def remove_leading(ip):
    return ".".join([str(int(i)) for i in ip.split(".")])