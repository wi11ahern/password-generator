import random
import string

import settings

from typing import List


class PasswordGenerator:
    _acceptable_characters: str = string.ascii_letters
    _special_characters: str = '!@*-_.'

    def __init__(
            self,
            password_length: int = 8,
            include_special_chars: bool = True,
            include_numbers: bool = True
    ):
        self.password_length = password_length
        self.include_special_chars = include_special_chars
        self.include_numbers = include_numbers

    def generate_shuffled_password(self) -> str:
        """
        Generates a randomized password.
        :return: password string.
        """
        guaranteed_characters_list: List[str] = []

        # If True, include numbers 0-9 in acceptable characters.
        # Guarantees that at least one digit is included the password.
        if self.include_numbers:
            self._acceptable_characters += string.digits
            guaranteed_characters_list.append(random.choice(string.digits))

        # If True, include special characters !@#$%& in the acceptable characters
        # Guarantees that at least 1 special character is included in the password.
        if self.include_special_chars:
            self._acceptable_characters += self._special_characters
            guaranteed_characters_list.append(random.choice(self._special_characters))

        # Guarantee that the first character of the password is always a letter or number.
        password_characters: List[str] = [
            random.choice(self._acceptable_characters.strip(self._special_characters))
        ]

        # Generate the remaining number of characters.
        password_characters.extend([
            random.choice(self._acceptable_characters)
            for i in range(self.password_length - len(guaranteed_characters_list) - 1)
        ])

        # Add in guaranteed characters if any.
        password_characters.extend(guaranteed_characters_list)

        # Shuffle all characters minus the first.
        random.shuffle(password_characters[1:])

        return ''.join(password_characters)

    def generate_human_readable_password(self) -> str:
        """
        Generates a random, human-readable password.
        :return: password string.
        """
        # Read in words from file.
        with open(settings.ROOT_DIR + '/resources/proper_names_list.txt') as file:
            words: str = file.read()

        words: List[str] = words.splitlines()
        curated_words: List[str] = []

        # Curate sub-selection of words.
        for word in words:
            word_length = len(word)
            if 4 <= word_length <= 6:
                curated_words.append(random.choice([word.upper(), word.lower()]))

        # Randomly select words to form the password.
        password_words: List[str] = [
            random.choice(curated_words)
            for i in range(self.password_length)
        ]

        return '-'.join(password_words)

