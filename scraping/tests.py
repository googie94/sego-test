from django.test import TestCase
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
#
from urllib.request import HTTPError, URLError
#

#test12 news scraping
# import requests
# #
# class Content:
# 	"""
# 	글이나 페이지 전체에서 적용할 기반 클래스
# 	"""
# 	def __init__(self, url, title, body):
# 		self.url = url
# 		self.title = title
# 		self.body = body

# def getPage(url):
# 	req = requests.get(url)
# 	return BeautifulSoup(req.text, 'html.parser')

# def scrapeNYTimes(url):
# 	bs = getPage(url)
# 	title = bs.find('h1').text
# 	lines = bs.select('div.StoryBodyCompanionColumn div p')
# 	body = '\n'.join([line.text for line in lines])
# 	return Content(url, title, body)

# def scrapeBrookings(url):	
# 	bs = getPage(url)
# 	title = bs.find('h1').text
# 	body = bs.find('div', {'class', 'post-body'}).text
# 	body = ''
# 	return Content(url, title, body)

# # url = """
# # https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/
# # """

# # content = scrapeBrookings(url)
# # print('Title: {}'.format(content.title))
# # print('URL: {}'.format(content.url))
# # print(content.body)

# url = """
# https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html
# """

# content = scrapeNYTimes(url)
# print('Title: {}'.format(content.title))
# print('URL: {}'.format(content.url))
# print(content.body)


#test11 oreilly
# import ssl
# from urllib.parse import urlparse
# allExtLinks = set()
# allIntLinks = set()
# #
# def getAllExternalLinks(siteUrl):
# 	try:
# 	    ssl._create_unverified_context
# 	except AttributeError:
# 	    pass
# 	else:
# 	    ssl._create_default_https_context = ssl._create_unverified_context
# 	html = urlopen(siteUrl)
# 	domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	internalLinks = getInternalLinks(bs, domain)
# 	externalLinks = getExternalLinks(bs, domain)
# 	#
# 	for link in externalLinks:
# 		if link not in allExtLinks:
# 			allExtLinks.add(link)
# 			print(link)
# 	#
# 	for link in internalLinks:
# 		if link not in allIntLinks:
# 			allIntLinks.add(link)
# 			getAllExternalLinks(link)

# allIntLinks.add('http://oreilly.com')
# getAllExternalLinks('http://oreilly.com')


#test10 wiki
# import ssl
# import re
# def verify():
# 	try:
# 	    ssl._create_unverified_context
# 	except AttributeError:
# 	    pass
# 	else:
# 	    ssl._create_default_https_context = ssl._create_unverified_context
# #
# def getUrl(url):
# 	try:
# 		verify()
# 		html = urlopen(url)
# 	except URLError as e:
# 		return None
# 	except HTTPError as e:
# 		return None
# 	return html
# #

# pages = set()
# def getLinks(pageUrl):
# 	global pages
# 	# 'https://en.wikipedia.org/wiki/Kevin_Bacon'
# 	html = getUrl('http://en.wikipedia.org'+pageUrl)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	#
# 	try:
# 		print(bs.h1.get_text())
# 		# print(bs.find(id = 'mw-content-text').findAll('p')[0])
# 		# print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
# 	except AttributeError:
# 		print('this missing something')
# 	#
# 	links = bs.findAll('a', href = re.compile('^(/wiki/)'))
# 	for link in links:
# 		if link.attrs['href'] not in pages:
# 			newPage = link.attrs['href']
# 			print('----------\n'+newPage)
# 			pages.add(newPage)
# 			getLinks(newPage)
# getLinks('')


#test9 regex
# import re
# print('-------')
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for img in images:
# 	print(img['src'])


#test8 haldle parent
# print('---------')
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# value = bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
# print(value)


#test7 handle child tag2 - nextsibling
# print('----------')
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# sbs = bs.find('table', {'id': 'giftList'}).tr.next_siblings

# for sb in sbs:
# 	print(sb)


#test6 handle children tag
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# childrens = bs.find('table', {'id': 'giftList'}).children
# for child in childrens:
# 	print(child)

#test5 class 이용 스크랩핑
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html, 'html.parser')

# nameList = bs.findAll('span', {'class': 'green'}, text = 'the prince', limit=3)
# for name in nameList:
# 	print(name.get_text())


#test4 Error3 - Attribute(요청한 클래스나 태그가 없는 경우 None을 반환)
# def getSomething(url):
# 	try:
# 		html = urlopen(url)
# 	except URLError as e:
# 		return None
# 	except HTTPError as e:
# 		return None
# 	#
# 	try:
# 		bs = BeautifulSoup(html, 'html.parser')
# 		title = bs.h1
# 	except AttributeError as e:
# 		return None
# 	return title

# title = getSomething('http://www.pythonscraping.com/pages/warandpeace.html')
# if title == None:
# 	print('title is None')
# else:
# 	print(title)


#test3 Error2 - URL
# try:
# 	html = urlopen('http://www.pythonscrapingthisurldoesnotexist.com')
# except HTTPError as e:
# 	print(e)
# except URLError as e:
# 	print('sever not found!')
# else:
# 	print('keep going')
# 	bs = BeautifulSoup(html, 'html.parser')
# 	print(bs.h1)

#test2 Error1 - HTTP
# try:
# 	html = urlopen('htt://www.pythonscraping.com/pages/page1.html')	
# except HTTPError as e:
# 	print(e)
# else:
# 	print('keep going')
# 	bs = BeautifulSoup(html, 'html.parser')
# 	print(bs.h1)

#test1
# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html, 'html.parser')
# print(bs.h1)

