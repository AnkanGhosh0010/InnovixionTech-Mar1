#Basic Web Scraper
#Author:  Ankan Ghosh | 9.3.24 | Innovixion Tech Task 1
'''
Create a simple web scraper that extracts information from a
website and presents it in a structured form.
_____________________________________________________________
SCRAPING MY OWN BLOG PAGE
'https://zeusweb0010.blogspot.com/2022/10/what-is.html#more'
'''
import requests
from bs4 import BeautifulSoup
from docx import Document

# URL of Website
url = 'https://zeusweb0010.blogspot.com/2022/10/what-is.html#more'

# HTTP request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Print the HTML code in TXT file
with open('htmlCODEBasicWebScrapper.txt', 'w',encoding='utf-8') as f:
    print("HTML CODE:\n\n\n", soup.prettify(), file=f)
    
post_header = soup.find('h3', class_='post-title entry-title')
post_body = soup.find('div', class_='post-body entry-content float-container')

post_header_text = post_header.get_text(strip=True) if post_header else ''
post_body_text = post_body.get_text(strip=True,separator='\n') if post_body else ''

combined_text = post_header_text + '\n\n' + post_body_text

# Create a new Word document
doc = Document()
doc.add_paragraph(combined_text)

# Save the document
doc.save('BasicWebScrapper.docx')