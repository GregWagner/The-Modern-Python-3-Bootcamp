import unittest
from card import Card
from deck import Deck

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Spades")

    def test_init(self):
        self.assertEqual(self.card.suit, "Spades")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        self.assertEqual(repr(self.card), "A of Spades")


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")

    def test_count(self):
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        card = self.deck.cards[-1]
        delt_card = self.deck.deal_card()
        self.assertEqual(card, delt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)


if __name__ == "__main__":
    unittest.main()
