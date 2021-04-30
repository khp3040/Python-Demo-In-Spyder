# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:08:30 2021

@author: KshitijPawar
"""

class Shape:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def CalculateArea(self):
        raise NotImplementedError("Not Implemented")
        
class Rectangle(Shape):
    def CalculateArea(self):
        return self._width * self._height
    
class Triangle(Shape):
    def CalculateArea(self):
        return self._width * self._height * 0.5
    
rect = Rectangle(23,12)
tri = Triangle(13,23)

print(tri.CalculateArea())
print(rect.CalculateArea())