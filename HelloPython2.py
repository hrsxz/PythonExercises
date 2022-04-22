# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:04:23 2021

@author: xisong
"""

name = ''
while not name != '':
    print('Enter your name: ')
    name = input()
print ('How many guests will you have=?')
numOfGuests = int(input())
if numOfGuests != 0:
    print('Be sure to have enough room for all guests.')
print('Done.')