# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:44:21 2021

@author: KshitijPawar
"""

import csv

products = []
p1 = []

class Product:
    
    def lower_dict(d):
        new_dict = dict((k.lower(), v.lower()) for k, v in d.items())
        return new_dict

    def product():  
        filename = 'ProductsCsv.txt'
        
        with open(filename, 'r') as data:
            
            for line in csv.DictReader(data):
                products.append(line)
                #print(products)
                #print(line)
            #print(products) 
            for i in range(0,len(products)):
                p1.append(products[i]['name'])
            print(p1)
        return products,p1

class Search(Product):
    def findProduct():
        p = str(input("enter product name : "))
        for i in range(0,len(p1)):
            if(p == p1[i]):
                flag = True
            else:
                flag = False  
        try:
            if( flag == True):
                pass
        except (TypeError) as e:
            print(f"Convertion failed:{e}")
    
        else:
            print("Enter valid Name")
            
            
Search.findProduct()
# for i in range(0,len(products)):
#     p1.append(products[i]['name'])