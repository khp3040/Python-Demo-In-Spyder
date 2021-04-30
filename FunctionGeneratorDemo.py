# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:31:34 2021

@author: KshitijPawar
"""

def myFuncGenerator(n):
    for x in range(n):
        yield x*4
        
gen = myFuncGenerator(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) #Stops or Yields
print(next(gen))
print(next(gen))
