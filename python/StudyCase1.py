# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 15:12:06 2021

@author: MathiyalaganN
"""
import csv

  
filename ="csv_file.txt"
  
# opening the file using "with" 
# statement

product = []
product1= []
p1= []
with open(filename, 'r') as data:

    for line in csv.DictReader(data):
        product.append(line)
        
    print(product)
    for i in range(0,len(product)):
        p1.append(product[i]['name'])
        
        
    print(p1)
        
        
    
    
    
