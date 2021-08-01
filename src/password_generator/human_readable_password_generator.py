import random

from typing import List
import settings
from src.password_generator.i_password_generator import PasswordGeneratorInterface


class HumanReadablePasswordGenerator(PasswordGeneratorInterface):
    def __init__(
            self,
            number_of_words: int = 4,
            word_delimiter: str = 'Dash',
            include_uppercase_words: bool = False,
            include_special_chars: bool = False,
            include_numbers: bool = False
    ):
        delimiter_map = {
            'Dash': '-',
            'Underscore': '_',
            'Space': ' ',
            'Comma': ',',
            'Period': '.'
        }
        self.number_of_words = number_of_words
        self.word_delimiter = delimiter_map[word_delimiter]
        self.include_uppercase_words = include_uppercase_words
        self.include_special_chars = include_special_chars
        self.include_numbers = include_numbers

    def generate_password(self) -> str:
        """
        Generates a random, human-readable password.
        :return: password string.
        """
        # Read in words from file.
        with open(settings.ROOT_DIR + '/src/resources/proper_names_list.txt') as file:
            words: str = file.read()

        words: List[str] = words.splitlines()
        curated_words: List[str] = []

        # Curate sub-selection of words.
        for word in words:
            word_length = len(word)
            if 4 <= word_length <= 6:
                curated_words.append(word)

        for index, word in enumerate(curated_words):
            # If True, randomly make all characters in a word lowercase or uppercase.
            if self.include_uppercase_words:
                curated_words[index] = random.choice([word.upper(), word.lower()])
            else:
                curated_words[index] = word.lower()

        # Randomly select words to form the password.
        password_words: List[str] = [
            random.choice(curated_words)
            for i in range(self.number_of_words)
        ]

        return self.word_delimiter.join(password_words)

