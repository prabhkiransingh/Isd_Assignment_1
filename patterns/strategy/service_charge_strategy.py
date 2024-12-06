from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Base class for service charge strategies.
    
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account):
        """
        Calculates the service charge for a given bank account.

        Args:
            account: The bank account to calculate the service charge for.

        Returns:
            The service charge amount.
        """
        pass