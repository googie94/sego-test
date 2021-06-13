from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .celery import app

@app.task
def sum(x, y):
    return x + y
