# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:45:42 2021

@author: MathiyalaganN
"""
DIGIT_MAP ={
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
    }
def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion was successfull! x={x}")
    except (KeyError,TypeError) as e:
        print(f"Convertion failed:{e}")
        x = -1
#   except (IndentationError):
#       pass 
        raise
    finally:
        print('Inside Finally')
    return x    
"""        
    except KeyError:
        print("Convertion failed")
        x = -1
    except TypeError:
        print("Convertion failed")
    return x
"""
print(convert("three four".split()))
print(convert("eleventeen".split()))
print(convert("eleventeen"))
