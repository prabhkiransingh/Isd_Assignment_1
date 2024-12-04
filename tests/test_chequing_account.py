"""
Description: Unit tests for the chequing_account class.
Author: Prabhkiran Singh
"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    
    def setUp(self):
        # Initialize with example values
        self.chequing_account = ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), -200.0, 0.05)

    def test_init_valid_input_attributes_set(self):
        # Initialize account for testing attribute values
        account = ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), -200.0, 0.05)
        
        # Assert attribute values using correct name mangling
        self.assertEqual(account._BankAccount__account_number, 20019)
        self.assertEqual(account._BankAccount__client_number, 1010)
        self.assertEqual(account._BankAccount__balance, 1000.50)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -200.0)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)
        self.assertEqual(account._date_created, date(2024, 5, 10))

    def test_init_invalid_overdraft_limit(self):
        # Assert ValueError for invalid overdraft limit
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), "invalid_limit", 0.05)

    def test_init_invalid_overdraft_rate(self):
        # Assert ValueError for invalid overdraft rate
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), -200.0, "invalid_rate")

    def test_init_invalid_date_created(self):
        # Assert ValueError for invalid date created
        with self.assertRaises(ValueError):
            ChequingAccount(20019, 1010, 1000.50, "invalid_date", -200.0, 0.05)

    def test_service_charges_balance_greater_than_overdraft_limit(self):
        # Set balance to test standard service charge scenario
        self.chequing_account._BankAccount__balance = 0.0
        # Assert standard service charge
        self.assertEqual(0.50, round(self.chequing_account.get_service_charges(), 2))

    def test_service_charges_balance_less_than_overdraft_limit(self):
        # Set balance below overdraft limit
        self.chequing_account._BankAccount__balance = -250.0
        # Calculate overdraft amount without abs
        overdraft_amount = self.chequing_account._ChequingAccount__overdraft_limit - self.chequing_account._BankAccount__balance
        expected_service_charges = 0.50 + (overdraft_amount * self.chequing_account._ChequingAccount__overdraft_rate)
        
        # Assert calculated service charge matches expected value
        self.assertEqual(expected_service_charges, round(self.chequing_account.get_service_charges(), 2))

    def test_service_charges_balance_equal_to_overdraft_limit(self):
        # Set balance equal to overdraft limit
        self.chequing_account._BankAccount__balance = -200.0
        # Assert only the standard service charge applies
        self.assertEqual(0.50, round(self.chequing_account.get_service_charges(), 2))

    def test_str_representation(self):
        # Assert string representation of account object
        self.assertEqual(str(self.chequing_account), "Account Number: 20019 Balance: $1,000.50\n"
                                                     "Overdraft Limit: $-200.00 Overdraft Rate: 5.00% Account Type: Chequing")

if __name__ == "__main__":
    unittest.main()
