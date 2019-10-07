'''
第三章上机实验-读取文件
2019.09.24
'''
#!/usr/bin/env python
import os


#attempt to open the file in two ways
while True:
    #get filename
    fname=input("Please enter your filename\n")
    try:
        fobj=open(fname,'r')
    except IOError:
        print("Error occurred.File not found.")
    else:
        break
'''
while True:
    if not os.path.exists(fname):
        print("Error cannot found %s" % fname)
        fname=input("Please enter your filename\n")
    else:
        break
'''
#open and print the file   
fobj=open(fname,'r')
for eachline in fobj:
    print(eachline.strip("\n"))
fobj.close()
