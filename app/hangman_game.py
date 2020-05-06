from word_creator import WordGenerator
from char_inputter import CharInputter
from hangman_display import HangmanDisplay


class HangmanGame(object):
    __slots__ = ['__secret_word', '__char_inputter', '__hangman_display', '__inputted_words', '__typed_chars',
                 '__typed_chars', '__status']

    MAX_LIFE = 6
    STATUS_WAITING = 1
    STATUS_PLAYING = 2
    STATUS_LOST = 3
    STATUS_WIN = 4

    def __init__(self, word_generator: WordGenerator, char_inputter: CharInputter, hangman_display: HangmanDisplay):
        self.__secret_word = word_generator.generate()
        self.__char_inputter = char_inputter
        self.__hangman_display = hangman_display
        self.__inputted_words = ["_" for _ in range(len(self.__secret_word))]
        self.__typed_chars = set()
        self.__status = HangmanGame.STATUS_WAITING

    def play(self):
        self.__hangman_display.welcome(len(self.__secret_word))
        self.__status = HangmanGame.STATUS_PLAYING
        win = self.__game_loop()
        self.__hangman_display.result(win, self.__secret_word.capitalize())

    def __game_loop(self):
        win = False
        current_life = self.MAX_LIFE
        self.__print_status(current_life)

        while current_life > 0 and not win:
            char = self.__char_inputter.get_single_char()
            if char is None:
                print("Invalid input, try again!")
                continue

            if self.__check_input_was_typed(char):
                print(f"You already input this character ({char})")
                continue

            if self.__process_char(char):
                win = self.__check_win()
            else:
                current_life -= 1

            self.__print_status(current_life)

        if win:
            self.__status = HangmanGame.STATUS_WIN
        else:
            self.__status = HangmanGame.STATUS_LOST

        return win

    def status(self) -> int:
        return self.__status

    def __print_status(self, current_life):
        self.__hangman_display.status(self.__inputted_words, self.MAX_LIFE - current_life, current_life)

    def __check_win(self) -> bool:
        if "_" in self.__inputted_words:
            return False
        return self.__secret_word == "".join(self.__inputted_words)

    def __check_input_was_typed(self, char) -> bool:
        return char in self.__typed_chars

    @property
    def inputted_words(self) -> list:
        return self.__inputted_words

    def __process_char(self, char) -> bool:
        self.__typed_chars.add(char)
        if char not in self.__secret_word:
            return False

        for index, secret_char in enumerate(self.__secret_word):
            if secret_char == char:
                self.__inputted_words[index] = secret_char

        return True
