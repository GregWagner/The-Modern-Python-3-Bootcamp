from card import Card
from random import shuffle

class Card(object):

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck(object):

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        deck_size = self.count()
        if deck_size == 0:
            raise ValueError("All cards have been delt")

        number = deck_size if number > deck_size else number

        hand = self.cards[-number:]
        self.cards = self.cards[:-number]
        return hand

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only fill decks can be shuffled")
        shuffle(self.cards)
        return self
                    
    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


# Deck of 52 cards.
my_deck = Deck()
print(my_deck)

my_deck.shuffle()
print(my_deck)

