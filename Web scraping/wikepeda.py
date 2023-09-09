import requests
from bs4 import BeautifulSoup

def scrape_product_price(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price_element = soup.find('div', {'class': 'mw-parser-output'})
    
    price = price_element.text.strip()
    
    return price

product_url = 'https://en.wikipedia.org/wiki/Arrests_of_Ulysses_S._Grant'

product_price = scrape_product_price(product_url)

print("Product Price:", product_price)
