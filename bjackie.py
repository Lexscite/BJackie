from app.game import Game


def main():
    num_rounds = 1

    game = Game()
    for k in range(0, num_rounds):
        game.round()


if __name__ == "__main__":
    main()
