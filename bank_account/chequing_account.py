from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    BASE_SERVICE_CHARGE = 0.50  

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
        self.overdraft_limit = float(overdraft_limit)

        if not isinstance(overdraft_rate, (float)) or overdraft_rate < 0 or overdraft_rate > 1:
            raise ValueError("Overdraft rate must be a float between 0 and 1.")
        self.overdraft_rate = float(overdraft_rate)

    def __str__(self) -> str:
        """
        Returns a string representation of the chequing account.
        """
        base_str = super().__str__()
        overdraft_limit_str = f"${self.overdraft_limit:.2f}"
        overdraft_rate_str = f"{self.overdraft_rate * 100:.2f}%"
        return f"{base_str}Overdraft Limit: {overdraft_limit_str} Overdraft Rate: {overdraft_rate_str} Account Type: Chequing"

    def get_service_charges(self) -> float:
        """
        Calculates the service charges for the account.

        Returns:
            float: The total service charge including overdraft fees if applicable.
        """
        if self.balance >= self.overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            overdraft_amount = self.overdraft_limit - self.balance
            return self.BASE_SERVICE_CHARGE + overdraft_amount * self.overdraft_rate
