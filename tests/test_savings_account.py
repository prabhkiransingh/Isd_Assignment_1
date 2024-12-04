"""
Description: Unit tests for the savings_account class.
Author: {Prabhkiran Singh}
Date:
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount  

class TestSavingsAccount(unittest.TestCase):
    
    def setUp(self):
        self.setUp_savings = SavingsAccount(20019, 1010, 1000.50, date.today(), 100.00)

    def test_init_attributes(self):
        # Arrange
        account = SavingsAccount(20019, 1010, 1000.50, date.today(), 100.00)
        
        # Assert
        self.assertEqual(account._BankAccount__account_number, 20019)
        self.assertEqual(account._BankAccount__client_number, 1010)
        self.assertEqual(account._BankAccount__balance, 1000.50)
        self.assertEqual(account._SavingsAccount__minimum_balance, 100.00)

    def test_init_invalid_minimum_balance(self):
        # Assert
        with self.assertRaises(ValueError):
            SavingsAccount(20019, 1010, 1000.50, date.today(), "invalid")

    def test_get_service_charges_balance_greater_than_minimum(self):
        # Arrange
        account = SavingsAccount(20019, 1010, 200.00, date.today(), 100.00)
        
        # Assert
        self.assertEqual(0.50, round(account.get_service_charges(), 2))

    def test_get_service_charges_balance_equal_to_minimum(self):
        # Arrange
        account = SavingsAccount(20019, 1010, 100.00, date.today(), 100.00)
        
        # Assert
        self.assertEqual(0.50, round(account.get_service_charges(), 2))

    def test_get_service_charges_balance_less_than_minimum(self):
        # Arrange
        account = SavingsAccount(20019, 1010, 49.99, date.today(), 50.00)
        
        # Assert
        self.assertEqual(1.00, round(account.get_service_charges(), 2))

    def test_str_method(self):
        # Arrange
        account = SavingsAccount(20019, 1010, 1000.50, date.today(), 100.00)
        
        # Assert
        self.assertEqual(str(account), "Account Number: 20019 Balance: $1,000.50\n"
                                       "Minimum Balance: $100.00 Account Type: Savings")

if __name__ == "__main__":
    unittest.main()