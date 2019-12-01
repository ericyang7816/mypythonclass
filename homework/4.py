import re

patt1='^(0?[1-9]|1[0-2])[. -]([0-2]?[1-9]|3[0-1])$'
while True:
    text1=input()
    m=re.match(patt1,text1)
    print(m.group())