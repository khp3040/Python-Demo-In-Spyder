# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:49:41 2021

@author: KshitijPawar
"""

# =============================================================================
# def hyperVolume(*args):
#     print(args)
#     print(type(args))
#hyperVolume(6,7)
# =============================================================================

# =============================================================================
# def hyperVolume(*args):
#     i = iter(args)
#     v = next(i)
#     for args in i:
#         v *= args
#     return v
# 
# 
# print(hyperVolume(1,2,3,4))
# print(hyperVolume(8,9))
# 
# =============================================================================

# =============================================================================
# def tag(name, **kwargs):
#     print(name)
#     print(kwargs)
#     print(type(kwargs))
#     
# tag('img', src='ibm.jpg',alt='IBM Employee')
# =============================================================================


def tag(name, **kwargs):
    result = '<'+name 
    for key, value in kwargs.items():
        result += '{k} = {v} '.format(k=key,v=str(value))
    result += '>' 
    return result

print(tag('img ', src ='ibm.jpg',alt ='IBM Employee'))
