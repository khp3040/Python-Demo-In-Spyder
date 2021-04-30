# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:36:52 2021

@author: KshitijPawar
"""

# =============================================================================
# def sort_by_last_name(*strings):
#     
#     def last_letter(s):
#         return s[-1];
#     print(last_letter)
#     return sorted(strings,key=last_letter)
# 
# print(sort_by_last_name("hello","i","am","a","local","function"))
# 
# =============================================================================

def enclosing():
    x=56667.98
    def local_func():
        print(x)
    return local_func

lf = enclosing()
lf()

print(lf.__closure__)