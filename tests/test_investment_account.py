"""
Description: Unit tests for the investment_account class.
Author: {Prabhkiran Singh}
"""

"""
Description: Unit tests for the InvestmentAccount class.
Author: {Prabhkiran Singh}
Date: {9/15/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""
import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount  

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        # Common setup for tests
        self.investment_account = InvestmentAccount(20019, 1010, 1000.50, date(2024, 10, 5), 1.50)

    def test_init_attributes_set_to_values(self):
        # Arrange
        account = InvestmentAccount(20019, 1010, 1000.50, date(2024, 10, 5), 1.50)
        
        # Assert
        self.assertEqual(account._account_number, 20019)
        self.assertEqual(account._client_number, 1010)
        self.assertEqual(account._balance, 1000.50)
        self.assertEqual(account._date_created, date(2024, 10, 5))
        self.assertEqual(account._management_fee, 1.50)

    def test_init_invalid_management_fee_type(self):
        # Assert
        with self.assertRaises(ValueError):
            InvestmentAccount(20019, 1010, 1000.50, date(2024, 10, 6), "invalid")


    def test_init_invalid_balance(self):
        # Assert
        with self.assertRaises(ValueError):
            InvestmentAccount(20019, 1010, "invalid", date(2024, 10, 5), 1.50)

    def test_get_service_charges_more_than_10_years(self):
        # Arrange
        account = InvestmentAccount(20019, 1010, 1000.50, date(2008, 10, 5), 2.00)
        
        # Assert
        self.assertEqual(0.50, round(account.get_service_charges(), 2))

    def test_get_service_charges_exactly_10_years(self):
        # Arrange
        ten_years_ago = date.today() - timedelta(days=10 * 365.25)
        account = InvestmentAccount(20019, 1010, 1000.50, ten_years_ago, 3.00)
        
        # Assert
        self.assertEqual(0.50, round(account.get_service_charges(), 2))

    def test_get_service_charges_within_last_10_years(self):
        # Arrange
        account = InvestmentAccount(20019, 1010, 1000.50, date(2024, 10, 5), 2.50)
        
        # Assert
        self.assertEqual(3.00, round(account.get_service_charges(), 2))

    def test_str_waived_fee_more_than_10_years(self):
        # Arrange
        account = InvestmentAccount(20019, 1010, 1000.50, date(2008, 7, 20), 1.50)
        
        # Assert
        self.assertEqual(str(account), "Account Number: 20019 Balance: $1,000.50\n"
                        "Date Created: 2008-07-20\n"
                        "Management Fee: Waived Account Type: Investment")

    def test_str_management_fee_within_last_10_years(self):
        # Arrange
        account = InvestmentAccount(20019, 1010, 1000.50, date(2015, 1, 1), 1.50)
        
        # Assert
        self.assertEqual(str(account), "Account Number: 20019 Balance: $1,000.50\n"
                        "Date Created: 2015-01-01\n"
                        "Management Fee: $1.50 Account Type: Investment")

if __name__ == '__main__':
    unittest.main()