import sys
import io
from unittest import TestCase

from hangman_display import TerminalHangmanDisplay


class TestTerminalHangmanDisplay(TestCase):

    @classmethod
    def setUpClass(cls):
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output
        cls.display = TerminalHangmanDisplay()
        cls.__output = captured_output

    def test_status(self):
        for value in range(7):
            self.display.status(['a', 'b', 'c'], value, 6)
        self.__output.getvalue().__contains__("((dead))")

    def test_welcome(self):
        self.display.welcome(6)
        self.__output.getvalue().__contains__("The secret word contains 6 chars")

    def test_result_win(self):
        self.display.result(True, "Test")
        self.__output.getvalue().__contains__("You WIN the game: Test")

    def test_result_lost(self):
        self.display.result(False, "Test")
        self.__output.getvalue().__contains__("You LOST, the word is: Test")
