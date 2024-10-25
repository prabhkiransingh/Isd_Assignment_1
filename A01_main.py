"""
Description: A client program written to verify correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """
    Test the functionality of the methods encapsulated 
    in the BankAccount and Transaction classes.
    """

    # Create a valid instance of the Client class
    client = Client("Prabhkiran", "Singh", "PrabhkiranSingh@gmail.com")

    # Declare a BankAccount object with an initial value of None
    bank_account = None

    # Instantiate the BankAccount object
    try:
        bank_account = BankAccount(20019, client.client_number, 1000.50)
    except Exception as e:
        print(f"Error creating BankAccount: {e}")

    # Attempt to create a BankAccount with an invalid balance
    try:
        invalid_bank_account = BankAccount(20020, client.client_number, "invalid")
    except Exception as e:
        print(f"Error creating BankAccount with invalid balance: {e}")

    # Print the Client and BankAccount instances
    print(client)
    print(bank_account)

    # Attempt to deposit a non-numeric value
    try:
        bank_account.deposit("invalid")
    except Exception as e:
        print(f"Error depositing non-numeric value: {e}")

    # Attempt to deposit a negative value
    try:
        bank_account.deposit(-100)
    except Exception as e:
        print(f"Error depositing negative value: {e}")

    # Attempt to withdraw a valid amount
    try:
        bank_account.withdraw(500)
    except Exception as e:
        print(f"Error withdrawing valid amount: {e}")

    # Attempt to withdraw a non-numeric value
    try:
        bank_account.withdraw("invalid")
    except Exception as e:
        print(f"Error withdrawing non-numeric value: {e}")

    # Attempt to withdraw a negative value
    try:
        bank_account.withdraw(-100)
    except Exception as e:
        print(f"Error withdrawing negative value: {e}")

    # Attempt to withdraw an amount exceeding the balance
    try:
        bank_account.withdraw(1500)
    except Exception as e:
        print(f"Error withdrawing amount exceeding balance: {e}")

    # Print the BankAccount instance after transactions
    print(bank_account)

