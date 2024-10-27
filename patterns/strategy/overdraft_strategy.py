
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges for the account, including overdraft fees if applicable.

        Args:
            account (BankAccount): The BankAccount object for which to calculate the service charges.

        Returns:
            float: The total service charge including overdraft fees if applicable.
        """
        if account.balance >= self.__overdraft_limit:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            overdraft_amount = self.__overdraft_limit - account.balance
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE + overdraft_amount * self.__overdraft_rate