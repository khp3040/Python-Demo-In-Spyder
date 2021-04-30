# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:28:51 2021

@author: KshitijPawar
"""
DIGIT_MAP = {
    'zero': '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
    }

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"conversion successful! x={x}")
    except KeyError as e:
        print(f"conversion failed because of {e}")
        x = -1
    except  TypeError as e:
        print(f"conversion failed because of {e}")
        x = -1
    finally :
        print("inside finally")
    return x

print(convert(512))
print(convert("nine".split()))   
print(convert("three four".split()))
print(convert("eleven".split())) 