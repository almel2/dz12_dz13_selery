from time import sleep

from celery import shared_task
from django.core.mail import send_mail as django_send_mail


@shared_task
def mail(email, text):
    django_send_mail('Remind me', text, 'sashakuznecova2016@gmail.com', [email])

@shared_task()
def add(x, y):
    sleep(5)
    return x + y

