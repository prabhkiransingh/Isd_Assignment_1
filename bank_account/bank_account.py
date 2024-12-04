from datetime import date
from abc import ABC, abstractmethod

class BankAccount(ABC):
    """
    A class representing a bank account.

    Attributes:
        _account_number (int): The account number.
        _client_number (int): The client number.
        _balance (float): The current balance of the account.
        date_created (date): The date the account was created.

    Methods:
        update_balance(amount): Updates the balance by adding the given amount.
        deposit(amount): Deposits the given amount into the account.
        withdraw(amount): Withdraws the given amount from the account.
    """

    LOW_BALANCE_LEVEL = 50.00
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    

    def __init__(self, account_number:int, client_number:int, balance:float, date_created: date):  
        """
        Initializes a BankAccount object.

        Args:
            account_number (int): The account number.
            client_number (int): The client number.
            balance (float, optional): The initial balance of the account. Defaults to 0.0.
            date_created (date, optional): The date the account was created. Defaults to the current date.

        Raises:
            ValueError: If account_number or client_number is not an integer.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        if not isinstance(date_created, date):
            raise ValueError("Date created must be a valid date.")
        self._date_created = date_created

        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

    @property
    def account_number(self):
        """
        Returns the account number.

        Returns:
            int: The account number.
        """
        return self.__account_number

    @property
    def client_number(self):
        """
        Returns the client number.

        Returns:
            int: The client number.
        """
        return self.__client_number

    @property
    def balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.__balance

    def update_balance(self, amount):
        """
        Updates the balance by adding the given amount.

        Args:
            amount (float): The amount to add to the balance.

        Raises:
            ValueError: If amount is not a numeric value.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a numeric value.")
        
        self.__balance += float(amount)

        if self.__balance < self.LOW_BALANCE_LEVEL:
            raise ValueError(f"Low balance warning ${self.__balance:,.2f}: on account {self.__account_number}.")

        
        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            raise ValueError(f"Large transaction ${amount:,.2f}: on account {self.__account_number}.")

    def deposit(self, amount):
        """
        Deposits the given amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If amount is not a positive numeric value.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
            self.update_balance(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

    def withdraw(self, amount):
        """
        Withdraws the given amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If amount is not a positive numeric value or exceeds the account balance.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
            if amount > self.__balance:
                raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self.__balance:,.2f}")
            self.update_balance(-amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

    def __str__(self):
        """
        Returns a string representation of the account.

        Returns:
            str: A string representation of the account.
        """
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}\n"
         
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Abstract method: Calculates and returns the service charges.

        Returns:
            float: The service charges for the bank account.
        """
        return self.BASE_SERVICE_CHARGE
