import json
import urllib
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.wildberries.ru/catalog/38567378/detail.aspx?targetUrl=XS'
html = request.urlopen(url).read()
a = json.loads(html, ensure_ascii=False)
print(html)
