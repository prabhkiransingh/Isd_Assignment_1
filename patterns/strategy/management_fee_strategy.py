from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta



class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    A strategy for calculating service charges that includes management fees based on account age.

    Attributes:
        TEN_YEARS_AGO (date): A class constant representing the date 10 years ago from today.
        __management_fee (float): The management fee to be applied to account.
        __date_created (date): The creation date of the account.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days= 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with the account creation date and management fee.

        Args:
            date_created (date): The date when the account was created.
            management_fee (float): The management fee to be applied to account.
        """
        self.__management_fee = management_fee
        self.__date_created = date_created

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges for the account, including management fees if applicable.

        Args:
            account (BankAccount): The BankAccount object for which to calculate the service charges.

        Returns:
            float: The total service charge including management fees if applicable.
        """
        base_service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        if self.__date_created <= self.TEN_YEARS_AGO:
            return base_service_charge 
        else:
            return base_service_charge + self.__management_fee  


