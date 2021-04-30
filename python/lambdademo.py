# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:16:44 2021

@author: MathiyalaganN
"""

orders1 = ['Iphone 12','oneplus Pro','Samsung Galaxy']

"""
print(sorted(orders1,key = lambda name: name.split()[-1]))
"""
last_name = lambda name: name.split()[-1]

print(last_name('Samsung Galaxy'))

def my_last_name(name):
    return name.split()[-1]

"""
Function vs lambda

def name(args): body   lambda args1,args2:expr
"""