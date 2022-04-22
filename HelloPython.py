# -*- coding: utf-8 -*-
"""
Created on Sat May  8 12:31:15 2021

@author: xisong
"""

import inspect

def hello_world(var1, var2):
    var1 = 12
    print("My name is {} {}".format(var1, var2))
    var1 = 24
    sum = var1 + 100
    print(sum)
    who = inspect.getframeinfo(inspect.currentframe().f_back)[2]
    print('{} call me'.format(who))

def Caller1():
    hello_world('xiaozhou',2)


Caller1()
