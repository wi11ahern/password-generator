import random
import string
from typing import List


class PasswordGenerator:
    _acceptable_characters: str = string.ascii_letters

    def __init__(
            self,
            password_length: int = 12,
            keywords: List[str] = None,
            include_special_chars: bool = True,
            include_numbers: bool = True
    ):
        self.password_length = password_length
        if password_length < 6:
            raise EnvironmentError(f'Password length must be at least 6 characters. {password_length} were given.')

        self.keywords = keywords
        self.include_special_chars = include_special_chars
        self.include_numbers = include_numbers

    def generate_password(self) -> str:
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
            special_characters = '!@#$%&'
            self._acceptable_characters += special_characters
            guaranteed_characters_list.append(random.choice(special_characters))

        # Generate the set of password characters.
        password_characters: List[str] = [
            random.choice(self._acceptable_characters)
            for i in range(self.password_length - len(guaranteed_characters_list))
        ]
        password_characters.extend(guaranteed_characters_list)
        random.shuffle(password_characters)

        if self.keywords:
            for keyword in self.keywords:
                password_characters.insert(random.choice(range(0, len(password_characters) - 1)), keyword)

        return ''.join(password_characters)
