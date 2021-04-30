# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:21:06 2021

@author: KshitijPawar
"""

def escape_unicode(f):
    def wrap(*args,**kwargs):
        x= f(*args,**kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def my_func():
    return 'æl̥Jṅ!@#QāZsṣErty.|":~'

print(my_func())