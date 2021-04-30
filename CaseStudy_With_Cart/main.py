# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 18:11:33 2021

@author: 0014CR744
"""
from prod_repo import Product
from search_prod_name import Search
from search_brand import Brand
from check_quantity import Quantity
from price import Price
from cart import Cart
from order import  Order


class Main():
    def Sys():
        p = Product.productRepository()
        ct = Cart.createCart()
        try:
            ch1 = input("Do you wish to search Product(y/n): ")
            if ch1 == 'y':
                while ch1 == 'y':
                    s = Search.name(p)
                    Search.displayBrand(s)
               
                    if len(s) !=0:
                        b = Brand.chooseBrand()
                        o = Brand.selectBrand(b,s)
                        vo = Brand.verifyBrand(o)
                    else:
                        raise TypeError()
                
                    if len(vo) != 0:
                        q = Quantity.quantity()
                        vq = Quantity.verifyQuantity(q,vo)
                    else:
                        raise TypeError()
                
                    if vq == True:
                        pr = Price.calculateProductPrice(q, vo)
                        uo = Order.updateOrder(vo,q,pr)
                        act = Cart.addToCart(ct,uo)
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
                        Cart.displayCart(act)
                        if len(act) != 0:
                            while True:
                                ch4 = input("Do you wish to remove Products from your cart(y/n): ")
                                if ch4 == 'y':
                                    act = Cart.removeFromCart(act)
                                    Cart.displayCart(act)
                                elif ch4 == 'n':
                                    Order.placeOrder(act)
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
    