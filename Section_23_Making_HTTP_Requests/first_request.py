import requests

url = "http://www.google.com"
response = requests.get(url)
print(f"You request to {url} came back with status code {response.status_code}")
print(response.text)
