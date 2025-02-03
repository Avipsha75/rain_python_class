import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"

response = requests.get(url)

if response.status_code == 200:
    print("Trending Repositories fetched successfully!\n")

    data = response.json()

    for repo in data['items'][:10]:
        name = repo['name']
        owner =repo['owner']['login']
        description = repo.get('description', 'No description available')
        stars = repo['stargazers_count']
        print(f"Repo Name: {name}\nOwnwer: {owner}\nStars: {stars}\nDescription: {description}\n")
else:
    print(f"Failed to retrieve trending repositories. Status Code: {response.status_code}")