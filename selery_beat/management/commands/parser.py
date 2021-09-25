from django.core.management import BaseCommand
from bs4 import BeautifulSoup
import requests

from selery_beat.models import Author, Quote

site = 'https://quotes.toscrape.com/'


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
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
                        Author.objects.get(name=author_name)

                    Quote.objects.get_or_create(quote=quote, author=Author.objects.get(name=author_name))

                    quotes_num -= 1

                    quotes_num = 0
                    break
            print('ok')