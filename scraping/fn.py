from datetime import datetime, timedelta, timezone
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import time
import json
import re

# SSL
import  os, ssl
if  ( not  os.environ.get ( 'PYTHONHTTPSVERIFY', '') and getattr (ssl, '_create_unverified_context', None)) : 
	ssl._create_default_https_context =  ssl._create_unverified_context

# MYSQL
import pymysql
host = 'sego.c3jqlg47t2v5.ap-northeast-2.rds.amazonaws.com'
user = 'sego_admin'
pw = 'googie0126!'
db = 'sego'
conn = pymysql.connect(host=host, user=user, passwd=pw, db=db, charset='utf8')
cur = conn.cursor()
cur.execute('USE sego')

def store_post(params):
	cur.execute(
		'INSERT INTO table (params) VALUES (%s)',
		(params)
	)
	cur.connection.commit()

# USER
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
  'Referer': 'https://apis.naver.com/'
}

# KEYWORD
keyword = '%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC'
keyword.encode('utf-8')

# '%Y%m%d %H:%M'
today = datetime.today().strftime('%Y%m%d')
yesterday = datetime.today() - timedelta(days=3)
yesterday = yesterday.strftime('%Y%m%d')

# LIST 
url_list = []

def get_total(index):
	index = str(index)
	url = 'https://s.search.naver.com/p/review/search.naver?rev=44&where=m_view&api_type=2&start='+index+'&query='+keyword+'&nso=so:dd,p:from'+yesterday+'to'+today+'&_callback=jQuery22408904023140404929_1623601229725'
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser').text
	f1 = bs.find(':')
	bs = bs[f1+1:]
	f2 = bs.find(',')
	bs = bs[:f2]
	total = bs.replace(' ', '')
	return int(total)

def get_post(index):
	index = str(index)
	url = 'https://s.search.naver.com/p/review/search.naver?rev=44&where=m_view&api_type=2&start='+index+'&query='+keyword+'&nso=so:dd,p:from'+yesterday+'to'+today+'&_callback=jQuery22408904023140404929_1623601229725'
	print(url)
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	print(bs)
	blog_hrefs = bs.findAll('a', href = re.compile('(https://m.blog.naver.com/)[^A-Z]*/'))
	cafe_hrefs = bs.findAll('a', href = re.compile('(https://m.cafe.naver.com/)[^A-Z]*/'))
	print('blog : ', len(blog_hrefs))
	print('cafe : ', len(cafe_hrefs))
	# global url_list
	# url_list = []
	# for href in hrefs:
	# 	if href.attrs['href'].replace('\\"','').replace(' ','') not in url_list:
	# 		url_list.append(href.attrs['href'].replace('\\"','').replace(' ',''))
	# return url_list

total = get_total(1)
print('total : ', total)
index = 1
while index <= total:
	get_post(index)
	# for url in url_list:
	# 	getBlogPost(url)
	index += 15

















