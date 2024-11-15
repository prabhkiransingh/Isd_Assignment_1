from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy  

class InvestmentAccount(BankAccount):
    """
    A class representing an Investment Account, inheriting from BankAccount.
    
    This account type has a management fee that is applied to service charges
    for accounts less than 10 years old.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
        """
        Initialize an InvestmentAccount object.

        Args:
            account_number (int): The unique account number.
            client_number (int): The client's identification number.
            balance (float): The initial account balance.
            date_created (date): The date the account was created.
            management_fee (float): The management fee for the account.

        Raises:
            ValueError: If date_created is not a valid date object.

        """
        super().__init__(account_number, client_number, balance, date_created)

        if not isinstance(date_created, date):
            raise ValueError("Invalid date_created")
        
        if not isinstance(management_fee, (float)):
            raise ValueError("Management fee must be a number.")
        
        if not isinstance(balance, (float)):
            raise ValueError("Balance must be a number.")
        self.__management_fee = float(management_fee)
        
        self.__management_fee_strategy = ManagementFeeStrategy(date_created, self.__management_fee)  
    
            

    def get_service_charges(self) -> float:
        """
        Calculate the service charges for the account.

        Returns:
            float: The calculated service charge. For accounts older than 10 years,
                only the base service charge is applied. For newer accounts,
                the management fee is added to the base service charge.
        """
        return self.__management_fee_strategy.calculate_service_charges(self)
    def __str__(self) -> str:
        """
        Return a string representation of the InvestmentAccount.

        Returns:
            str: A string containing account details including the date created
                 and management fee information.
        """
        base_string = super().__str__()  
        management_fee_str = (
            f"Management Fee: ${self.__management_fee:.2f} Account Type: Investment" 
            if self._date_created > self.TEN_YEARS_AGO else 
            "Management Fee: Waived Account Type: Investment"
        )
        
        return f"{base_string}Date Created: {self._date_created}\n{management_fee_str}"