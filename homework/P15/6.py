import re

patt1='^www\.([A-Za-z0-9])+\.com$'
text1='www.qq.com'
m=re.match(patt1,text1)
print(m.group())

patt2='www\.([A-Za-z0-9])+\.(com|edu|net|gov)$'
text2='www.jhu.edu'
m=re.match(patt2,text2)
print(m.group())