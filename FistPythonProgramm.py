# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:24:41 2021

@author: xisong
"""
while True:
    print('Who are you')
    name = input()
    if name != 'Zhou':
        continue
    print('Hello, Zhou. What is the password?')
    password = input()
    if password == 'anan':
        break
print('Access granted.')
