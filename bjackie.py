from app.game import Game


def main():
    num_rounds = 5
    num_decks = 6

    game = Game(num_decks)
    for k in range(0, num_rounds):
        game.round()

    print("Total wins = {}, win rate = {:.1%}".format(game.player.wins, game.player.wins / num_rounds))
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
