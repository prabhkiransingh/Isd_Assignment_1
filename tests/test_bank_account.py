"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: {Prabhkiran Singh}
Date: {9/15/2024}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
class BankAccount:
    def __init__(self, account_number, client_number, balance):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        try:
            self.balance = float(balance)
        except ValueError:
            self.balance = 0.0

        self.account_number = account_number
        self.client_number = client_number

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        
        self.balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
        if amount > self.balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.balance:,.2f}")
        
        self.balance -= amount
    
    def update_balance(self, new_balance):
        if not isinstance(new_balance, (int, float)):
            raise ValueError(f"New balance: {new_balance} must be numeric.")
        
        self.balance = float(new_balance)

    def __str__(self):
        return f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"


import unittest

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        
        self.setUp_bank = BankAccount(20019, 1010, 1000.50)

    def test_valid_bank_account_creation(self):
        #Arrange
        account = BankAccount(20019, 1010, 1000.50)
         # Asserts
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 1010)
        self.assertEqual(round(account.balance, 2), 1000.50)

    def test_invalid_account_number(self):
        #Arrange

        #Assert
        with self.assertRaises(ValueError):
            BankAccount("20019", 1010, 1000.50)

    def test_invalid_client_number(self):
        #Arrange

        #Assert
        with self.assertRaises(ValueError):
            BankAccount(20019, "1010", 1000.50)

    def test_invalid_balance(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, "invalid")
        self.assertEqual(account.balance, 0.0)

    def test_account_number(self):
        #Arrange

        #Assert
        self.assertEqual(20019, self.setUp_bank.account_number)

    def test_client_number(self):
        #Arrange

        #Assert
        self.assertEqual(1010, self.setUp_bank.client_number)

    def test_update_balance_positive(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        account.update_balance(2000.00)
        self.assertEqual(round(account.balance, 2), 2000.00)

    def test_update_balance_negative(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        account.update_balance(-500.00)
        self.assertEqual(round(account.balance, 2), -500.00)

    def test_update_balance_non_numeric(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        with self.assertRaises(ValueError):
            account.update_balance("invalid")

    def test_valid_deposit(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        account.deposit(500)
        self.assertEqual(round(account.balance, 2), 1500.50)

    def test_invalid_deposit_negative(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        with self.assertRaises(ValueError):
            account.deposit(-100)

    def test_valid_withdrawal(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        account.withdraw(500)
        self.assertEqual(round(account.balance, 2), 500.50)

    def test_invalid_withdrawal_non_numeric(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        with self.assertRaises(ValueError):
            account.withdraw("invalid")

    def test_invalid_withdrawal_negative(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        with self.assertRaises(ValueError):
            account.withdraw(-100)

    def test_withdrawal_exceeding_balance(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        with self.assertRaises(ValueError):
            account.withdraw(1500)

    def test_bank_account_str(self):
        #Arrange

        #Assert
        account = BankAccount(20019, 1010, 1000.50)
        self.assertEqual(str(account), "Account Number: 20019 Balance: $1,000.50\n")