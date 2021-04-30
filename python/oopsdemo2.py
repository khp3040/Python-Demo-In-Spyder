# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:08:45 2021

@author: MathiyalaganN
"""

class Shape:
    def __init__(self,width,height):
        self._width = width
        self._height = height
    def calculateArea(self):
        raise NotImplementedError('not implemented')
        
        
class Rectangle(Shape):
    def calculateArea(self):
        return self._width*self._height
    
class Triangle(Shape):
    def calculateArea(self):
        return .5*self._width*self._height
        
    
rectangle = Rectangle(23.4,34.5)
triangle = Triangle(23.4,34.5)
print(rectangle.calculateArea())
print(triangle.calculateArea())
