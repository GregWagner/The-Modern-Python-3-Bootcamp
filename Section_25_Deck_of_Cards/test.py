from deck import Deck

# Deck of 52 cards.
my_deck = Deck()
print(my_deck)

my_deck.shuffle()
print(my_deck)

# A of Hearts
card = my_deck.deal_card()
print(card)

#[8 of Spades, 10 of Clubs, 6 of Spades, 10 of Diamonds, Q of Spades]
hand = my_deck.deal_hand(5)
print(hand)

# Deck of 46 cards.
print(my_deck)
