#!/usr/bin/env python
import time
'''
db = {}
name=input('name:')
passwd = input('passwd: ')

info=(passwd,localtime)
db[name] = info
nameInput=input('name:')
print(db.get(nameInput)[1])
'''
localtime1 = time.time()
localtime2 = time.time()
a=localtime1-localtime2
print(localtime1)
print(localtime2)
print(a)
