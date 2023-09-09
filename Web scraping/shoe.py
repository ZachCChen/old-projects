import requests
from bs4 import BeautifulSoup

def scrape_product_price(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price_element = soup.find('div', {'class': 'product-price is--current-price css-s56yt7 css-xq7tty'})
    
    price = price_element.text.strip()
    
    return price

product_url = 'https://www.nike.com/t/air-jordan-1-mid-mens-shoes-b3js2D/DQ8426-517?nikemt=true&cp=34492719349_search_%7CPRODUCT_GROUP%7CGOOGLE%7C71700000088292143%7CAll_X_X_X_X-Device_X_Nike-Clearance_X_SSC%7C%7Cc&gclid=CjwKCAjw67ajBhAVEiwA2g_jEBeLWHrKbmzmfJhFt_k_zSlg2a2UHFUyBucZvj-gLsr1tHvL2QzbZxoCBy8QAvD_BwE&gclsrc=aw.ds'

product_price = scrape_product_price(product_url)

print("Product Price:", product_price)
