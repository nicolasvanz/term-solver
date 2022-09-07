import sys

from termo_game import TermoGame


def main(words_amount):
    game = TermoGame(words_amount=words_amount)
    print(f"suggested initial guess: {game.suggested_guess()}")
    while(True):
        try:
            line = input().split()
            guess = line[0]
            info = line[1:]
        except ValueError:
            print("invalid usage. Type the word and infos separated by one space")
            continue

        game.guess(guess, info)


if __name__ == "__main__":
    try:
        words_amount = int(sys.argv[1])
    except IndexError or ValueError:
        print("invalid usage. Usage: 'main.py <n>' where n is the word amount")
        exit()

    main(words_amount)