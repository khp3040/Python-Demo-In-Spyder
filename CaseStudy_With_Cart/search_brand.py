# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:03:00 2021

@author: 0014CR744
"""
class Brand():
    def chooseBrand():
        brandName = str(input("Enter Brand you wish to purchase : "))
        return brandName
            
    def selectBrand(brandName,searchList):
        orderList = list(filter(lambda brand: brand.get("brand") == brandName,searchList))
        return orderList
    
    def verifyBrand(orderList):     
        if len(orderList) == 0:    
            print("Invalid Brand Name ")
        else:
            return orderList