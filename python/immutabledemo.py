# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:58:50 2021

@author: MathiyalaganN
"""
"""
def sequence_class(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls

seq =sequence_class(immutable = False)

t = seq ('python3')

print(t)

print(type(t))
"""
def sequence_class(immutable):
    
    return tuple if immutable else list

seq =sequence_class(immutable = True)

t = seq ('python3')

print(t)

print(type(t))