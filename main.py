import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint
file = open('data.csv', 'w', newline='\n')
write_object = csv.writer(file)

page = 1

for page in range(6):
    url = f'https://books.toscrape.com/catalogue/category/books_1/page-{page}.html'
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')

    all_book = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")



    for book in all_book:
        book_article = book.find('article')
        title = book_article.h3.text
        price = book_article.find('p', class_='price_color').text
        write_object.writerow([title, price])
        # print(price)
time.sleep(randint(15, 20))


