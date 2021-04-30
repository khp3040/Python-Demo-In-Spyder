# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:12:01 2021

@author: MathiyalaganN
"""
from test2 import MyClass
instance = MyClass()
"""
print(instance('ibm.com'))
print(instance.__call__('google.com'))
print(instance._cache)
"""
print(instance('ibm.com'))

print(instance.has_host('ibm.com'))

instance.clear()

print(instance.has_host('ibm.com'))

"""
def myFunc():
    print('Hello')
    
from test2 import MyClass
print(MyClass)
print(myFunc)
instance = MyClass()
"""





