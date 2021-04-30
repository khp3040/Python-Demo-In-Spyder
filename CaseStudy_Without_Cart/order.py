# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:15:45 2021

@author: KshitijPawar
"""
class Order():

    def placeOrder(slist):
        
        try:
             brandName = str(input("Enter Brand Name : "))
             order = list(filter(lambda i: i.get("brand") == brandName,slist))

             if len(order) == 0:    
                 print("Invalid brand name")
        
             else:
                 try:          
                     productQnt = int(input("enter quantity : "))
                        
                     if productQnt <= 0:
                         raise ValueError()
                                         
                     elif productQnt <= int(order[0]["stockAvailable"]):
                         print("total price : ",productQnt *int(order[0]["price"]))
                            
                     else:
                         print("stock unavailable") 
           
                 except ValueError:
                     print("Please Enter A Positive Integer ")
           
        except ValueError:
            pass   

# p = Product.productRepository()
# s = Search.search(p)
# Search.displayBrand(s)
# Order.placeOrder(s)