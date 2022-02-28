from words import *



def main():
    global words

    while(True):
        try:
            guess, info = input().split()
        except ValueError:
            print("invalid usage. Type the word and info separated by one space")
            continue
        
        words.guess(guess, info)

if __name__ == "__main__":
    words = Words()
    main()