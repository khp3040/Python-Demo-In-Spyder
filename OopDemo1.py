# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:34:02 2021

@author: KshitijPawar
"""

class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"no airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"invalid Route number  '{number}'")
        self._number = number
        self._aircraft = aircraft
        
    def number(self):
        return self._number
    def aircraft_model(self):
        return self._aircraft.model()
        
class AirCraft:
    def __init__(self,registration, model, num_rows, num_of_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_of_seats_per_row = num_of_seats_per_row
        
    def registration(self):
         return self.registration
    def model(self):
        return self.model.model
             
    def seating_plan(self):
         return(range(1, self._num_rows+1),
                "ABCDEFGHIJK"[:self._num_of_seats_per_row])
    
    
  

flight = Flight('SM1234',AirCraft('AIR-987','AirBus-619',num_rows=22,num_of_seats_per_row=8))
print(type(flight))
print(flight.number())
print(flight._aircraft.seating_plan())


# aircraft = AirCraft('AIR-987','AirBus-619',num_rows=22,num_of_seats_per_row=8)
# print(aircraft.seating_plan())
