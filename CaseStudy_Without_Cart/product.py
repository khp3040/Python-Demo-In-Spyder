# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:15:45 2021

@author: KshitijPawar
"""
import csv

class Product():
    
    def productRepository():
        filename = 'ProductsCsv.txt'
        products = []
        with open(filename, 'r') as data:
            
            for line in csv.DictReader(data):
                products.append(line)
                #print(line)
        #print(self.products)   
        return products
    
    

# p = Product
# print(p.productRepository())