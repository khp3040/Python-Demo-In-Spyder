# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:48:13 2021

@author: KshitijPawar
"""
g='global'

def outer(p = 'Parameter'):
    l = 'local'
    def inner():  
        print(g,p,l)
    
    inner()
    
outer()