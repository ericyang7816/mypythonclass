import re

monthlist=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
f=open('redata.txt','r')
text=f.read()
for month in monthlist:
    search=re.search(month,text)
    if search is not None:
        print(search.group())
