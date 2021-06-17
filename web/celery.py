from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import datetime, timedelta
from celery.schedules import crontab
from scraping.fn import scraping_start

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

app = Celery('web')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
# 	'every-15-seconds' : {
# 		'task': 'web.tasks.hello',
# 		'schedule': crontab(minute='*'),
# 		'args': ('googie',)
# 	}
# }

app.autodiscover_tasks()


@app.task
def naver_scraping():
	scraping_start()

@app.task(bind=True)
def debug_task(self):
    print('Request : {0!r}'.format(self.request))
