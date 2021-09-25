
from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail as django_send_mail

import requests

from .models import Author, Quote


@shared_task
def nothing_to_send(subject, message, receiver):
    django_send_mail(subject, message, 'admin@example.com', [receiver] )



@shared_task
def parser():
    site = 'https://quotes.toscrape.com/'
    quotes_num = 5
    while quotes_num > 0:
        for page in range(1, 11):
            URL = f'{site}/page/{str(page)}/'
            r = requests.get(URL)
            soup = BeautifulSoup(r.text, 'html.parser')

            items = soup.find_all('div', class_="quote")

            for i in items:
                quote = i.find('span', class_="text").get_text()
                author_name = i.find('small', class_="author").get_text()

                link_detal = i.find('a').get('href')
                url_detal = f'{site}{link_detal}'
                r = requests.get(url_detal)
                soup = BeautifulSoup(r.text, 'html.parser')

                about = soup.find('div', class_='author-description').text.strip()
                # print(about)
                birthday = soup.find('span', class_="author-born-date").text
                # print(birthday)
                birth_loc = soup.find('span', class_="author-born-location").text
                # print(birth_loc)

                if not Author.objects.filter(name=author_name).exists():
                    author = Author.objects.create(name=author_name, birthday=birthday, birth_loc=birth_loc,
                                                                   about=about)

                else:
                    author = Author.objects.get(name=author_name)

                #quote = Quote.objects.create(quote=quote, author=author)
                Quote.objects.get_or_create(quote=quote, author=Author.objects.get(name=author_name))

                quotes_num -= 1

                if quotes_num != 0 and i == items[-1] and page == 10:
                    nothing_to_send.delay(subject='Quotes ended', message='Больше нет quetes',
                                          receiver='example@example.com')
                    quotes_num = 0
                    break
