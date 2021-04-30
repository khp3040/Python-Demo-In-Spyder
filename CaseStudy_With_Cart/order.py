# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:10:14 2021

@author: 0014CR744
"""

class Order():
    
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
            
    def updateOrder(orderList,Quantity,productPrice):
        orderList.append(Quantity)
        orderList.append(productPrice)
        return orderList