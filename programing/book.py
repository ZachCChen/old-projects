import requests
from bs4 import BeautifulSoup

Book = []
Book_Price = []

response = requests.get('https://books.toscrape.com/')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
book_titles = soup.find_all('h3')
prices = soup.find_all('p', class_='price_color')

for title in book_titles:
    Book.append(title.text.strip().encode('utf-8').decode('utf-8'))

for price in prices:
    Book_Price.append(price.text.strip().encode('utf-8').decode('utf-8'))

for i in range(len(Book)):
    print(Book[i], Book_Price[i])