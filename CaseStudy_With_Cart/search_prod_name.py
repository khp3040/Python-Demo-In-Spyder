# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:59:49 2021

@author: 0014CR744
"""

class Search():
    def name(productList): 
        productName = str(input("Enter Product Name : "))
        searchList = list(filter(lambda i: i.get("name") == productName,productList))
        return searchList
            
    def displayBrand(searchList):
        try:
            if(len(searchList) == 0):
                raise ValueError()
            else:
                for i in range(0,len(searchList)):
                    print(f"Brand : { searchList[i]['brand']} | Price : { searchList[i]['price']}")
               
        except ValueError:
                print("Product not available")