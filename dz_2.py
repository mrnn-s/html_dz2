import requests
print(requests.__version__)

from bs4 import BeautifulSoup
import urllib.parse
import re
import json

base_url = 'http://books.toscrape.com/catalogue/'
url = base_url + 'page-1.html'
page_counter = 1
data = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        book_data = {}

        # Извлечение названия книги
        book_title = article.find('h3').find('a')
        book_data['title'] = book_title['title'] if book_title else ''