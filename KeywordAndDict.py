# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:05:01 2021

@author: xisong
"""

print('*********1. python函数参数传递是引用传递：***')
def test(a,b,*args,**kwargs):
    c = args
    print(a, '\n',b,'\n',c)
    dict = kwargs
    print(dict['age'])
test('this is a', 'this is b', 'c1', 'c2','c3', name = 'Zhou', age= 36)


print('*********2. tuple list and string***')
listHello = list('Hello')
print(listHello)
strHello = ''
for i in range(len(listHello)):
    strHello = strHello + listHello[i]
print(strHello)

print('********3. 对比值或者地址是否相等***')
a = 1
b = 1
print(a == b) # True 对比值是否相等
print(a is b) # True 对比地址是否一致

a = 888
b = 888
print(a == b) # True
print(a is b) # False

a = 'hello'
b = 'hello'
print(a == b) # True
print(a is b) # True

a = 'hello world'
b = 'hello world'
print(a == b) # True
print(a is b) # False

print('*********4. 调用全局变量***')
verbose = True
def example():
    global verbose
    verbose = False
    print('verbose =',verbose)
example();

print('*********5. python函数参数传递是引用传递：***')
def test(n):
    print(id(n))
k = "string"
print(id(k)) # 2305161642256
test(k) # 2305161642256

#%%
