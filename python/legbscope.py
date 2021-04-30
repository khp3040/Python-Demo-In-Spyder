# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:49:52 2021

@author: MathiyalaganN
"""

g = 'global'

def outer (p='param'):
    l = 'local'
    def inner():
        
        print(g, p, l)
    inner()
      
outer()   
"""
outer.inner()"""
"""There is no attribute 'inner' """

"""
In Javascript
var myFunc(){
var date = new Date()
setTimeout(function(){
    console.log(date)
    },10000)
    }
"""