# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 09:31:57 2021

@author: KshitijPawar
"""
from MySystem import System

# p = System.productRepository()
# s = System.search(p)
# System.displayBrand(s)
# b = System.chooseBrand()
# o = System.selectBrand(b,s)
# vo = System.verifyBrand(o)
# q = System.Quantity()
# vq = System.verifyQuantity(q,vo)
# pr = System.calculateProductPrice(q, vo)
# ct = System.createCart()
# act = System.addToCart(vo,q,pr,ct)
# System.displayCart(act)
# System.placeOrder(act)

class Main():
    def Sys():
        p = System.productRepository()
        ct = System.createCart()
        try:
            ch1 = input("Do you wish to search Product(y/n) :")
            if ch1 == 'y':
                while ch1 == 'y':
                    s = System.search(p)
                    System.displayBrand(s)
               
                    if len(s) !=0:
                        b = System.chooseBrand()
                        o = System.selectBrand(b,s)
                        vo = System.verifyBrand(o)
                    else:
                        raise TypeError()
                
                    if len(vo) != 0:
                        q = System.Quantity()
                        vq = System.verifyQuantity(q,vo)
                    else:
                        raise TypeError()
                
                    if vq == True:
                        pr = System.calculateProductPrice(q, vo)
                        uo = System.updateOrder(vo,q,pr)
                        #ct = System.createCart()
                        act = System.addToCart(ct,uo)
                        #print(act)
                    else:
                        raise  TypeError()
                    
                    ch2 = input("Do you want to search again (y/n): ")
                    if ch2 == 'y':
                        pass
                    elif ch2 == 'n':
                        break
                    else:
                        raise TypeError()
               

                if len(act) != 0:
                    ch3  = input("Do you want to see your cart(y/n): ")
                    if ch3 == 'y':
                        System.displayCart(act)
                        if len(act) != 0:
                            while True:
                                ch4 = input("Do you wish to remove Products from your cart(y/n): ")
                                if ch4 == 'y':
                                    act = System.removeFromCart(act)
                                    System.displayCart(act)
                                elif ch4 == 'n':
                                    System.placeOrder(act)
                                    break
                                else:
                                    raise ValueError()
                                    break
                                
                        
                    
                    elif ch3 =='n':
                        print("Thankyou for visiting")
                    else:
                        raise ValueError()
                else:
                    raise TypeError()

            elif ch1 == 'n':
                 print("Thanks For Visiting")
            else:
                 raise ValueError() 
         
                
         
                
        except ValueError:
            print("Incorrect Choice")
        except TypeError:
            pass
        except UnboundLocalError:
            pass
        
Main.Sys()