from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://www.cufe.edu.cn/index.htm")
bsObj=BeautifulSoup(html,"html.parser")
images=bsObj.findAll("img",{"src":re.compile(".+\.jpg")}) 
for image in images:
    print(image["src"])
