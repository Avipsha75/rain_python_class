# Scrapes and Save Images from websites
import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.dekorcompany.com/?srsltid=AfmBOorLrgrkh8pwGqeXw5JpK9wUFm_r7eTwfFquIIKm8Q4BF37Uz5gO"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

img_tag = soup.find("img")

if img_tag and img_tag.get("src"):
    img_url = img_tag["src"]

    if not img_url.startswith("http"):
        from urllib.parse import urljoin
        img_url = urljoin(url, img_url)

    img_data = requests.get(img_url).content
    with open("scraped_image.jpg", "wb") as f:
        f.write(img_data)

    print("Image saved successfully!")
else:
    print("No image found.")

