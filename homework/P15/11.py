import re

patt1='^([\w-])+@([\w-])+\.(([\w-])+\.)*([\w-])+$'
text1='someone@cufe.edu.cn'
m=re.match(patt1,text1)
print(m.group())
