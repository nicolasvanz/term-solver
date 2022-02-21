from words import *


words = Words()

while(True):
    guess, info = input().split()

    words.guess(guess, info)
