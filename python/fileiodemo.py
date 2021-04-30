# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:45:19 2021

@author: MathiyalaganN

Mode
'r' --> open for reading
'w' --> open for writing
'a' --> open for appending mode

Selector
'b' --> binary mode
't' --> Text mode

'wb' --> writebinary
'at' --> append text

'r+b' --> read and write
open() returns file object
"""

"""
import sys
print(sys.getfilesystemencoding())
"""
import sys
f = open('data.txt',mode='rt',encoding='utf-8')

"""

f.writelines(['Python3 popularly ,\n'
              'used for data science',
              'and natural language processing\n'])
"""

for line in f:
    sys.stdout.write(line)
    
f.close()