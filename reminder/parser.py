import requests
from bs4 import BeautifulSoup
q = []
url = 'https://quotes.toscrape.com/'
r = requests.get(url)
soup =BeautifulSoup(r.text, 'html.parser')
print(soup)
for span in soup.find('span', {'itemprop' 'text'}):
    pass
