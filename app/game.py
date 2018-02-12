from app.player import Player
from app.deck import Deck


class Game:
    round_counter = 0

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        return

    def round(self):
        self.round_counter += 1
        print("Round {} started".format(self.round_counter))

        if not self.deck.get_cards():
            self.deck = Deck()

        self.deck.shuffle()

        self.player.hit(self.deck.deal())
        self.dealer.hit(self.deck.deal())
        self.print_state()

        while self.player.playing:
            if self.player.calc_hand() > 21:
                print("You have too much :(")
                self.player.stop()
                break

            choice = input("[hit] or [stay]? ")
            while choice not in {"hit", "stay"}:
                choice = input("[hit] or [stay]? ")
            if choice == "hit":
                self.player.hit(self.deck.deal())
            if choice == "stay":
                self.player.stop()
            self.print_state()

        if not self.player.calc_hand() > 21:
            while self.dealer.calc_hand() < 17:
                self.dealer.hit(self.deck.deal())
                self.print_state()
            self.dealer.stop()

        winner = self.get_winner()
        if winner == self.player:
            print("Player won!")
        elif winner == self.dealer:
            print("Dealer won")
        else:
            print("Push")

    def print_state(self):
        print("Player's hand is:")
        self.player.print_hand()

        print("Dealer's hand is:")
        self.dealer.print_hand()

        print("Actual score is: {}:{}".format(self.player.calc_hand(), self.dealer.calc_hand()))

    def get_winner(self):
        if self.player.calc_hand() > self.dealer.calc_hand() and not self.player.calc_hand() > 21:
            return self.player
        elif self.player.calc_hand() < self.dealer.calc_hand() or self.player.calc_hand() > 21:
            return self.dealer
        else:
            return None
