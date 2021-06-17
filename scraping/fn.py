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

def post_save(post_id, category, title, content, created_date, link):
	cur.execute(
		'INSERT INTO naver_post (post_id, category, title, content, created_date, link) VALUES (%s, %s, %s, %s, %s, %s)',
		(post_id, category, title, content, created_date, link)
	)
	cur.connection.commit()

# USER
payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
  'Referer': 'https://apis.naver.com/',
  'cookie': 'NID_AUT=E+4QhvIhxFfc+sNaRX3LxBxS9NQPpK1epH+UtEstJ13QwhB3aZW8VtlnCtfHhLVo; NID_SES=AAABk2NnrqkevXufdsIWmK2uXWcaUI4qwrWBx6YqudKIT+rbkY97ndl44XegPbAGlW+2cpK/dKLnYZOlyCb3EHeQ52v4YFxbhVzobzBXJys7NLBPUGuBevH3JNRpnw6Zk0bFIONfJIqU6sxveGNZHvzZXVRS333FB3Za8wqm+SLNryUIMVex4mbiNL1bBNvGMIrVOrl55dTX6Ar+3rWQYuWqmeY0zOKGbZUoH/IokZrGQMHupDSJqgMHjwMKPy1AZ0w6Tik+fAd4UDHUuNTAJ0BVp2+rD4MxucGKcCm+dVMEXQUBP3Hvth7FxcS/y//RTWDwJcd7X8rbRCjuJOzuF9ffhOfWFZiaH21xLlJ5QPxzeadcPv7OwCm0d28Ue2nD0OhSBNfcbOdaMvDi27kMdYoCrAHt8oZ5FHtG1zZ4Qlb4OwTqJlz6KMDVjuu83zpOIz8qb8pd2D7nq7jwaXpWsXT3Jm/aiQvXnuvHMyQIugyqWX1AkBEIvjq5CiZs7dbggiss8tvYoVXPCEdD41kCFeqJtBv7iOSS2GNIpdreRx/0+2jQ'
}

# KEYWORD
keyword = '%ED%94%8C%EB%9E%A9%ED%92%8B%EB%B3%BC'
keyword.encode('utf-8')

# '%Y%m%d %H:%M'
today = datetime.today().strftime('%Y%m%d')
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime('%Y%m%d')
# print(yesterday, ' TO ', today)
# LIST 
blog_urls = []
cafe_urls = []

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

def get_post_url(index):
	index = str(index)
	# print('index', index)
	url = 'https://s.search.naver.com/p/review/search.naver?rev=44&where=m_view&api_type=2&start='+index+'&query='+keyword+'&nso=so:dd,p:from'+yesterday+'to'+today+'&_callback=jQuery22408904023140404929_1623601229725'
	# print(url)
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	blog_hrefs = bs.findAll('a', href = re.compile('(https://m.blog.naver.com/)[^A-Z]*/'))
	cafe_hrefs = bs.findAll('a', href = re.compile('(https://m.cafe.naver.com/)[^A-Z]*/'))
	global blog_urls
	global cafe_urls
	blog_urls = []
	cafe_urls = []
	for href in blog_hrefs:
		if href.attrs['href'].replace('\\"','').replace(' ','') not in blog_urls:
			blog_urls.append(href.attrs['href'].replace('\\"','').replace(' ',''))
	for href in cafe_hrefs:
		if href.attrs['href'].replace('\\"','').replace(' ','') not in cafe_urls:
			cafe_urls.append(href.attrs['href'].replace('\\"','').replace(' ',''))
	# print('blog : ', len(blog_urls))
	# print(blog_urls)
	# print('cafe : ', len(cafe_urls))
	# print(cafe_urls)
	# return url_list

