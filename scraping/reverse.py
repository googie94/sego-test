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
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2MTkwNTk0NTIsImV4cCI6MTYxOTA3MDI1Mn0.LmoSIYnvrDWYsXvKYJGEgkX7ELW8IvgL5Mb9IxFz8Qo'
}

# AREAGROUP
def getAreaGroup(api):
	req = requests.get(api, headers=headers, data=payload).json()
	time.sleep(random.uniform(1,4))
	global areaGroupList
	areaGroupList = req["regionList"]
	return areaGroupList

# AREA
def getArea(api):
	req = requests.get(api, headers=headers, data=payload).json()
	time.sleep(random.uniform(3,10))
	global areaList
	areaList = req["regionList"]
	return areaList

# AREADETAIL
def getAreaDetail(api):
	req = requests.get(api, headers=headers, data=payload).json()
	time.sleep(random.uniform(3,10))
	global areaDetailList
	areaDetailList = req["regionList"]
	return areaDetailList

api = "https://new.land.naver.com/api/regions/list?cortarNo=0000000000"
getAreaGroup(api)
# print(areaGroupList)

results = []
for ag in areaGroupList[::-1]:
	api = "https://new.land.naver.com/api/regions/list?cortarNo={}".format(ag["cortarNo"])
	getArea(api)
	# print(areaList)
	for a in areaList:
		api = "https://new.land.naver.com/api/regions/list?cortarNo={}".format(a["cortarNo"])
		getAreaDetail(api)
		# print(areaDetailList)
		for ad in areaDetailList:
			# 
			print(ad)
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
				req = requests.get(api, headers=headers, data=payload).json()
				time.sleep(random.uniform(1,4))
				# test = req.json()
				if req["isMoreData"] == False:
					break;
				else:
					for t in req["articleList"]:
						# print(t["articleNo"])
						results.append(t["articleNo"])
					# 
					print("ITEM LENGTH : ", len(results))
					# 
					if len(results) != 0:
						for index, r in enumerate(results):
							print('----------------------')
							print("ITEM INDEX : ", index)
							print("INST NUM : ", r)
							try:
								# print("INST NUM : ", r)
								api = "https://new.land.naver.com/api/articles/{}".format(r)
								req = requests.get(api, headers=headers, data=payload).json()
								time.sleep(random.uniform(3,6))
								ag = req["articleDetail"]["cityName"]
								a = req["articleDetail"]["divisionName"]
								d = req["articleDetail"]["sectionName"]
								ph = req["articleRealtor"]["cellPhoneNo"]
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
