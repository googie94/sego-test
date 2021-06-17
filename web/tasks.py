from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app
# 
from scraping import fn

@app.task
def naver_scraping():
	fn.scraping_start()