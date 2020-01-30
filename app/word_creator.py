from abc import abstractmethod
from abc import ABC

from faker import Faker


class WordGenerator(ABC):

    @abstractmethod
    def generate(self) -> str:
        pass


class LastNameWordGenerator(WordGenerator):
    def generate(self) -> str:
        return Faker().last_name().lower()