def get_blog_post(url):
	category = 'blog'
	# print('===============주소===============')
	# print(url)
	post_id = url.split('/')[4]
	# 
	html = urlopen(url)
	bs = BeautifulSoup(html, 'html.parser')
	# print(bs)
	# 최근 블로그
	try:
		# DATE
		date = bs.find('p', {'class': 'blog_date'}).text
		if '시간' in date:
			time = date.replace('시간 전', '')
			time = int(time)
			time = -time
			now = datetime.now()
			date = now + timedelta(hours=time)
			date = str(date)
			date = date[:16]
		elif '분' in date:
			time = date.replace('시간 전', '')
			time = int(time)
			time = -time
			now = datetime.now()
			date = now + timedelta(minutes=time)
			date = str(date)
			date = date[:16]
		else:
			dates = date.split('.')
			date_arr = []
			for date in dates:
				date_arr.append(date.replace(' ','').replace('\n\t', ''))
			date = str(date_arr[0]+'-'+date_arr[1]+'-'+date_arr[2]+' '+date_arr[3])
			# print('before', date)
		date = datetime.strptime(date,'%Y-%m-%d %H:%M')
		# CONTENT
		try:
			title = bs.find('div', {'class': 'se-module se-module-text se-title-text'}).text
			contents = bs.findAll('div', {'class': 'se-module se-module-text'})
			# print('===============제목===============')
			# print(date)
			# print(title)
			# print('===============내용===============')
			arr = []
			for content in contents:
				arr.append(content.get_text())
			content = ''.join(arr)
			# print(content)

			# IMAGE
			try:
				images = bs.findAll('img')
				for img in images:
					if 'https://mblogthumb-phinf.pstatic.net' in img.attrs['src']:
						# print(img.attrs['src'].replace('_blur', '0'))
			except:
				pass
			post_save(post_id, category, title, content, date, url)


		except:
			title = bs.find('h3').text
			content = bs.find('p', {'class': 'se_textarea'}).text
			# print('===============제목===============')
			# print(date)
			# print(title)
			# print('===============내용===============')
			# print(content)
			post_save(post_id, category, title, content, date, url)

	# 아니라면
	except:
		date = bs.find('p', {'class': 'se_date'}).text
		dates = date.split('.')
		date_arr = []
		for date in dates:
			date_arr.append(date.replace(' ','').replace('\n\t', ''))
		date = str(date_arr[0]+'-'+date_arr[1]+'-'+date_arr[2]+' '+date_arr[3])
		# print('before', date)
		date = datetime.strptime(date,'%Y-%m-%d %H:%M')
		title = bs.find('h3').text
		content = bs.find('div', {'id': 'viewTypeSelector'}).text
		# print('===============제목===============')
		# print(date)
		# print(title)
		# print('===============내용===============')
		# print(content)
		post_save(post_id, category, title, content, date, url)

	# 
	# print('===============태그===============')
	try:
		tags = bs.findAll('span', {'class': 'ell'})
		for tag in tags:
			if "#" in tag.text[0]:
				tag = tag.text
				tag = tag.replace('#','')
				# print(post_id, tag)
				# store_tag(post_id, tag)
	except:
		# print('NONE TAG')
		pass
	# SENT COMMENT
	user_name = url.split('/')[3]
	get_blog_post_comment(user_name, post_id)

