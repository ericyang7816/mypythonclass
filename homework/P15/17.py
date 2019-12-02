import re

daylist=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
f=open('redata.txt','r')
text=f.read()
for day in daylist:
    search_list=re.findall(day,text)
    print('number of %s: %d'%(day,len(search_list)))