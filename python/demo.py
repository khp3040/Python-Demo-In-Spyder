# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:45:04 2021

@author: MathiyalaganN
"""
import csv

with open('csv_file.txt','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    with open('new_file.txt','w') as new_file:
      csv_writer=csv.writer(new_file, delimiter=',')
      for line in csv_reader:
       csv_writer.writerow(line)
      # print(line)
       
