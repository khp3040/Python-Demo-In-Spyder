# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:22:08 2021

@author: KshitijPawar
"""

order1 =['Iphone', 'RedMi','Oppo','Nokia','OnePlus','RealMe','Samsung']

# print(sorted(order1,key=lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]

print(last_name('samsung'))