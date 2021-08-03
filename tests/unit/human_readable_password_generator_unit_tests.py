import string

from unittest import TestCase

from src.password_generator.human_readable_password_generator import HumanReadablePasswordGenerator


class HumanReadablePasswordGeneratorTests(TestCase):

    def test_generate_human_readable_password(self):
        """
        Tests if the generated password is:
        - A string
        - 4 words long
        - Split by '-'
        """
        password_generator = HumanReadablePasswordGenerator()
        password = password_generator.generate_password()
        print(password)

        self.assertIsInstance(password, str)
        self.assertTrue(len(password.split('-')) == 4)
        self.assertTrue(len(password.split('-')) == 4)

    def test_generate_password_with_special_characters(self):
        """
        Tests if the generated password does NOT include special characters.
        """
        password_generator = HumanReadablePasswordGenerator(
            include_special_chars=True
        )
        password = password_generator.generate_password()
        print(password)

        self.assertTrue((any(char in password_generator._special_characters for char in password)))

    def test_generate_password_with_numbers(self):
        """
        Tests if the generated password does NOT include numbers.
        """
        password_generator = HumanReadablePasswordGenerator(
            include_numbers=True
        )
        password = password_generator.generate_password()
        print(password)

        self.assertTrue((any(char in string.digits for char in password)))

