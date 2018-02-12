from app.deck import Deck

class Game:
    def __init__(self):
        self._deck = Deck()
        return

    def run(self):
        print("Game started")
        self._deck.shuffle()
        card = self._deck.take_card()
        print(card)