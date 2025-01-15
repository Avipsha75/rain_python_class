import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
responses = requests.post(url, json={"name": "John Doe", "username": "johndoe", "email": "johndoe@example.com"})

if response.status_code == 200:
    print("Data fetched successfully!\n")
    #Parsew the JSON data
    data = response.json()

    #Display the first 3 posts
    for post in data[:3]:
        print(f"Name: {post['name']}")
        print(f"Username: {post['username']}")
        print(f"Email: {post['email']}\n")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")

if responses.status_code == 201:
    print("Data added successfully!\n")
    #Parsew the JSON data
    data = responses.json()

    #Display the first 3 posts
    for post in data[:3]:
        print(f"Name: {post['name']}")
        print(f"Username: {post['username']}")
        print(f"Email: {post['email']}\n")
else:
    print(f"Failed to add data. Status Code: {responses.status_code}")
