# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:09:17 2021

@author: 0014CR744
"""

class Cart():
    
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
            
