#! python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:49:49 2021

@author: xisong
"""
import copy

print('*********6.python 变成快速上手 4.10.1***')
spam = ['apples','bananas','tofu','cats']
def rerangeSpam(listSpam):
    retList = ''
    for i in range(len(listSpam)):  
        #if i == len(listSpam) - 1 :
        if listSpam[i] == listSpam[-1]:
            retList = retList + 'and ' + listSpam[i]
        else:    
            retList = retList + listSpam[i] + ', '
    print('\'',retList,'\'')
rerangeSpam(spam)
rerangeSpam(['1','2','3','4','5'])
rerangeSpam(['1','2','3','4','5','6','7','8'])
   
'''spam = [] 
while True: 
    print ('Enter some words into spam:')
    spam_input = input()
    if spam_input == '': 
        break
    spam = spam + [spam_input]
def add_and(spam):
     spam_and = 'and ' + spam[-1]
     del spam[-1]
     spam.append(spam_and)
     spam_all = spam[0]
     for i in range(1,len(spam)):
         spam_all = spam_all + ',' + spam[i]
     print (spam_all)
add_and(spam)'''
 
print('*********6.python 变成快速上手 4.10.2***')
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for i in range(6):
    for k in range(9):
        if k == 8:
            print(grid[k][i])
        else:
            print(grid[k][i],end='')
