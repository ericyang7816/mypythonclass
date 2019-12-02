import re
patt=r'::(\w+@\w+\.\w+)::'
f=open('redata.txt','r')
text=f.read()
m=re.findall(patt,text)
print(m)