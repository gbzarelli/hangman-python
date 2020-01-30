from abc import ABC, abstractmethod


class HangmanDisplay(ABC):

    @abstractmethod
    def status(self, input_words: list, hits: int, life: int):
        pass

    def welcome(self, secret_word_length):
        pass

    def result(self, win: bool, word: str):
        pass


class TerminalHangmanDisplay(HangmanDisplay):
    # This display show until 6 hits
    def status(self, input_words: list, hits: int, life: int):

        print(input_words)

        if 0 == hits:
            print(
                """
            _______
            |     |
            |   
            |   
            |   
            |
            """
            )
        elif 1 == hits:
            print(
                """
            _______
            |     |
            |     O
            |   
            |   
            |
            """
            )
        elif 2 == hits:
            print(
                """
            _______
            |     |
            |     O
            |    /
            |   
            |
            """
            )
        elif 3 == hits:
            print(
                """
            _______
            |     |
            |     O
            |    /|
            |   
            |
            """
            )
        elif 4 == hits:
            print(
                """
            _______
            |     |
            |     O
            |    /|\\
            |   
            |
            """
            )
        elif 5 == hits:
            print(
                """
            _______
            |     |
            |     O
            |    /|\\
            |    / 
            |
            """
            )
        else:
            print(
                """
            _______
            |     |
            |     O
            |    /|\\
            |    / \\
            |  ((dead))
            """
            )
        print(f"You have {life} life", "\n")

    def welcome(self, secret_word_length):
        print("*********************************")
        print("***Welcome to the Hangman Game***")
        print("******Discover the last name*****")
        print("*********************************")
        print(f"\nThe secret word contains {secret_word_length} chars\n")

    def result(self, win: bool, word: str):
        if win:
            print(f"You WIN the game: {word}")
        else:
            print(f"You LOST, the word is: {word}")
