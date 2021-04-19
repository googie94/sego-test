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
import datetime
#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
#
import pyperclip
# 
import csv
#




# save mysql
import pymysql

host = 'sego.c3jqlg47t2v5.ap-northeast-2.rds.amazonaws.com'
user = 'sego_admin'
pw = 'googie0126!'
db = 'sego'
conn = pymysql.connect(host=host, user=user, passwd=pw, db=db, charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

def store(area_group, area, district, phone):
	cur.execute(
		'INSERT INTO agent2 (area_group, area, district, phone) VALUES (%s, %s, %s, %s)',
		(area_group, area, district, phone)
	)
	cur.connection.commit()



# -------------------------------
import json
import random

# USER
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2MTg4MTcxOTEsImV4cCI6MTYxODgyNzk5MX0.elA6vG4bfmIHmn1sshzUlFF0S48jFs8bcsbRdgrZ7CQ'
}

# AREAGROUP
def getAreaGroup(api):
	req = requests.get(api, headers=headers, data=payload)
	time.sleep(random.uniform(1,4))
	global areaGroupList
	areaGroupList = req.json()["regionList"]
	return areaGroupList

# AREA
def getArea(api):
	req = requests.get(api, headers=headers, data=payload)
	time.sleep(random.uniform(3,10))
	global areaList
	areaList = req.json()["regionList"]
	return areaList

# AREADETAIL
def getAreaDetail(api):
	req = requests.get(api, headers=headers, data=payload)
	time.sleep(random.uniform(3,10))
	global areaDetailList
	areaDetailList = req.json()["regionList"]
	return areaDetailList

api = "https://new.land.naver.com/api/regions/list?cortarNo=0000000000"
getAreaGroup(api)
# print(areaGroupList)

results = []
for ag in areaGroupList:
	api = "https://new.land.naver.com/api/regions/list?cortarNo={}".format(ag["cortarNo"])
	getArea(api)
	# print(areaList)
	for a in areaList:
		api = "https://new.land.naver.com/api/regions/list?cortarNo={}".format(a["cortarNo"])
		getAreaDetail(api)
		# print(areaDetailList)
		for ad in areaDetailList:
			# 
			for i in range(1, 500):
				print("MORE INDEX : ",i)
				try:
					time.sleep(random.uniform(1,4))
					try:
						# print("INST NUM : ", ad["cortarNo"])
						api = "https://new.land.naver.com/api/articles?cortarNo={}&order=rank&realEstateType=SG%3ASMS%3AGJCG%3AAPTHGJ%3AGM%3ATJ&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={}".format(ad["cortarNo"], i)
					except:
						pass
				except:
					pass
				req = requests.get(api, headers=headers, data=payload)
				time.sleep(random.uniform(1,4))
				# test = req.json()
				if req.json()["isMoreData"] == False:
					break;
				else:
					for t in req.json()["articleList"]:
						# print(t["articleNo"])
						results.append(t["articleNo"])

			print("ITEM LENGTH : ", len(results))
			# print(results)
			if len(results) != 0:
				for index, r in enumerate(results):
					print("ITEM INDEX : ", index)
					try:
						time.sleep(random.uniform(1,4))
						try:
							# print("INST NUM : ", r)
							api = "https://new.land.naver.com/api/articles/{}".format(r)
						except:
							pass
					except:
						pass
					# 
					req = requests.get(api, headers=headers, data=payload)
					global final
					final = req.json()
					try:		
						ag = final["articleDetail"]["cityName"]
						a = final["articleDetail"]["divisionName"]
						d = final["articleDetail"]["sectionName"]
						ph = final["articleRealtor"]["cellPhoneNo"]
						print(ag, a, d, ph)
						store(ag, a, d, ph)
					except:
						pass
					# 
					if index+1 == len(results):
						print('------------LAST INDEX------------')
						results = []
			else:
				print('NO ITEM')

			




# -------------------------------

# 5권역 - 안양, 과천, 안산, 군포, 수원
# GET PHONE NUMBER - NAVER
# OPEN CRHOME
# driver = webdriver.Chrome()
# driver.implicitly_wait(3)

# # GET URL
# driver.get('https://new.land.naver.com/offices')

# # LIST
# # 1~21
# areaList=[7]
# districtList=[1]
# itemList=[]
# dtindex=0

# # FUNCTIONS
# def clickSelector(path):
# 	item = driver.find_element_by_css_selector(path)
# 	item.click()

