from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
'''
html1 = urlopen("https://www.zhihu.com/special/19551676")
soup_obj1 = BeautifulSoup(html1, "html.parser")
titles1 = soup_obj1.findAll("div", {"class": re.compile("ContentItem-module-title-....")})
for title in titles1:
    print(title.get_text())
'''
html2 = urlopen("https://zhuanlan.zhihu.com/readrun")
soup_obj2 = BeautifulSoup(html2, "html.parser")
titles2 = soup_obj2.findAll(lambda tag: tag.attrs['class']=='ArticleItem-Title')
f=open('title.txt','w')
for title in titles2:
    print(title.get_text())
#    f.write(title.get_text())
#    f.write('\n')
