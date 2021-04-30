# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:58:01 2021

@author: KshitijPawar
"""

import socket
class MyClass:
    def __init__(self):
        self._cache ={}
        
        
    def __call__(self,host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
        
    def clear(self):
        self._cache.clear()
        
    def has_host(self):
        return host in self._cache