def get_blog_post_comment(user_name, post_id):
	# print('COMMENT START')
	# print('SECCESS', user_name, post_id)
	url = 'https://blog.naver.com/PostList.nhn?blogId='+user_name
	html = urlopen(url)
	bs = BeautifulSoup(html.read(), 'html.parser')
	scripts = bs.findAll("script")
	for script in scripts:
		if "blogNo" in script.text:
			text = script.text
			var = text.split("var")
			for v in var:
				if "blogNo" in v:
					blog_no = v.split("'")[1]
	api_url = 'https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=blog&templateId=default&pool=cbox9&lang=ko&objectId='
	content_no = post_id
	object_id = blog_no + '_201_' + content_no
	api_url = api_url + object_id + '&groupId=' + blog_no
	res = requests.get(api_url, headers=headers)
	res = res.text
	res = res[10:]
	a = res.find(');')
	res = res[:a]
	res = json.loads(res)
	# print('===============댓글===============')
	try:
		comment_count = res['result']['count']['total']
		# print('댓글 수 : ', comment_count)
	except:
		# print('DONT COMMENT')
	# 
	try:
		comments = res['result']['commentList']
		for comment in comments:
			if comment['contents'] == "": 
				# print('숨김')
			else:
				content = comment['contents'].replace('<br>','')
				dates = comment['modTime'].replace('T', ' ')
				date = dates[:16]
				# print(date)
				created_date = datetime.strptime(date,'%Y-%m-%d %H:%M')
				# print(created_date)
				# print(post_id, content, created_date)
				# store_comment(post_id, content, created_date)
	except:
		pass
	# print('POST END')

def get_cafe_post(url):
	category = 'cafe'
	# print('===============주소===============')
	# print(url)
	link = url
	url = url[25:]
	find_cafe_index = url.find('/')
	# find_art_index = url.find('?')
	find_code_index = url.find('=')
	cafe_nm = url[:find_cafe_index]
	cafe_id = url[find_cafe_index+1:]
	cafe_code = url[find_code_index+1:]
	cafe_code = cafe_code.replace('=', '%3D')
	buid = '8957b977-a4ae-4cae-b947-5d0be546d7db'
	# api_url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/{}/articles/{}?useCafeId=false&art={}&query={}'.format(cafe_nm, cafe_id, cafe_code, keyword)
	api_url = 'https://apis.naver.com/cafe-web/cafe-articleapi/v2/cafes/{}/articles/{}?useCafeId=false&buid={}'.format(cafe_nm, cafe_id, buid)
	# print(api_url)
	req = requests.get(api_url, headers=headers, data=payload).json()
	try:
		req = requests.get(api_url, headers=headers, data=payload).json()
		# print('===============POST===============')
		post_id = str(req['result']['article']['id'])
		# print(post_id)
		# print('===============날짜===============')
		date = str(req['result']['article']['writeDate'])
		date = date[:10]
		date = datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d %H:%M:%S')
		# print(date)
		# print('===============제목===============')
		title = req['result']['article']['subject']
		# print(title)
		content_html = req['result']['article']['contentHtml']
		content = BeautifulSoup(content_html, 'html.parser')
		# IMAGE
		try:
			images = content.findAll('img')
			for img in images:
				if 'https://cafeptthumb-phinf.pstatic.net' in img.attrs['src']:
					# print(img.attrs['src'].replace('_blur', '0'))
		except:
			pass
		# print('===============내용===============')
		content = content.get_text()
		content = content.strip()
		content = content.replace('\n','')
		# print(content)
		# 
		# store_post(post_id, category, title, content, date, link)
		# 
		# print('===============댓글===============')
		comment_list = req['result']['comments']['items']
		for comment in comment_list:
			comment_content = comment['content']
			# print(comment_content)
			comment_date = str(comment['updateDate'])
			comment_date = comment_date[:10]
			comment_date = datetime.fromtimestamp(int(comment_date)).strftime('%Y-%m-%d %H:%M:%S')
			# print(comment_date)
			# store_comment(post_id, comment_content, comment_date)
	except:
		pass

# total = get_total(1)
# print('total : ', total)
# index = 1
# while index <= total:
# 	get_post_url(index)
# 	for url in blog_urls:
# 		get_blog_post(url)
# 	for url in cafe_urls:
# 		get_cafe_post(url)
# 	index += 15

def scraping_start():
	print('START FUNCTION')
	total = get_total(1)
	# print('total : ', total)
	index = 1
	while index <= total:
		get_post_url(index)
		for url in blog_urls:
			get_blog_post(url)
		for url in cafe_urls:
			get_cafe_post(url)
		index += 15	











