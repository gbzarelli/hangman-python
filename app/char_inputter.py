from abc import abstractmethod
from abc import ABC
from typing import Optional


class CharInputter(ABC):

    @abstractmethod
    def get_single_char(self) -> Optional[str]:
        pass


class TerminalCharInputter(CharInputter):
    def get_single_char(self) -> Optional[str]:
        new_char = input("Enter with a new char\n").lower()
        if len(new_char) != 1:
            return None
        return new_char
