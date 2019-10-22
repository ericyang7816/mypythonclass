'''
第三章上机实验-读写文件
2019.09.24
'''
#!/usr/bin/env python
import os
ls=os.linesep
def makeTextFile():
    while True:
        fname=input("Please enter a name")
        try:
            fobj=open(fname)
        except IOError:
            break
        else:
            print("Error %s is already exist"%fname)
    all = []
    print("Please enter lines.To quit by enter'.'")
    while True:
        entry=input('>>')
        if entry=='.':
            break
        else:
            all.append(entry)
    fobj=open(fname,'w',newline="") #消除空行
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print('OK')
def readTextFile():
    fname=input("Please enter your filename\n")
    while True:
        if not os.path.exists(fname):
            print("Error cannot found %s" % fname)
            fname=input("Please enter your filename\n")
        else:
            break
    fobj=open(fname,'r')
    for eachline in fobj:
        print(eachline.strip("\n"))
    fobj.close()

print("***************")
userChoice=input("1:makefile 2:readfile\n")

if userChoice == '1':
    makeTextFile()
if userChoice == '2':
    readTextFile()
