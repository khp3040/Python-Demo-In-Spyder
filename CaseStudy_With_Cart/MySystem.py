# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:39:09 2021

@author: KshitijPawar
"""

import csv
#from functools import reduce

class System():

    def productRepository():
        filename = 'ProductsCsv.txt'
        productList = []
        with open(filename, 'r') as data:
            for line in csv.DictReader(data):
                productList.append(line)
                #print(line)
            #print(self.productList)   
        return productList
               
    def search(productList): 
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
    
    def Quantity():
        try:
            Quantity = int(input("Enter Quantity you wish to purchase : "))
            return Quantity
        except  ValueError:
            print("Please enter a number and not a string")
    
    def verifyQuantity(Quantity,orderList):
        try:
            if Quantity <= 0:
                raise ValueError()
            elif Quantity <= int(orderList[0]["stockAvailable"]):
                 return True
                 
            elif Quantity > int(orderList[0]["stockAvailable"]):
                print("Stock Unavailable")      
            else:
                raise ValueError()
        except ValueError:
            print("Please Enter Positive Integer")
        except TypeError:
            pass
        
    def calculateProductPrice(Quantity,orderList):
        try:
            productPrice = Quantity * int(orderList[0]['price'])
            print("Price : ", productPrice)
            return productPrice
        except TypeError:
            pass
     
    def updateOrder(orderList,Quantity,productPrice):
        orderList.append(Quantity)
        orderList.append(productPrice)
        return orderList
        
        
    def createCart():
        cart = []
        return cart

    def addToCart(cart,orderList):
        try:
            ch = input("Do you wish to add to cart (y/n) : ")
            if ch == 'y':  
                cart.append(orderList)
                #print(cart)
                return cart
            elif ch == 'n':
                print("Thankyou for visiting")
            else:
                raise ValueError()
        except ValueError:
            print("Invalid Choice")
            
    def displayCart(cart):
        try:
            if len(cart) == 0:
                print("Your Cart is Empty")
            else:
                print("Your Cart Details")
                for i in range(len(cart)):
                    print("--------------------------------------")
                    print(f"Item {i+1}")
                    #print("Product Code: ", cart[i][0]['code']) 
                    print("Product: ", cart[i][0]['name']) 
                    print("Brand: ", cart[i][0]['brand'])
                    print("Quantity: ", cart[i][1])
                    print("Price: ", cart[i][2])
                    print("--------------------------------------")
           
        except TypeError:
            pass

    def removeFromCart(cart):
        try:
            ch1 = int(input('Enter Item number you want to remove: '))
            cart.pop((ch1 - 1))
            return cart
        except ValueError:
                    print("Please Enter Correct Item number")
        except TypeError:
                    print("Please Enter a Integer Value")
        except IndexError:
                    print("Invalid Item Number")
                    return cart
    
    def placeOrder(cart): 
        try:
            ch = input("Do you wish to place order(y/n): ")
        
            if ch =='y':
                if len(cart) == 0:
                    print("You Cannot Place Order Since your Cart is Empty")
                    print("Thankyou for visiting")
                    
                else:
                    TotalOrderPrice = 0
                    for i in range(len(cart)):
                        TotalOrderPrice += int(cart[i][2])      
                    print("Total Price of all Products: ", TotalOrderPrice)
                    return TotalOrderPrice
            elif ch == 'n':
                print("Thankyou for visiting")
            else:
                raise ValueError()
        except ValueError:
            print("Invalid Choice")
  
# p = System.productRepository()
# s = System.search(p)
# System.displayBrand(s)
# b = System.chooseBrand()
# o = System.selectBrand(b,s)
# vo = System.verifyBrand(o)
# q = System.Quantity()
# vq = System.verifyQuantity(q,vo)
# pr = System.calculateProductPrice(vq, vo)
# ct = System.createCart()
# act = System.addToCart(vo,vq,pr,ct)
# System.displayCart(act)
# System.placeOrder(act)