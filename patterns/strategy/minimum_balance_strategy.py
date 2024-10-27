from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initialize the MinimumBalanceStrategy object.

        Args:
            base_service_charge (float): The base service charge.
            minimum_balance (float): The minimum balance required for the account.
        """
        self.__minimum_balance = minimum_balance
        

    def calculate_service_charges(self, balance: float) -> float:
        """
        Calculate the service charges based on the account balance.

        Args:
            balance (float): The current balance of the account.

        Returns:
            float: The calculated service charge.
        """
        if balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM