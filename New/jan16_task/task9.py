import requests

url= "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "New Post",
    "body": "This is my new post.",
    "userId": "Avi"
}

response = requests.post(url, json = data)