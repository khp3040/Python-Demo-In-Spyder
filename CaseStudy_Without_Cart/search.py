# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:15:45 2021

@author: KshitijPawar
"""
class Search():
    
    def search(plist): 
        #p = Product.productRepository()
        productName = str(input("Enter product name : "))
        psearch = list(filter(lambda i: i.get("name") == productName,
                                   plist))
        #print(self.psearch)
        return psearch
            
    def displayBrand(psearch):
         try:
          
            if(len(psearch) == 0):
                raise ValueError()
            
            for i in range(0,len(psearch)):
                print(f"Brand : { psearch[i]['brand']} | Price : { psearch[i]['price']}")
               
            # return search()
         except ValueError:
            print("Product not available")
         
# p = Product.productRepository()
# s = Search.search(p)
# Search.displayBrand(s)