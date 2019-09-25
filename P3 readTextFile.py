'''
第三章上机实验-读取文件
2019.09.24
'''
#!/usr/bin/env python
import os

#get filename
fname=input("Please enter your filename\n")

#attempt to open the file in two ways
'''
try:
    fileobj=open(fname,'r')
except IOError:
    print("Error occurred")
else:
    #display contents
    for eachline in fileobj:
        print(eachline),
    fileobj.close()
'''
while True:
    if not os.path.exists(fname):
        print("Error cannot found %s" % fname)
        fname=input("Please enter your filename\n")
    else:
        break

#open and print the file   
fileobj=open(fname,'r')
for eachline in fileobj:
    print(eachline),
fileobj.close()