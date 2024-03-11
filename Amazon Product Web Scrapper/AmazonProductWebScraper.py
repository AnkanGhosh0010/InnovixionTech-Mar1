#Amazon Product Web Scraper
#Author:  Ankan Ghosh | 9.3.24 | 
'''
Amazon pruduct web scraper would get the http request from the requests library then
beautifulSoup library would parse the elements show the product name,price and 
reviews of our desired page and accumulate the data to an Excel sheet using openpyxl library
'''

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# add your user agent (YOU MUST CHANGE THE USER AGENT: "https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
# URL of Amazon page to scrape
url = 'https://www.amazon.in/s?k=laptop&crid=3KC5Z7L8A0IZZ&sprefix=laptop+%2Caps%2C218&ref=nb_sb_noss_2'

# HTTP request
response = requests.get(url,headers=HEADERS)

# Parse HTML content 
soup = BeautifulSoup(response.content, 'html.parser')

# all div elements of the products
products = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2v5pwx3nl8aar2aoxf0782v1pf s-latency-cf-section puis-card-border')

# Excel workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Write headers to the first row of the worksheet
ws.append(['Product Name', 'Price', 'Reviews'])

# Loop through the product divs and extract information
for product in products:
    #for product name
    try:
        product_name = product.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
    except AttributeError:
        product_name = '-'
    
    #for product price
    try:
        product_price = product.find('span', class_='a-price-whole').text.strip()
    except AttributeError:
        product_price = '-'

    #for product review
    try:
        product_reviews = product.find('span', class_='a-icon-alt').text.strip()
    except AttributeError:
        product_reviews = '-'

    # extracted information to the worksheet
    ws.append([product_name, product_price, product_reviews])

# Saving the workbook to an excel file
wb.save('AmazonProductsLIST.xlsx')
