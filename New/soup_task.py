import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

code = soup.find_all('a')
# print(code)

print ("All the links are: ")
for i in code:
    print(i.get('href'))
   

