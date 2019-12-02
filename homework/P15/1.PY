import re
patt='[bh][aiu]t'
text='bat bit but hat hit hut'
m=re.findall(patt,text)
print(m)