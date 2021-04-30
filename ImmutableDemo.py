# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:58:05 2021

@author: KshitijPawar
"""

def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
        
    return cls
#seq = sequence_class(immutable = True)
seq = sequence_class(immutable = False)

t = seq('pyton3')

print(t)

print(type(t))