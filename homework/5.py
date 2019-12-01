import re

patt1='^\d{16}$'
text1='6230df'
m=re.match(patt1,text1)
print(m.group())