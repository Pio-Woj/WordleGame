from random import choice
from rich import print


class Wordle:
    def __init__(self, path_to_dictonary):
        with open(path_to_dictonary, "r", encoding="UTF-8") as file:
            self.words = file.read().splitlines()
        self.word = choice(self.words)
        self.num_guesses = 0
        self.guesses = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
            5: [" "]*5,
        }

    def draw_board(self):
        for guess in self.guesses.values():
            print(" ||| ".join(guess))
            print("="*25)
    
    def get_user_input(self):
        
        user_quess = input("Podaj 5-literowe słowo: ")
        while True:
            if len(user_quess) != 5:
                user_quess = input("Podane słowo nie jest 5-literowe")
                continue
            elif user_quess not in self.words:
                user_quess = input("Podane słowo nie instnieje w słowniku: ")
                continue
            break
        word_to_be_checkced = self.word
        user_quess = user_quess.lower()

        for id, char in enumerate(user_quess):
            if char == word_to_be_checkced[id]:
                word_to_be_checkced = word_to_be_checkced.replace(char,"-",1)
                char = f"[green]{char}[/]"
            self.guesses[self.num_guesses][id] = char

        for id, char in enumerate(user_quess):
            if char in word_to_be_checkced and self.guesses[self.num_guesses][id] != f"[green]{char}[/]":
                word_to_be_checkced = word_to_be_checkced.replace(char,"-",1)
                char = f"[yellow]{char}[/]"
                self.guesses[self.num_guesses][id] = char
        
        self.num_guesses += 1
        
        return user_quess

    def play(self):
        while True:
            self.draw_board()
            user_quess = self.get_user_input()

            if user_quess == self.word:
                self.draw_board()
                print(f"Wygrałeś! Prawidłowem słowem jest {self.word}")
                break
            if self.num_guesses > 5:
                self.draw_board()
                print(f"Przegrałeś! Prawidłowem słowem jest {self.word}")
                break
