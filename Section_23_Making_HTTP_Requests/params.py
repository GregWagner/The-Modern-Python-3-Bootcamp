import requests

url = "https://icanhazdadjoke.com/search"
#response = requests.get(url, headers={"Accept": "text/plain"})
#print(response.text)
response = requests.get(
    url,
    headers={"Accept": "application/json"}
    params = {"term": "cat", "limit": 1}
)

data = response.json()      # this is a dict
print(data['joke'])
