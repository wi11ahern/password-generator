import string

from unittest import TestCase

from pasword_generator import PasswordGenerator


class PasswordGeneratorUnitTests(TestCase):

    def test_generate_password_default(self):
        """
        Tests if the generated password is:
        - A string
        - 12 characters long
        - Includes at least 1 special character
        - Includes at least 1 digit
        """
        password_generator = PasswordGenerator()
        password = password_generator.generate_password()

        self.assertIsInstance(password, str)
        self.assertTrue(len(password) == 8)
        self.assertTrue((any(char in string.punctuation + ' ' for char in password)))
        self.assertTrue((any(char in string.digits for char in password)))

    def test_generate_password_without_special_characters(self):
        """
        Tests if the generated password is does NOT include special characters.
        """
        password_generator = PasswordGenerator(
            include_special_chars=False
        )
        password = password_generator.generate_password()

        self.assertTrue((not any(char in string.punctuation + ' ' for char in password)))

    def test_generate_password_without_numbers(self):
        """
        Tests if the generated password is does NOT numbers.
        """
        password_generator = PasswordGenerator(
            include_numbers=False
        )
        password = password_generator.generate_password()

        self.assertTrue((not any(char in string.digits for char in password)))

    def test_generate_password_with_keywords(self):
        """
        Tests if the generated password includes keywords.
        """
        keywords = ['hello', 'world']
        password_generator = PasswordGenerator(
            keywords=keywords
        )
        password = password_generator.generate_password()

        self.assertTrue((any(keyword in password for keyword in keywords)))



