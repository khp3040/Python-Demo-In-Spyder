# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:23:28 2021

@author: KshitijPawar
"""

from functools import reduce


# names = ['java','javascript','python','kotlin','groovy']

# def starts_with_j(val):
#     return val.startswith('j')

# print(list(filter(starts_with_j,names)))



# orders =[{'id':1,'name':'Iphone','price':5678.5},
#          {'id':3,'name':'Ipad','price':3678.5},
#          {'id':4,'name':'macbook','price':123678.5}]

    
# print(list(filter(lambda order: order['price'] >= 50000, orders)))

# print(max(order['price'] for order in orders))

# print(min(order['price'] for order in orders))

# print(sum(order['price'] for order in orders))

# avg = sum(order['price'] for order in orders) / len(orders)
# print(avg)

#########################ASSIGNMENT##############################

#HINT
# print(reduce(lambda x,y:x+y,map(lambda a: a ,filter(lambda c: (c>=3),(3,4,1,2,5)))))

#sum
# print(reduce(lambda o1,o2: o1 + o2,map(lambda o: o['price'] ,orders)))

#average
# avg = reduce(lambda o1,o2: o1 + o2,map(lambda o: o['price'] ,orders)) / len(orders)
# print(avg)

#Average with filter
filteredData = list()
print(filteredData)
#avg = reduce(lambda o1,o2: o1+o2,map(lambda o : o, filteredData)) / len(filteredData) 
#print(avg)

orders =[{'id':1,'name':'Iphone','price':5678.5},
         {'id':3,'name':'Ipad','price':3678.5},
         {'id':4,'name':'macbook','price':123678.5}]


#MIN
print(reduce(lambda o1,o2 : o1 if o1 < o2  else o2 ,map(lambda p : p['price'],orders)))

#MAX
print(reduce(lambda o1,o2 : o1 if o1 > o2  else o2 ,map(lambda p : p['price'],orders)))


#MAX using filter


