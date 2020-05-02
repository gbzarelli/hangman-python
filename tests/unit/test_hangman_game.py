import unittest
from typing import Optional
from unittest.mock import Mock

from char_inputter import CharInputter
from hangman_display import HangmanDisplay
from hangman_game import HangmanGame


class CounterCharsInputter(CharInputter):

    def __init__(self, chars):
        self.__time = 0
        self.__chars = chars

    def get_single_char(self) -> Optional[str]:
        ret = self.__chars[self.__time]
        self.__time += 1
        return ret


class FailedCharInputterTest(CounterCharsInputter):

    def __init__(self):
        super().__init__(("a", "b", "c", "d", "e", "f", "g", "h", "i"))


class SuccessCharInputterTest(CounterCharsInputter):

    def __init__(self):
        super().__init__(("h", "e", "l", "p", "d", "v"))


class SuccessWithInvalidInputInCharInputterTest(CounterCharsInputter):

    def __init__(self):
        super().__init__(("h", None, "e", "l", "p", "d", "v"))


class SuccessWithAlreadyInputInCharInputterTest(CounterCharsInputter):

    def __init__(self):
        super().__init__(("h", "h", "e", "l", "p", "d", "v"))


class SuccessHangmanDisplayTest(HangmanDisplay):

    def welcome(self, secret_word_length):
        assert secret_word_length == 7

    def result(self, win: bool, word: str):
        assert win is True
        assert word.__eq__("Helpdev")

    def status(self, input_words: list, hits: int, life: int):
        assert life == 6


class TestHangmanGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create default mocks
        cls.word_generate = Mock()
        cls.char_inputter = Mock()
        cls.hangman_display = Mock()

        # configure mocks
        cls.word_generate.generate.return_value = "helpdev"

        # create default game
        cls.game = HangmanGame(cls.word_generate, cls.char_inputter, cls.hangman_display)

    def test_should_create_a_game_with_cleaning_inputted_words(self):
        assert len(self.game.inputted_words) == 7
        for key in self.game.inputted_words:
            assert key == "_"
        assert self.game.status() is HangmanGame.STATUS_WAITING

    def test_should_win_the_game(self):
        char_inputter = SuccessCharInputterTest()
        hangman_display = SuccessHangmanDisplayTest()
        game = HangmanGame(self.word_generate, char_inputter, hangman_display)
        game.play()
        assert game.status() is HangmanGame.STATUS_WIN

    def test_should_win_the_game_with_already_inputted(self):
        char_inputter = SuccessWithAlreadyInputInCharInputterTest()
        hangman_display = SuccessHangmanDisplayTest()
        game = HangmanGame(self.word_generate, char_inputter, hangman_display)
        game.play()
        assert game.status() is HangmanGame.STATUS_WIN

    def test_should_win_the_game_with_invalid_inputted(self):
        char_inputter = SuccessWithInvalidInputInCharInputterTest()
        hangman_display = SuccessHangmanDisplayTest()
        game = HangmanGame(self.word_generate, char_inputter, hangman_display)
        game.play()
        assert game.status() is HangmanGame.STATUS_WIN

    def test_should_lost_the_game(self):
        char_inputter = FailedCharInputterTest()
        game = HangmanGame(self.word_generate, char_inputter, self.hangman_display)
        game.play()
        assert game.status() is HangmanGame.STATUS_LOST
