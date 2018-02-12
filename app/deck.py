import random

class Deck:
    def __init__(self):
        self._cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        return
    
    def shuffle(self):
        random.shuffle(self._cards)
        print("Deck shuffled")

    def take_card(self):
        return self._cards.pop(0)