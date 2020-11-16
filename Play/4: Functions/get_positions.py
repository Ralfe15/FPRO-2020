#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:54:12 2020

@author: rafael
"""

def get_positions(sentence, word_list):
    res = ""
    for word in sentence.split():
        if word in word_list:
            res += "{} ".format(str(word_list.index(word)))
        else:
            return ""
    return res[:-1]
