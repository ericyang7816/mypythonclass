from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.cufe.edu.cn/fwzn.htm")
bsObj = BeautifulSoup(html, "html.parser")
names = bsObj.find('div',{'class':'dqwz-right'})
obj=names.findAll('a')
for name in obj:
    print(name.get_text())
    print('\n')