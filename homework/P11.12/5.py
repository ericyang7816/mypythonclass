#coding:utf-8
from urllib.request import urlretrieve

def firstNonBlank(lines):
    for  eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f=open(webpage,'rb+')
    lines=f.readlines()
    f.close()
    print(firstNonBlank(lines))
    lines.reverse()
    print(firstNonBlank(lines))

def download(url='http://www.zhihu.com',process=firstLast):
    try:
        retval=urlretrieve(url)[0]
    except IOError:
        retval=None
    if retval:
        process(retval)

if __name__=="__main__":
    download()