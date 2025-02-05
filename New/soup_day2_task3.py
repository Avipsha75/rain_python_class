import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bbc.com/news"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

news = []
for article in soup.find_all("a", class_="gs-c-promo-heading"):
    title = article.get_text(strip=True)
    link = "https://www.bbc.com" + article["href"]
    news.append([title, link])

df = pd.DataFrame(news, columns=["Title", "URL"])
df.to_csv("bbc_news.csv", index=False)

print(df.head())  
