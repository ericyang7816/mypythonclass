'''
第三章上机实验-写入文件
2019.09.24
'''
#!/usr/bin/env python
import os
ls=os.linesep

#get filename in two ways
'''
while True:
    fname=input("Please enter a name")
    if os.path.exists(fname):
        print("Error %s is already exist"%fname)
    else:
        break
'''
while True:
    fname=input("Please enter a name\n")
    try:
        fobj=open(fname)
    except IOError:
        break
    else:
        print("Error %s is already exist"%fname)

#get file text in lines
all = []
print("Please enter lines.To quit by enter'.'")

#loop until user stop
while True:
    entry=input('>>')
    if entry=='.':
        break
    else:
        all.append(entry)

#write lines to file
fobj=open(fname,'w',newline="") #消除空行
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print('OK')
