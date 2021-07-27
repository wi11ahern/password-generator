import random
import string
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
        if password_length < 8:
            raise EnvironmentError(f'Password length must be at least 8 characters. {password_length} were given.')

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

