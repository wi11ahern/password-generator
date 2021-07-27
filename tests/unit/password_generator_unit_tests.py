import string

from unittest import TestCase

from pasword_generator import PasswordGenerator


class PasswordGeneratorUnitTests(TestCase):
    _special_characters: str = '!@*-_.'

    def test_generate_password_default(self):
        """
        Tests if the generated password is:
        - A string
        - 8 characters long
        - First character is a letter or number
        - Includes at least 1 special character
        - Includes at least 1 digit
        """
        password_generator = PasswordGenerator()
        password = password_generator.generate_password()
        print(password)

        self.assertIsInstance(password, str)
        self.assertTrue(len(password) == 8)
        self.assertTrue((any(char in password[0] for char in string.digits + string.ascii_letters)))
        self.assertTrue((any(char in self._special_characters for char in password)))
        self.assertTrue((any(char in string.digits for char in password)))

    def test_generate_password_first_character_is_letter_or_number(self):
        """
        Tests if the generated password's first character is a letter or number.
        """
        password_generator = PasswordGenerator(
            include_special_chars=False
        )
        password = password_generator.generate_password()
        print(password)

        self.assertTrue((any(char in password[0] for char in string.digits + string.ascii_letters)))

    def test_generate_password_without_special_characters(self):
        """
        Tests if the generated password is does NOT include special characters.
        """
        password_generator = PasswordGenerator(
            include_special_chars=False
        )
        password = password_generator.generate_password()
        print(password)

        self.assertTrue((not any(char in self._special_characters for char in password)))

    def test_generate_password_without_numbers(self):
        """
        Tests if the generated password is does NOT numbers.
        """
        password_generator = PasswordGenerator(
            include_numbers=False
        )
        password = password_generator.generate_password()
        print(password)

        self.assertTrue((not any(char in string.digits for char in password)))


