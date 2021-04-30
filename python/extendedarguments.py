# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:49:11 2021

@author: MathiyalaganN

extended arguments syntax

Arbitrary number of positional arguments

arbitrary keyword arguments

Position only and keyword arguments
"""
print("One","Two",'Three',4,5,67,89)

print("{a}<====>{b}".format(a="IBM",b="India"))

"""
def hyperVolume(*args):
    print(args)
    print(type(args))
 """  
 
"""
 Rules for *args
 1.must come after positional arguments
2.only collects positional arguments
"""
 
def hyperVolume(*args):
    i = iter(args)
    v = next(i)
    for args in i:
        v *=args
    return v    
        
        
print(hyperVolume(2))
print(hyperVolume(2,3))
print(hyperVolume(2,3,4))
print(hyperVolume(2,3,4,5))

"""
Arbitrary keyword Arguments
Prefix with **

conventionally called as **kwargs  (keywordargs)
"""
"""
def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))
"""    
    
def tag(name, **kwargs):
   result = '<'+name
   for key, value in kwargs.items():
       result += ' {k}={v}'.format(k=key, v=str(value))
   result +='>'
   return result
   
print(tag('img',src='ibm.jpg',alt='IBMIndia'))
    
tag('img',src='ibm.jpg',alt='IBMIndia')