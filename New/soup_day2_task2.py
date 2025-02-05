# Extract Meta Information from a Webpage
import requests
from bs4 import BeautifulSoup

url = "https://www.dekorcompany.com/?srsltid=AfmBOorLrgrkh8pwGqeXw5JpK9wUFm_r7eTwfFquIIKm8Q4BF37Uz5gO" 
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

meta = soup.find_all("meta")

meta_content = soup.find('meta', {'name' : 'description'})
if meta_content:
    print(meta_content['content'])
else:
    print("No meta description found.")

