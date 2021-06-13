from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import datetime, timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

app = Celery('web')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request : {0!r}'.format(self.request))


@app.task
def add(x,y):
    return x + y
