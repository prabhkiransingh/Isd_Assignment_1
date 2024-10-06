from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """
    A class representing a Savings Account, inheriting from BankAccount.
    """

    SERVICE_CHARGE_PREMIUM = 2.0

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

        if not isinstance(minimum_balance, (float)):
            raise ValueError("Minimum balance must be a number.")
        
        try:
            self._minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self._minimum_balance = 50.0  
            

    @property
    def minimum_balance(self) -> float:
        """
        Get the minimum balance required for the account.

        Returns:
            float: The minimum balance.
        """
        return self._minimum_balance

    def __str__(self) -> str:
        """
        Return a string representation of the SavingsAccount.

        Returns:
            str: A string containing account details including the minimum balance.
        """
        base_str = super().__str__()  
        return f"{base_str}Minimum Balance: ${self.minimum_balance:.2f} Account Type: Savings"

    def get_service_charges(self) -> float:
        """
        Calculate the service charges for the account.

        If the balance is below the minimum balance, a premium charge is applied.

        Returns:
            float: The calculated service charge.
        """
        if self.balance >= self.minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM