from words import *

class TermoGame:
    def __init__(self, words_amount = 1, word_length = 5):
        self.words_amount = words_amount
        self.word_length = word_length
        self.ds = [get_words() for _ in range(words_amount)]
        self.all_words = get_words()
        self.done = [False] * self.words_amount

    def info_is_valid(self, info):
        if len(info) != self.words_amount:
            print("Info does not match with the number of words. Try again")
            return False

        for i in range(len(info)):
            if len(info[i]) != self.word_length:
                print("Info length does not match with word length. Try again")
                return False
            elif not set(info[i]).issubset({'g', 'r', 'y'}):
                print("bad info content. Letter info must be 'g', 'y' or 'r'")
                return False

        return True

    def guess(self, guess, info):
        if not self.info_is_valid(info):
            return

        correct_idx = [[] for _ in range(self.words_amount)]
        present_idx = [[] for _ in range(self.words_amount)]
        wrong_idx   = [[] for _ in range(self.words_amount)]

        for i in range(self.words_amount):
            if info[i] == "g" * self.word_length:
                self.done[i] = True
                self.ds[i].clear()
                continue
            for j in range(self.word_length):
                if info[i][j] == 'g':
                    correct_idx[i].append((j, guess[j]))
                elif info[i][j] == 'y':
                    present_idx[i].append((j, guess[j]))
                elif info[i][j] == 'r':
                    wrong_idx[i].append(guess[j])
                else:
                    print("unexpected error")
                    exit()

        if all(self.done):
            print("Success!")
            exit()

        wrong_idx = list(map(lambda x: list(set(x)), wrong_idx))

        for i in range(self.words_amount):
            for w in wrong_idx[i]:
                for c in correct_idx[i]:
                    if c[1] == w:
                        wrong_idx[i].remove(w)
                for p in present_idx[i]:
                    if p[1] == w and w in wrong_idx[i]:
                        wrong_idx[i].remove(w)

        if (guess in self.all_words):
            self.all_words.remove(guess)
        else:
            print("this word is not registered!")

        self.process_correct(correct_idx)
        self.process_present(present_idx)
        self.process_wrong(wrong_idx)

        print(f"suggested: {self.suggested_guess()}")

    def process_correct(self, correct):
        for i in range(self.words_amount):
            correct_aux = correct[i]
            ds_aux = self.ds[i]
            while(True):
                removed = False
                for idx, letter in correct_aux:
                    for word in ds_aux:
                        if word[idx] != letter:
                            ds_aux.remove(word)
                            removed = True
                if not removed:
                    break

    def process_present(self, present):
        for i in range(self.words_amount):
            present_aux = present[i]
            ds_aux = self.ds[i]
            while(True):
                removed = False
                for idx, letter in present_aux:
                    for word in ds_aux:
                        if letter in word and word[idx] != letter:
                            continue
                        else:
                            removed = True
                            ds_aux.remove(word)
                if not removed:
                    break

    def process_wrong(self, wrong):
        for i in range(self.words_amount):
            wrong_aux = wrong[i]
            ds_aux = self.ds[i]
            while (True):
                removed = False
                for letter in wrong_aux:
                    for word in ds_aux:
                        if letter in word:
                            ds_aux.remove(word)
                            removed = True
                if not removed:
                    break

    def suggested_guess(self):
        for i in range(self.words_amount):
            if self.done[i]:
                continue
            lds = len(self.ds[i])
            if lds == 0:
                print("no words left! The word might not be registered!")
                exit()
            elif lds == 1:
                # there is only one word left
                return self.ds[i][0]

        # counter for each DS
        counter = [
            {chr(i) : 0 for i in range(97, 123)}
            for _ in range(self.words_amount)
        ]
        for i in range(self.words_amount):
            counter[i]['ç'] = 0

        for i in range(self.words_amount):
            if self.done[i]:
                continue

            current_ds = self.ds[i]
            current_counter = counter[i]
            total = len(current_ds)

            # counting ocurrencies
            for word in current_ds:
                for letter in set(word):
                    current_counter[letter] += 1

            # measuring how good the letter is in a guess for the current DS.
            # we are looking for letters that appear in half of the
            # possible words of the current DS (in a perfect case)
            for key, value in current_counter.items():
                current_counter[key] = abs((value/total) - 0.5) + 0.5

        # measuring how good is a word in a guess. We are looking for words
        # whose letters appear in half of the possible words
        # of each DS (in a perfect case)

        values = []
        for word in self.all_words:
            value = 1
            word_set = set(word)
            for letter in word_set:
                for i in range(self.words_amount):
                    if self.done[i]:
                        continue
                    value *= counter[i][letter]
            values.append((word, value))

        values = sorted(values, key=lambda x: x[1])
        return values[0][0]
