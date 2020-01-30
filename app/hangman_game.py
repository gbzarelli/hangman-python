from word_creator import WordGenerator
from char_inputter import CharInputter
from hangman_display import HangmanDisplay


class HangmanGame(object):
    MAX_LIFE = 6

    def __init__(self, word_generator: WordGenerator, char_inputter: CharInputter, hangman_display: HangmanDisplay):
        self.secret_word = word_generator.generate()
        self.char_inputter = char_inputter
        self.hangman_display = hangman_display
        self.input_words = ["_" for _ in range(len(self.secret_word))]
        self.typed_chars = set()

    def play(self):
        self.hangman_display.welcome(len(self.secret_word))
        win = self.game_loop()
        self.hangman_display.result(win, self.secret_word.capitalize())

    def game_loop(self):
        win = False
        current_life = self.MAX_LIFE
        self.print_status(current_life)

        while current_life > 0 and not win:
            char = self.char_inputter.get_single_char()
            if char is None:
                print("Invalid input, try again!")
                continue

            if self.check_input_was_typed(char):
                print(f"You already input this character ({char})")
                continue

            if self.process_char(char):
                win = self.check_win()
            else:
                current_life -= 1

            self.print_status(current_life)

        return win

    def print_status(self, current_life):
        self.hangman_display.status(self.input_words, self.MAX_LIFE - current_life, current_life)

    def check_win(self) -> bool:
        if "_" in self.input_words:
            return False
        return self.secret_word == "".join(self.input_words)

    def check_input_was_typed(self, char) -> bool:
        return char in self.typed_chars

    def process_char(self, char) -> bool:
        self.typed_chars.add(char)
        if char not in self.secret_word:
            return False

        for index, secret_char in enumerate(self.secret_word):
            if secret_char == char:
                self.input_words[index] = secret_char

        return True
