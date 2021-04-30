# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:23:11 2021

@author: MathiyalaganN
"""
from functools import reduce

names = ['Java','JavaScript','Kotlin','Python','Groovy']

orders =[{'id':1,'name':'Iphone','price':55678.5},
         {'id':3,'name':'Ipad','price':32678.5},
         {'id':4,'name':'macbook','price':123678.5}]

"""
prices=map(lambda x:x['price'],orders)
total=sum(prices)
print(total)
"""
print(filter(lambda o1,o2: o1 > o2 ,map(lambda p: p['price'],orders)))
print(reduce(lambda o1,o2:o1 if o1 < o2 else o2,map(lambda order: order['price'],orders)))
# print(reduce(lambda o1,o2:o1+o2,map(lambda order: order['price'],filter(lambda order:order['price']>=20000.0,orders))))
# print(reduce(lambda o1,o2:o1+o2,map(lambda order: (order['price'],order['name']),filter(lambda order:order['price']>=20000.0,orders))))
# print(reduce(lambda o1,o2:(o1[0]+o2[0],o1[1]+o2[1]),map(lambda order: (order['price'],order['name']),filter(lambda order:order['price']>=20000.0,orders))))
# print(reduce(lambda o1,o2:o1+o2/2,map(lambda order: order['price'],filter(lambda order:order['price']>=20000.0,orders))))

# def Average(l):
#     avg = reduce(lambda x,y: x+y,l)/len(l)
#     return avg

# filtereddata=list(map(lambda order:order['price'],filter(lambda order : order['price'] >= 10000.0,orders)))

# print(reduce(lambda o1,o2:o1+o2,filtereddata)/len(filtereddata))
#print(reduce(lambda x,y:x+y,map(lambda x: x+x ,filter(lambda x: (x>=3,(1,2,3,4)))))


#print(reduce(lambda i,j : i if i['price'] > j['price'] else j,orders))

#print(reduce(lambda i,j : i if i['price'] < j['price'] else j,orders))



# res={sub['price'] for sub in orders}
# print(max(res))
# print(min(res))
# print(sum(res))      


#      #  Method 1  
     
# print(list(filter(lambda order: order['price'] >=50000.0, orders)))
#      #  Method 2    
     
# d = list(filter(lambda a: a.get("price")>50000.0,orders))
# print(d)
  

# def starts_with_j(val):
#     return val.startswith('J')


# print(list(filter(starts_with_j, names)))



# for x in names:
#     if x.startswith('J'):
#         print(x)


"""
range(start)
range(start,stop)
range(start,stop,step)
print(range(5))
for i in range(5,10):
    print(i)
    
print(list(range(0,10,2)))
"""
"""
Collection

Tuples
Strings
Lists
Dictionaries
Sets
Ranges
"""

data = set([67,45,21,44,32,44])
print(type(data))

data.add(45)

data.remove(44)

for x in data:
    print(x)

print("-------")

cloneddata = data.copy()

cloneddata.update([1,2,3,4])

for x in cloneddata:
    print(x)