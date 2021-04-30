# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:08:01 2021

@author: 0014CR744
"""
class Price():
    
    def calculateProductPrice(Quantity,orderList):
        
        try:
            productPrice = Quantity * int(orderList[0]['price'])
            print("Price : ", productPrice)
            return productPrice
        except TypeError:
            pass