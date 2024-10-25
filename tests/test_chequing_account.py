"""
Description: Unit tests for the chequing_account class.
Author: {Prabhkiran Singh}
"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    
    def setUp(self):
        self.chequing_account = ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), -200.0, 0.05)

    def test_init_valid_input_attributes_set(self):
        # Assert
        self.assertEqual(self.chequing_account.account_number, 20019)
        self.assertEqual(self.chequing_account.client_number, 1010)
        self.assertEqual(self.chequing_account.balance, 1000.50)
        self.assertEqual(self.chequing_account.overdraft_limit, -200.0)
        self.assertEqual(self.chequing_account.overdraft_rate, 0.05)
        self.assertEqual(self.chequing_account._date_created, date(2024, 5, 10))

    def test_init_invalid_overdraft_limit(self):
        # Assert
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), "invalid_limit", 0.05)

    def test_init_invalid_overdraft_rate(self):
        # Assert
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), -200.0, "invalid_rate")

    def test_init_invalid_date_created(self):
        # Assert
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1000.50, "invalid_date", -200.0, 0.05)

    def test_service_charges_balance_greater_than_overdraft_limit(self):
        # Arrange
        self.chequing_account._balance = 0.0
        
        # Assert
        self.assertEqual(0.50, round(self.chequing_account.get_service_charges(), 2))

    def test_service_charges_balance_less_than_overdraft_limit(self):
        # Arrange
        self.chequing_account._balance = -300.0
        expected_service_charges = 0.50 + (100 * 0.05)
        
        # Assert
        self.assertEqual(expected_service_charges, round(self.chequing_account.get_service_charges(), 2))

    def test_service_charges_balance_equal_to_overdraft_limit(self):
        # Arrange
        self.chequing_account._balance = -200.0
        
        # Assert
        self.assertEqual(0.50, round(self.chequing_account.get_service_charges(), 2))

    def test_str_representation(self):
        # Arrange
        
        # Assert
        self.assertEqual(str(self.chequing_account), "Account Number: 20019 Balance: $1,000.50\n"
                        "Overdraft Limit: $-200.00 Overdraft Rate: 5.00% Account Type: Chequing")

if __name__ == "__main__":
    unittest.main()