# def nextArea(num):
# 	driver.implicitly_wait(1)
# 	print("NEXTAREA START")
# 	index = str(num)
# 	print('AREA ID : ', index)
# 	clickSelector('#region_filter > div > a > span:nth-child(2)')
# 	time.sleep(1)
# 	# 경기도
# 	# clickSelector('#region_filter > div > div > div.area_list_wrap > ul > li:nth-child(2)')
# 	# 인천시
# 	clickSelector('#region_filter > div > div > div.area_list_wrap > ul > li:nth-child(3)')
# 	# 대구시
# 	# clickSelector('#region_filter > div > div > div.area_list_wrap > ul > li:nth-child(6)')
# 	time.sleep(1)
# 	clickSelector('#region_filter > div > div > div.area_list_wrap > ul > li:nth-child('+index+')')
# 	time.sleep(1)
# 	global districtList
# 	# districtList = driver.find_elements_by_css_selector('#region_filter > div > div > div.area_list_wrap > ul > li')
# 	print('NEXTAREA END')

# def nextDistrict(index):
# 	driver.implicitly_wait(1)
# 	print("NEXTDISTRICT START")
# 	print('DISTRICT LENGTH', len(districtList))
# 	global dtindex
# 	# dtindex = str(index+1)
# 	dtindex = str(index)
# 	print('DISTRICT INDEX : ', dtindex)
# 	clickSelector('#region_filter > div > div > div.area_list_wrap > ul > li:nth-child('+dtindex+')')
# 	# 
# 	time.sleep(1)
# 	clickSelector('#region_filter > div > a > span:nth-child(4)')
# 	time.sleep(1)
# 	clickSelector('#region_filter > div > div > div.area_list_wrap > ul > li:nth-child('+dtindex+')')
# 	# 
# 	time.sleep(2)
# 	try:
# 		for i in range(50):
# 			clickSelector('#listContents1 > div > div > div.loader')
# 			time.sleep(3)
# 	except:
# 		pass
# 	global itemList
# 	itemList = driver.find_elements_by_css_selector('#listContents1 > div > div > div:nth-child(1) > div')
# 	print('ITEM LENGTH', len(itemList))
# 	if len(itemList) == 0:
# 		clickSelector('#region_filter > div > a > span:nth-child(4)')
# 		time.sleep(1)
# 	print("NEXTDISTRICT END")

# def nextItem(index):
# 	driver.implicitly_wait(1)
# 	print('NEXTITEM START')
# 	index = str(index+1)
# 	# 
# 	try:
# 		other = driver.find_element_by_css_selector('#listContents1 > div > div > div:nth-child(1) > div:nth-child('+index+') > div > div.label_area > a')
# 		other.click()
# 		print('LINK CLICK')
# 	except:
# 		clickSelector('#listContents1 > div > div > div:nth-child(1) > div:nth-child('+index+')')
# 	# 
# 	time.sleep(2)
# 	# 
# 	try:
# 		ag = driver.find_element_by_css_selector('#region_filter > div > a > span:nth-child(2)').text
# 		ar = driver.find_element_by_css_selector('#region_filter > div > a > span:nth-child(3)').text
# 		dt = driver.find_element_by_css_selector('#region_filter > div > a > span:nth-child(4)').text
# 		is_phone = driver.find_element_by_css_selector('#detailContents1 > div.detail_box--summary > table > tbody > tr:last-child > td > div > div.info_agent_wrap > dl:nth-child(2) > dd').text
# 		if '010-' in is_phone:
# 			phone = is_phone.split(',')
# 			for phn in phone:
# 				if '010-' in phn:
# 					print(ag, ar, dt, phn)
# 					store(ag, ar, dt, phn)
# 				else:
# 					print('PHONE IS NONE')
# 		else:
# 			print('PHONE IS NONE')
# 	except:
# 		pass
# 	# 
# 	try:
# 		close = driver.find_element_by_css_selector('#ct > div.map_wrap > div.detail_panel > div > button')
# 		close.click()
# 	except:
# 		pass
# 	# 
# 	print('ITEM INDEX : ', index)
# 	if index == str(len(itemList)):
# 		print('LAST ITEM')
# 		clickSelector('#region_filter > div > a > span:nth-child(4)')
# 		time.sleep(1)
# 		if dtindex == str(len(districtList)):
# 			print('LAST DISTRICT')
# 			clickSelector('#region_filter > div > a > span:nth-child(4)')
# 			time.sleep(1)
# 	# 
# 	print('----------NEXTITEM END----------')
	

# # START
# for a in areaList:
# 	nextArea(a)
# 	# for d in range(0, len(districtList)):
# 	for d in districtList:
# 		nextDistrict(d)
# 		for i in range(0, len(itemList)):
# 			nextItem(i)
		

