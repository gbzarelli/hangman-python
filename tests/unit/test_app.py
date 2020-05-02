import string
from unittest.mock import patch

import mock
from faker.generator import random

from app import application


def test_init_without_main():
    application.init()


# Test main with random game
@patch('builtins.input', lambda _: random.choice(string.ascii_letters))
def test_init_main():
    with mock.patch.object(application, "__name__", "__main__"):
        application.init()
