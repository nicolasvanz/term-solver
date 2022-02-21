from words import *


def error():
    print("error")

words = Words()
WORD_LENGTH = 5

while(True):
    guess, info = input().split()

    correct_idx = []
    present_idx = []
    wrong_idx   = []

    error = False
    for i in range(WORD_LENGTH):
        if info[i] == 'g':
            correct_idx.append((i, guess[i]))
        elif info[i] == 'y':
            present_idx.append((i, guess[i]))
        elif info[i] == 'r':
            wrong_idx.append(guess[i])
        else:
            error = True
            break
    
    wrong_idx = list(set(wrong_idx))
    for w in wrong_idx:
        for c in correct_idx:
            if c[1] == w:
                wrong_idx.remove(w)
        for p in present_idx:
            if p[1] == w:
                wrong_idx.remove(w)
                

    if not error:
        words.guess(correct_idx, present_idx, wrong_idx)
    else:
        error()
