import os

from celery import Celery




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dz12_dz13_selery.settings')

app = Celery('dz12_dz13_selery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()