class Player:
    def __init__(self):
        self.hand = []
        self.playing = True
        self.wins = 0

    def get_hand(self):
        return self.hand

    def reset_hand(self):
        self.hand = []

    def calc_hand(self):
        result = 0

        hand = list(self.hand)
        aces = []

        for card in hand:
            if card.name == "A":
                aces.append(card)
                hand.remove(card)

        for card in hand:
            result += card.value

        for ace in aces:
            if result > 10:
                result += ace.value
            else:
                result += ace.value + 10

        return result

    def hit(self, card):
        self.hand.append(card)

    def print_hand(self):
        for card in self.hand:
            print("\t{} of {}".format(card.name, card.suit))
