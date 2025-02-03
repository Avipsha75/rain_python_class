import requests
from bs4 import BeautifulSoup

url = "https://edition.cnn.com/2025/02/03/africa/trump-aid-cut-threat-south-africa-intl/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

code = soup.find_all('h1', class_='headline_text inline-placeholder vossi-headline-text')
# print(code)

print ("All the links are: ")
for i in code:
    print(i.get('text'))