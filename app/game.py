from app.player import Player
from app.deck import Deck


class Game:
    round_counter = 0

    def __init__(self, num_decks):
        self.deck = Deck()

        std_deck = list(self.deck.cards)
        for i in range(1, num_decks):
            self.deck.cards += std_deck

        self.player = Player()
        self.dealer = Player()

    def round(self):
        self.round_counter += 1
        if self.round_counter > 1:
            input("Press Enter to start next round...")
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
                self.player.playing = False
                break
            if self.player.calc_hand() == 21:
                print("You have 21!")
                self.player.playing = False
                break

            choice = input("Want to [hit] or [stop]? ")
            while choice not in {"hit", "stop"}:
                choice = input("Wrong command. Want to [hit] or [stop]? ")
            if choice == "hit":
                self.player.hit(self.deck.deal())
            if choice == "stop":
                self.player.playing = False
            self.print_state()

        if not self.player.calc_hand() > 21:
            while self.dealer.calc_hand() < 17:
                self.dealer.hit(self.deck.deal())
                self.print_state()
            self.dealer.playing = False

        winner = self.get_winner()
        if winner == self.player:
            self.player.wins += 1
            print("Player won!")
        elif winner == self.dealer:
            self.dealer.wins += 1
            print("Dealer won")
        else:
            self.player.wins += 1
            self.dealer.wins += 1
            print("Push")

        print("Current win rate is: {:.1%}\n".format(self.player.wins / self.round_counter))

        self.reset()

    def reset(self):
        self.player.playing = True
        self.dealer.playing = True
        self.player.reset_hand()
        self.dealer.reset_hand()

    def print_state(self):
        print("Player's hand is:")
        self.player.print_hand()

        print("Dealer's hand is:")
        self.dealer.print_hand()

        print("Actual score is: {}:{}\n".format(self.player.calc_hand(), self.dealer.calc_hand()))

    def get_winner(self):
        if (self.player.calc_hand() > self.dealer.calc_hand() or self.dealer.calc_hand() > 21)\
                and not self.player.calc_hand() > 21:
            return self.player
        elif self.player.calc_hand() < self.dealer.calc_hand() or self.player.calc_hand() > 21:
            return self.dealer
        else:
            return None
