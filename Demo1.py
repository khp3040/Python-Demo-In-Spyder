# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:47:24 2021

@author: KshitijPawar
"""

import socket

def resolve(host):
    return socket.gethostbyname(host)

print(resolve('ibm.com'))