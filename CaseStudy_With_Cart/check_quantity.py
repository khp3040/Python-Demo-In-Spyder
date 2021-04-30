# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:05:15 2021

@author: 0014CR744
"""

class Quantity():
    def quantity():
        try:
            quant = int(input("Enter Quantity you wish to purchase : "))
            return quant
        except  ValueError:
            print("Please enter a number and not a string")
    
    def verifyQuantity(quant,orderList):
        try:
            if quant <= 0:
                raise ValueError()
            elif quant <= int(orderList[0]["stockAvailable"]):
                 return True
                 
            elif quant > int(orderList[0]["stockAvailable"]):
                print("Stock Unavailable")      
            else:
                raise ValueError()
        except ValueError:
            print("Please Enter Positive Integer")
        except TypeError:
            pass