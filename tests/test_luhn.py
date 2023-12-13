# pylint: disable=C0114,C0115,C0116


import unittest
from luhn import is_valid


class TestLuhn(unittest.TestCase):

    def test_luhn_valid_credit_card_number(self):
        credit_card_numbers = [
            "1000 2000 3000 4000",
            "9721 4872 0864 5208",
            "4539 3195 0343 6467",
        ]

        for credit_card_number in credit_card_numbers:
            is_credit_card_number_valid = is_valid(credit_card_number)

            self.assertTrue(is_credit_card_number_valid, f"Invalid credit card number {credit_card_number}")

    def test_luhn_invalid_credit_card_number(self):
        credit_card_numbers = [
            "1234 5678 9012 3456",
            "8273 1232 7352 0569",
            "1827 3645 5463 7281",
        ]

        for credit_card_number in credit_card_numbers:
            is_credit_card_number_valid = is_valid(credit_card_number)

            self.assertFalse(is_credit_card_number_valid, f"Valid credit card number {credit_card_number}")

    def test_luhn_malformed_credit_card_number(self):
        credit_card_number = "9273 1355 2234 016"


        #test si le message d'erreur fonction
        with self.assertRaises(Exception) as context:
            is_valid(credit_card_number)

        self.assertIn("Invalid credit card length", str(context.exception))

    def test_luhn_non_digit_input(self):
        credit_card_number = "Here is my credit card number!"

        #test si le message d'erreur fonction
        with self.assertRaises(Exception) as context:
            is_valid(credit_card_number)

        self.assertIn("Invalid characters in the credit card number", str(context.exception))
        
if __name__ == '__main__':
    unittest.main()
