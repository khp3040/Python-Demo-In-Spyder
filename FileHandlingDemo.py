# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:41:12 2021

@author: KshitijPawar
"""

import  sys

# print(sys.getfilesystemencoding())

####Write
# f= open('dataDemo.txt',mode='wt',encoding='utf-8')
# f.write("Python File Handling Demo")
# f.close()

####Append
# f= open('dataDemo.txt',mode='at',encoding='utf-8')
# f.writelines("\n Python for Machine Learning \n python for data-science \n python for nlp")
# f.close()

####Read
f = open('dataDemo.txt',mode='rt',encoding='utf-8')

for line in f:
    sys.stdout.write(line)

f.close()








