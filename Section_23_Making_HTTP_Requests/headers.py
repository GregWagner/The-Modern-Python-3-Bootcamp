import requests

url = "https://icanhazdadjoke.com/"
#response = requests.get(url, headers={"Accept": "text/plain"})
#print(response.text)
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()      # this is a dict
print(data['joke'])
