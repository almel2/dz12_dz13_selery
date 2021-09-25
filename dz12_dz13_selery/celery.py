import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dz12_dz13_selery.settings')

app = Celery('dz12_dz13_selery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'scraping-task': {
        'task': 'selery_beat.tasks.parser',
        #'schedule': crontab(minute=0, hour='1,3,5,7,9,11,13,15,17,19,21,23'),
        'schedule': timedelta(seconds=30),
    }
}