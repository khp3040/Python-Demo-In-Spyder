# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
def resolve(host_as_arg):
    return socket.gethostbyname(host_as_arg)
print(resolve('google.com'))
