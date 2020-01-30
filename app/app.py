from hangman_display import TerminalHangmanDisplay
from hangman_game import HangmanGame
from word_creator import LastNameWordGenerator
from char_inputter import TerminalCharInputter

if __name__ == "__main__":
    HangmanGame(
        LastNameWordGenerator(),
        TerminalCharInputter(),
        TerminalHangmanDisplay()
    ).play()
