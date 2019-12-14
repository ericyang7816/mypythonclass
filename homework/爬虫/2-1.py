from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.cufe.edu.cn/zzjg/dzfw.htm")
bsObj = BeautifulSoup(html, "html.parser")
names = bsObj.find('div',{'class':'dzfw'})
obj=names.findAll('a')
for name in obj:
    for id in name.children:
        print('名称： '+id)
    print('链接： '+name['href'])
    print('\n')