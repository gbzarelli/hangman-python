from unittest.mock import patch

from char_inputter import TerminalCharInputter


class TestTerminalCharInputter:

    @patch('builtins.input', lambda _: 'y')
    def test_should_accept_a_single_char(self):
        value = TerminalCharInputter().get_single_char()
        assert value == 'y'

    @patch('builtins.input', lambda _: 'yz')
    def test_should_return_null_object_when_the_input_has_more_than_one_character(self):
        value = TerminalCharInputter().get_single_char()
        assert value is None
