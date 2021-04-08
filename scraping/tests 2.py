from django.test import TestCase
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
#
from urllib.request import HTTPError, URLError
#
import requests
import re
# 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Login
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)

# driver.get('http://www.plabfootball.com')

# driver.find_element_by_css_selector('#userMenu > div > a:nth-child(1)').click()

# login_link = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.regist')))
# login_link.click()
# # driver.find_element_by_css_selector('.btn.regist').click()

# driver.find_element_by_name('username').send_keys('sportfolio94@gmail.com')
# driver.find_element_by_name('password').send_keys('tmy4834733!')
# driver.find_element_by_css_selector('.btn.submit').click()

# time.sleep(5)

# driver.quit()


# codeit TEST

# unopen Chrome
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome('chromedriver',options=options)
# open Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/orangebottle/index')

branches = driver.find_elements_by_css_selector('div.container > div.branch')
branch_list = []

for branch in branches:
    name = branch.find_element_by_class_name('city').text.strip()
    address = branch.find_element_by_class_name('address').text.strip()
    phone = branch.find_element_by_class_name('phoneNum').text.strip()
    branch_list.append([name, address, phone])

print(branch_list)




# def getPage(url):
# 	req = requests.get(url)
# 	bs = BeautifulSoup(req.text, 'html.parser')
# 	rankWrap = bs.find('ul', {'class': 'rank__order'})
# 	rankList = rankWrap.find_all('li', {'class': 'list'})
# 	artistList = []
# 	for a in rankList:
# 		artistList.append(a.get_text(' ',strip=True).split(' ')[2])

# 	print(artistList)

# url = 'https://workey.codeit.kr/music/index'
# getPage(url)


# def getPage(url):
# 	req = requests.get(url)
# 	bs = BeautifulSoup(req.text, 'html.parser')
# 	branch = bs.find_all('div', {'class': 'branch'})
# 	branch_infos=[]
# 	for b in branch:
# 		branch_name = b.find('p', {'class': 'city'}).get_text()
# 		address = b.find('p', {'class': 'address'}).get_text()
# 		phone_number = b.find('span', {'class': 'phoneNum'}).get_text()
# 		branch_infos.append([branch_name, address, phone_number])
# 	print(branch_infos)

# url = 'https://workey.codeit.kr/orangebottle/index'
# getPage(url)



# def getPage(url):
# 	req = requests.get(url)
# 	bs = BeautifulSoup(req.text, 'html.parser')
# 	ph=[]
# 	for p in bs.find_all('span', {'class': 'phoneNum'}):
# 		ph.append(p.get_text())
# 	return ph

# url = 'https://workey.codeit.kr/orangebottle/index'
# print(getPage(url))

# 세고 크롤러 테스트
# class Content:
# 	def __init__(self, container, title, text):
# 		self.container = container
# 		self.title = title
# 		# self.url  = url
# 		self.text = text

# def getPage(url):
# 	req = requests.get(url)
# 	return BeautifulSoup(req.text, 'html.parser')

# def sego(url):
# 	bs = getPage(url)
# 	container = bs.findAll('div', {"class": "card--container"})
# 	title = bs.select("li", {"class": "card--title"})
# 	text = bs.select("pre", {"class": "card--content"})
# 	return Content(container, title, text)


# url = """
# http://www.letsego.site/
# """

# content = sego(url)
# print('CONTAINER: \n{}'.format(content.container))
# # print('TITLE : \n{}'.format(content.title))
# # print('TITLE : \n{}'.format(content.text))


# 크롤러 실제 사용 테스트
# class Crawler:

# 	def getPage(self, url):
# 		try:
# 			req = requests.get(url)
# 		except requests.exceptions.RequestException:
# 			return None
# 		return BeautifulSoup(req.text, 'html.parser')

# 	def safeGet(self, pageObj, selector):
# 		childObj = pageObj.select(selector)
# 		if childObj is not None and len(childObj) > 0:
# 			return childObj[0].get_text()
# 		return ''

# 	def search(self, topic, site):
# 		"""
# 		주어진 검색어로 주어진 웹사이트를 검색해 결과 페이지를 모두 기록합니다.
# 		"""
# 		bs = self.getPage(site.searchUrl + topic)
# 		searchResults = bs.select(site.resultListing)
# 		for result in searchResults:
# 			url = result.select(site.resultUrl)[0].attrs['href']
# 			#URL 상대/절대 경로 확인
# 			if (site.absoluteUrl):
# 				bs = self.getPage(url)
# 			else:
# 				bs = self.getPage(site.url + url)

# 			if bs is None:
# 				print('Something was wrong with that page or URL. Skipping!')
# 				return
# 			title = self.safeGet(bs, site.titleTag)
# 			body = self.safeGet(bs, site.bodyTag)
# 			if title != '' and body != '':
# 				content = Content(topic, url, title, body)
# 				content.print()

# class Content:
# 	"""
# 	글/페이지 전체에 사용할 기반 클래스
# 	"""
# 	def __init__(self, topic, url, title, body):
# 		self.topic = topic
# 		self.url = url
# 		self.title = title
# 		self.body = body

# 	def print(self):
# 		"""
# 		출력 결과를 원하는 대로 바꿀 수 있는 함수
# 		"""
# 		print('New article found for topic {}'.format(self.topic))
# 		print('URL: {}'.format(self.url))
# 		print('TITLE: {}'.format(self.title))
# 		print('BODY: \n{}'.format(self.body))

# class Website:
# 	"""
# 	웹사이트 구조에 관한 정보를 저장할 클래스
# 	"""
# 	def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
# 		self.name = name
# 		self.url = url
# 		self.searchUrl = searchUrl
# 		self.resultListing = resultListing
# 		self.resultUrl = resultUrl
# 		self.absoluteUrl = absoluteUrl
# 		self.titleTag = titleTag
# 		self.bodyTag = bodyTag

# crawler = Crawler()

# siteData = [
# 	["O\'Reilly Media'",
# 		'http://oreilly.com',
# 		'https://ssearch.oreilly.com/?q=',
# 		'article.product-result',
# 		'p.title a',
# 		True,
# 		'h1',
# 		'section#product-description'],
# 	['Brookings',
# 		'http://www.brookings.edu',
# 		'https://www.brookings.edu/search/?s=',
# 		'div.list-content article',
# 		'h4.title a',
# 		True,
# 		'h1',
# 		'div.post-body']
# ]

# sites = []
# for raw in siteData:
# 	sites.append(Website(raw[0], raw[1], raw[2], raw[3], raw[4], raw[5], raw[6], raw[7]))

# topics = ['python', 'data science']
# for topic in topics:
# 	print('GETTING INFO ABOUT ' +  topic)
# 	for targetSite in sites:
# 		crawler.search(topic, targetSite)


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

# url = """
# https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/
# """

# content = scrapeBrookings(url)
# print('Title: {}'.format(content.title))
# print('URL: {}'.format(content.url))
# print(content.body)

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

