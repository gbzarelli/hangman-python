from hangman_display import TerminalHangmanDisplay
from hangman_game import HangmanGame
from word_creator import LastNameWordGenerator
from char_inputter import TerminalCharInputter


def main():
    HangmanGame(
        LastNameWordGenerator(),
        TerminalCharInputter(),
        TerminalHangmanDisplay()
    ).play()


def init():
    if __name__ == "__main__":
        main()


init()
