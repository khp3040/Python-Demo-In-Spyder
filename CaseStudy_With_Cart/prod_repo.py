# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:58:03 2021

@author: 0014CR744
"""
import csv

class Product():
    def productRepository():
        filename = 'ProductsCsv.txt'
        productList = []
        with open(filename, 'r') as data:
            for line in csv.DictReader(data):
                productList.append(line)
                #print(line)
            #print(self.productList)   
        return productList