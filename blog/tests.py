from django.test import TestCase
#
from urllib.request import urlopen, HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bs = BeautifulSoup(html.read(), 'html.parser')
		for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
			print(sibling)
	except AttributeError as e:
		return None
	return title

title = getTitle('http://www.pythonscraping.com/pages/page3.html')
if title == None:
	print('Title could not be found')
else:
	print(title)