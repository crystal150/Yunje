#-*- coding: utf-8 -*-

import sys
import urllib
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

for branduid in range(56358, 64600):
    fp = urllib.urlopen("http://www.styleberry.co.kr/shop/shopdetail.html?branduid=%d" %branduid)
    source = fp.read()
    fp.close()

    soup = BeautifulSoup(source, "html.parser")

    for title in soup.find_all('h3', class_='tit-prd'):
        print branduid, title.text


#f = open("shops.csv", "w")

