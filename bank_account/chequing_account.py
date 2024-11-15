from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy
class ChequingAccount(BankAccount):
    
     

    def __init__(self, account_number: int, client_number: int, balance: float, date_created, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes a ChequingAccount object.

        Args:
            account_number (int): The account number.
            client_number (int): The client number.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            overdraft_limit (float): The overdraft limit for the account.
            overdraft_rate (float): The overdraft rate (as a percentage).

        Raises:
            ValueError: If overdraft limit or overdraft rate is not valid.
        """
        
        super().__init__(account_number, client_number, balance, date_created)

        
        if not isinstance(overdraft_limit, (float)):
            raise ValueError("Overdraft limit must be a numeric value.")
        self.__overdraft_limit = float(overdraft_limit)

        if not isinstance(overdraft_rate, (float)) or overdraft_rate < 0 or overdraft_rate > 1:
            raise ValueError("Overdraft rate must be a float between 0 and 1.")
        self.__overdraft_rate = float(overdraft_rate)

        self.__overdraft_strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    def __str__(self) -> str:
        """
        Returns a string representation of the chequing account.
        """
        base_string = super().__str__()
        overdraft_limit_str = f"${self.__overdraft_limit:.2f}"
        overdraft_rate_str = f"{self.__overdraft_rate * 100:.2f}%"
        return f"{base_string}Overdraft Limit: {overdraft_limit_str} Overdraft Rate: {overdraft_rate_str} Account Type: Chequing"

    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the account.

        Returns:
            float: The total service charge including overdraft fees if applicable.
        """
        return self.__overdraft_strategy.calculate_service_charges(self)