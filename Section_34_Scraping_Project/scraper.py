import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Now scraping {BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"] 
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        #sleep(2)
    return all_quotes

def start_game(quotes):
    quote = choice(quotes)
    print("Here's a quote:")
    print(quote["text"])
    print(quote["author"])

    remaining_guesses = 4
    guess = ''
    while guess.lower() != quote["author"].lower() and remaining_guesses:
        guess = input(f"Who said this quote? guesses remaining: {remaining_guesses}: ")
        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            break

        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's hint: The author was born on {birth_date} {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint. The author's first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here's a hint. The author's last name starts with {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ('y', 'yes'):
        return start_game(quotes)
    else:
        print("DONE")

quotes = scrape_quotes()
start_game(quotes)
