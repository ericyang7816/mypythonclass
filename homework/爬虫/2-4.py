from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.cufe.edu.cn/zzjg/dzfw.htm")
bsObj = BeautifulSoup(html, "html.parser")
items = bsObj.findAll(lambda tag: len(tag.attrs)==3)
for item in items:
    if item.name=='a':
        print(item)