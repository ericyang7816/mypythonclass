from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html1 = urlopen("https://www.zhihu.com/special/19551676")
soup_obj1 = BeautifulSoup(html1, "html.parser")
titles1 = soup_obj1.findAll("div", {"class": re.compile("ContentItem-module-title-....")})
f=open('title.txt','w')
for title in titles1:
    content=title.get_text()
    f.write(content+'\n')

html2 = urlopen("https://www.zhihu.com/special/19828946")
soup_obj2 = BeautifulSoup(html2, "html.parser")
titles2 = soup_obj2.findAll(lambda tag: tag.name=='img')
for title in titles2:
    print(title['src'])
