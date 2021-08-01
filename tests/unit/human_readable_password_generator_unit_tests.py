
from unittest import TestCase

from src.password_generator.human_readable_password_generator import HumanReadablePasswordGenerator


class PasswordGeneratorUnitTests(TestCase):

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

