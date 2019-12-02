import re
patt=r'::(\w+)@(\w+\.\w+)::'
f=open('redata.txt','r')
while True:
    text=f.readline()
    if text is not '':
        m=re.search(patt,text)
        if m is not None:
            print(m.group(1))
            print(m.group(2))
    else:
        break