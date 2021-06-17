from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app
# 
from scraping.fn import scraping_start

@app.task
def naver_scarping():
	scarping_start()