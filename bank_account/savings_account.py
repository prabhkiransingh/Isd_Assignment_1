from bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy 
class SavingsAccount(BankAccount):
    """
    A class representing a Savings Account, inheriting from BankAccount.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """
        Initialize a SavingsAccount object.

        Args:
            account_number (int): The unique account number.
            client_number (int): The client's identification number.
            balance (float): The initial account balance.
            date_created (date): The date the account was created.
            minimum_balance (float): The minimum balance required for the account.

        If minimum_balance is not a valid float, it defaults to 50.0.
        """
        super().__init__(account_number, client_number, balance, date_created)

        if not isinstance(minimum_balance, float):
            raise ValueError("Minimum balance must be a float.")
        
        self.__minimum_balance = minimum_balance
        self.__minimum_balance_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    @property
    def minimum_balance(self) -> float:
        """
        Get the minimum balance required for the account.

        Returns:
            float: The minimum balance.
        """
        return self.__minimum_balance

    def __str__(self) -> str:
        """
        Return a string representation of the SavingsAccount.

        Returns:
            str: A string containing account details including the minimum balance.
        """
        base_string = super().__str__()  
        return f"{base_string}Minimum Balance: ${self.minimum_balance:.2f} Account Type: Savings"

    def get_service_charges(self) -> float:
        """
        Calculate the service charges for the account using MinimumBalanceStrategy.

        Returns:
            float: The calculated service charge.
        """
        return self.__minimum_balance_strategy.calculate_service_charges(self.balance)