# time.sleep(3)
# driver.quit()
# ------------------------------

# GET PHONE NUMBER - NAVER - TEST

# unopen Chrome
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# driver = webdriver.Chrome('chromedriver',options=options)

# open Chrome
# driver = webdriver.Chrome()
# driver.implicitly_wait(3)

# driver.get('https://land.naver.com/')

# LOGIN
# login_link = driver.find_element_by_id('gnb_login_button')
# login_link.click()
# time.sleep(3)

# driver.find_element_by_xpath('//*[@id="id"]').click()
# driver.execute_script("document.getElementById('id').value = 'tmy7767'")
# driver.execute_script("document.getElementById('pw').value = 'tmy12358970'")
# login = driver.find_element_by_id('log.login')
# login.click()
# 

# 경기도 - 안산시 - 상록구
# show_list = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div[1]/div[1]/p/a')
# show_list.click()
# time.sleep(2)
# kg = driver.find_element_by_xpath('//*[@id="cityList"]/ul/li[2]/a')
# kg.click()
# time.sleep(1)
# asg = driver.find_element_by_xpath('//*[@id="dvsnList"]/ul/li[23]/a')
# asg.click()
# time.sleep(1)
# spd = driver.find_element_by_xpath('//*[@id="secList"]/div/ul/li[6]/a')
# spd.click()
# time.sleep(1)
# btn = driver.find_element_by_xpath('//*[@id="loc_list"]/div[4]/p[2]/a')
# btn.click()
# time.sleep(1)
# # 

# togi = driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/a[4]')
# togi.click()
# time.sleep(1) 
# for i in range(1, 100):
# 	item = driver.find_element_by_css_selector('div:nth-child('+str(i)+') > div > a.item_link')
# 	item.click()
# 	time.sleep(2)
# 	phone = driver.find_element_by_css_selector('dl.info_agent:nth-child(2) > dd').text
# 	print(phone)

# driver.quit()



# show_list = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div[1]/div[1]/p/a')
# show_list.click()
# time.sleep(1)
# kg = driver.find_element_by_xpath('//*[@id="cityList"]/ul/li[2]/a')
# kg.click()
# time.sleep(1)
# asg = driver.find_element_by_xpath('//*[@id="dvsnList"]/ul/li[23]/a')
# asg.click()
# time.sleep(1)
# spd = driver.find_element_by_xpath('//*[@id="secList"]/div/ul/li[6]/a')
# spd.click()
# time.sleep(1)
# results = driver.find_element_by_xpath('//*[@id="loc_list"]/div[4]/p[1]')
# print(results.text)

# driver.quit()









# driver.get('http://www.letsego.site')

# posts = driver.find_elements_by_css_selector('div.card--container')
# post_list = []

# csvFile = open('sego.csv', 'w')

# for post in posts:
#     name = post.find_element_by_css_selector('a > div > p').text
#     title = post.find_element_by_css_selector('a > ul.card--wrapper > li.card--title').text
#     content = post.find_element_by_css_selector('a > ul.card--wrapper > pre.card--content').text.strip()
#     post_list.append({
#     	'name' : name,
#     	'title': title,
#     	'content': content
#     	})
# driver.quit()
# try:
# 	writer = csv.writer(csvFile)
# 	writer.writerow(['닉네임', '제목', '내용'])
# 	for post in post_list:
# 		print(post['name'])
# 		print(post['title'])
# 		print(post['content'])
# 		writer.writerow((post['name'], post['title'], post['content']))
# finally:
# 	csvFile.close()





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


# 
# 네이버 크롤러 만들기
# 

# class Crawler:

# 	def getPage(self, url):
# 		try:
# 			req = requests.get(url)
# 		except requests.exceptions.RequestException:
# 			return None
# 		return BeautifulSoup(req.text, 'html.parser')


# 	def search(self, area, site):
# 		"""
# 		검색 지역으로 나온 결과를 담는다
# 		"""

# class Content:
# 	"""
# 	페이지 전체 사용 기반 클래스
# 	"""
# 	def __init__(self, topic, url, title, body):
# 		# self.topic = topic
# 		# self.url = url
# 		# self.title = title
# 		# self.body = body

# 	def print(self):
# 		"""
# 		출력 결과를 원하는 대로 바꿀 수 있는 함수
# 		"""
# 		# print('New article found for topic {}'.format(self.topic))
# 		# print('URL: {}'.format(self.url))
# 		# print('TITLE: {}'.format(self.title))
# 		# print('BODY: \n{}'.format(self.body))

# class Website:




# # 크롤러 실제 사용 테스트
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