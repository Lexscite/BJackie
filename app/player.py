class Player:
    def __init__(self):
        self.hand = []
        self.playing = True

    def get_hand(self):
        return self.hand

    def reset_hand(self):
        self.hand = []

    def calc_hand(self):
        result = 0
        for card in self.hand:
            result += card.value
        return result

    def hit(self, card):
        self.hand.append(card)

    def stop(self):
        self.playing = False

    def print_hand(self):
        for card in self.hand:
            print("\t{} of {}".format(card.name, card.suit))
