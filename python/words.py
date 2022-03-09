import json
from urllib import response
class Words:
    def __init__(self):
        self.words = get_words()
        self.all_words = get_words()
        self.word_length = 5
    
    def guess(self, guess, info):
        correct_idx = []
        present_idx = []
        wrong_idx   = []

        error = False
        for i in range(self.word_length):
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
                if p[1] == w and w in wrong_idx:
                    wrong_idx.remove(w)
        
        if error:
            print("error. this guess was not processed")
            return

        if (guess in self.all_words):
            self.all_words.remove(guess)
        else:
            print("this word is not registered!")

        self.process_correct(correct_idx)
        self.process_present(present_idx)
        self.process_wrong(wrong_idx)
        print(f"suggested: {self.suggested_guess()}")

    def process_correct(self, correct):
        while(True):
            removed = False
            for idx, letter in correct:
                for word in self.words:
                    if word[idx] != letter:
                        self.words.remove(word)
                        removed = True
            if not removed:
                break
    
    def process_present(self, present):
        while(True):
            removed = False
            for idx, letter in present:
                for word in self.words:
                    if letter in word and word[idx] != letter:
                        continue
                    else:
                        removed = True
                        self.words.remove(word)
            if not removed:
                break

    def process_wrong(self, wrong):
        while (True):
            removed = False
            for letter in wrong:
                for word in self.words:
                    if letter in word:
                        self.words.remove(word)
                        removed = True
            if not removed:
                break
    
    def suggested_guess(self):
        if len(self.words) == 1:
            return self.words[0]
    
        counter = {chr(i) : 0 for i in range(97, 123)}
        counter['ç'] = 0

        total = len(self.words)

        if (total == 0):
            print("no words left! the word might not be registered!")
            exit()

        # counting ocurrencies
        for word in self.words:
            for letter in set(word):
                counter[letter] += 1

        # measuring how good the letter is in a guess.
        # we are looking for letters that appear in half of the possible words
        for key, value in counter.items():
            counter[key] = abs((value/total) - 0.5) + 0.5

        # measuring how good is a word in a guess. We already know which letters
        # are good. We use this here
        values = []
        for word in self.all_words:
            value = 1
            word_set = set(word)
            for letter in word_set:
                value *= counter[letter]
            values.append((word, value))
        
        values = sorted(values, key=lambda x: x[1])
        return values[0][0]


def get_words():
    fileObject = open("termo.json", "r")
    jsonContent = fileObject.read()
    wordList = json.loads(jsonContent)['words']
    return wordList