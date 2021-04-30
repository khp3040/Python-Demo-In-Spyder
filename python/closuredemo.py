# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 15:33:10 2021

@author: MathiyalaganN
"""

"""
function myFunc(){
   function inner(){
       }
   }
"""

"""
python scoping Rules
L --> Local

E --> Enclosing

G --> Global

B --> Builtin
"""

def sort_By_Last_Letter(strings):
    def last_letter(s):
        return s[-1]
    print(last_letter)
    return sorted(strings,key = last_letter)
print(sort_By_Last_Letter(['ghi','def','abc']))


def enclosing():
    x = 56677.5
    def local_func():
        print(x)
    return local_func
    
lf = enclosing()
lf()
             
print(lf.__closure__)    
                     