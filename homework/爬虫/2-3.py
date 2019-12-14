from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.cufe.edu.cn/zzjg/dzfw.htm")
bsObj = BeautifulSoup(html, "html.parser")
info = bsObj.find('a',text='学校办公室 >>').parent.next_sibling.next_sibling
details=info.findAll('a')
for name in details:
    for id in name.children:
        print('名称： '+id)
    print('链接： '+name['href'])
    print('\n')