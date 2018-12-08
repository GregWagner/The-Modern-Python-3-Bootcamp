import requests
import random
from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format("Dad Joke 3000")
colored_ascii = colored(ascii_art, color="green")
print(colored_ascii)

print("Let me tell you a joke!")
topic = input("Enter a subject: ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params = {"term": topic}
)

data = response.json()      # this is a dict
number_of_jokes = len(data['results'])

if number_of_jokes:
    print(f"I know {number_of_jokes} jokes on that subject. Here is one:")
    joke = random.randint(0, number_of_jokes)
    print(data['results'].pop(joke)['joke'])
else:
    print("Sorry I don't know any jokes on that topic")

