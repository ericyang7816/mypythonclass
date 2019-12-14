import re

patt1='^\d{16}$'
text1='6230730021642567'
m=re.match(patt1,text1)
print(m.group())