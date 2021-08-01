import random
import string

from typing import List
import settings
from src.password_generator.i_password_generator import PasswordGeneratorInterface


class HumanReadablePasswordGenerator(PasswordGeneratorInterface):
    _special_characters: str = '!@*-_.'

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
        self._special_characters = self._special_characters.replace(delimiter_map[word_delimiter], '')

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
                curated_words.append(word.lower())

        # Randomly select words to form the password.
        password_words = [
            random.choice(curated_words)
            for i in range(self.number_of_words)
        ]

        # If True, randomly make all characters in a word lowercase or uppercase.
        if self.include_uppercase_words:
            self._include_uppercase(
                password_words=password_words
            )

        # If True, include special characters.
        # Guarantees at least one special character is used.
        if self.include_special_chars:
            self._include_special_characters(
                password_words=password_words
            )

        # If True, include numbers.
        # Guarantees at least one number is used.
        if self.include_numbers:
            self._include_numbers(
                password_words=password_words
            )

        return self.word_delimiter.join(password_words)

    def _include_uppercase(self, password_words: List[str]):
        """
        Randomly makes words uppercase.
        """
        for index, word in enumerate(password_words):
            password_words[index] = random.choice([word.upper(), word.lower()])

    def _include_special_characters(self, password_words: List[str]):
        """
        Randomly adds special characters to the end of words.
        Guarantees at least 1 special character is added.
        """
        has_special_char = False
        for index, word in enumerate(password_words):
            password_words[index] = random.choice([
                word + random.choice(self._special_characters),
                word
            ])

            if any(spec_char in password_words[index] for spec_char in self._special_characters):
                has_special_char = True

        if not has_special_char:
            index = random.choice(range(len(password_words)))
            word = password_words[index]
            password_words[index] = word + random.choice(self._special_characters)

    def _include_numbers(self, password_words: List[str]):
        """
        Randomly adds numbers to the end of words.
        Guarantees at least 1 number is added.
        """
        has_number = False
        for index, word in enumerate(password_words):
            password_words[index] = random.choice([
                word + random.choice(string.digits),
                word
            ])

            if any(number in password_words[index] for number in string.digits):
                has_number = True

        if not has_number:
            index = random.choice(range(len(password_words)))
            word = password_words[index]
            password_words[index] = word + random.choice(string.digits)

