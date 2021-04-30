# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:29:16 2021

@author: MathiyalaganN

nodejs fs asynchronous operation

open()

open a file for reading or writing

file:path to the file (required)
mode:read, write, or append, binary or text

encoding: encoding to use i text mode
"""

def myFunctionGenerator(n):
    for x in range(n):
        yield x*4
        
gen = myFunctionGenerator(3)
print(next(gen))
print(next(gen))
print(next(gen))

