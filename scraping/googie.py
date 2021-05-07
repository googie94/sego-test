from urllib.request import urlopen
from bs4 import BeautifulSoup
#
from urllib.request import HTTPError, URLError
#
import requests
import re
# 


html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)