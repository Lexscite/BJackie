import random


class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards = [
            Card("A",  "Spades", 1),  Card("A",  "Clubs", 1),  Card("A",  "Hearts", 1),  Card("A",  "Diamonds", 1),
            Card("2",  "Spades", 2),  Card("2",  "Clubs", 2),  Card("2",  "Hearts", 2),  Card("2",  "Diamonds", 2),
            Card("3",  "Spades", 3),  Card("3",  "Clubs", 3),  Card("3",  "Hearts", 3),  Card("3",  "Diamonds", 3),
            Card("4",  "Spades", 4),  Card("4",  "Clubs", 4),  Card("4",  "Hearts", 4),  Card("4",  "Diamonds", 4),
            Card("5",  "Spades", 5),  Card("5",  "Clubs", 5),  Card("5",  "Hearts", 5),  Card("5",  "Diamonds", 5),
            Card("6",  "Spades", 6),  Card("6",  "Clubs", 6),  Card("6",  "Hearts", 6),  Card("6",  "Diamonds", 6),
            Card("7",  "Spades", 7),  Card("7",  "Clubs", 7),  Card("7",  "Hearts", 7),  Card("7",  "Diamonds", 7),
            Card("8",  "Spades", 8),  Card("8",  "Clubs", 8),  Card("8",  "Hearts", 8),  Card("8",  "Diamonds", 8),
            Card("9",  "Spades", 9),  Card("9",  "Clubs", 9),  Card("9",  "Hearts", 9),  Card("9",  "Diamonds", 9),
            Card("10", "Spades", 10), Card("10", "Clubs", 10), Card("10", "Hearts", 10), Card("10", "Diamonds", 10),
            Card("J",  "Spades", 10), Card("J",  "Clubs", 10), Card("J",  "Hearts", 10), Card("J",  "Diamonds", 10),
            Card("Q",  "Spades", 10), Card("Q",  "Clubs", 10), Card("Q",  "Hearts", 10), Card("Q",  "Diamonds", 10),
            Card("K",  "Spades", 10), Card("K",  "Clubs", 10), Card("K",  "Hearts", 10), Card("K",  "Diamonds", 10),
        ]

    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck shuffled")

    def get_cards(self):
        return self.cards

    def deal(self):
        return self.cards.pop(0)
