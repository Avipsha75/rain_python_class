import requests
 
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully!\n")
    
    data = response.json()

    for post in data[:5]:
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")