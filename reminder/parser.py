import requests
from bs4 import BeautifulSoup



site = 'https://quotes.toscrape.com/'
r = requests.get(site)
soup = BeautifulSoup(r.text, 'html.parser')

athors = ['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']

kard =[]


items = soup.find_all('div', class_="quote")

for i in items:
    quote = i.find('span', class_="text").get_text()
    author_name = i.find('small', class_="author").get_text()

    link_detal = i.find('a').get('href')
    url_detal = f'{site}{link_detal}'
    r = requests.get(url_detal)
    soup = BeautifulSoup(r.text, 'html.parser')

    about = soup.find('div', class_='author-description').text.strip()
    #print(about)
    birthday = soup.find('span', class_="author-born-date").text
    #print(birthday)
    birth_loc = soup.find('span', class_="author-born-location").text
    #print(birth_loc)

    if not Author.objects.filter(name=author_name).exists():
        author, created = Author.objects.get_or_create(name=author_name, birthday=birthday, birth_loc=birth_loc, about=about)

    else:
        author = Author.objects.get(name=author_name)

    quote = Quote.objects.create(quote=quote, author=author_name)



