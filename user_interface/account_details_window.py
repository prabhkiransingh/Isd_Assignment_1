from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.

    Attributes:
        balance_updated (Signal): A signal emitted when the account balance is updated.
        account (BankAccount): The bank account associated with this window.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetailsWindow.

        Args:
            account (BankAccount): The bank account to be displayed and managed.

        Raises:
            TypeError: If the provided account is not an instance of BankAccount.
        """
        super().__init__()
        
        if isinstance(account, BankAccount):
            # Create a copy of the account to avoid modifying the original
            self.account = copy.copy(account)
            
            # Initialize the display with account details
            self.update_display()
            
            # Connect UI elements to their respective functions
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            # Reject the window creation if the account is not valid
            self.reject()
    
    def update_display(self):
        """
        Updates the account number and balance display in the UI.

        This method should be called whenever the account details change.
        """
        self.account_number_label.setText(f"Account Number: {self.account.account_number}")
        self.balance_label.setText(f"Balance: ${self.account.balance:.2f}")
            
    def __on_apply_transaction(self):
        """
        Handles deposit and withdraw transactions.

        Raises:
            ValueError: If the entered amount is not a valid number.
            Exception: If the transaction fails for any reason (e.g., insufficient funds).
        """
        try:
            # Attempt to convert the entered amount to a float
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a valid amount")
            self.transaction_amount_edit.setFocus()
            return
            
        try:
            # Determine the transaction type based on which button was clicked
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            else:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)
                
            # Update the display to reflect the new balance
            self.update_display()
            
            # Clear the transaction amount field and set focus
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
            
            # Emit the balance_updated signal to notify listeners
            self.balance_updated.emit(self.account)
            
            # Show a success message with transaction details
            QMessageBox.information(self, "Transaction Successful", 
                                    f"{transaction_type} of ${amount:.2f} successful\n"
                                    f"Account Number: {self.account.account_number}\n"
                                    f"New Balance: ${self.account.balance:.2f}")
            
        except Exception as e:
            # Show an error message if the transaction fails
            QMessageBox.critical(
                self,
                "Error",
                f"{transaction_type} failed: {str(e)}"
            )
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
    
    def __on_exit(self):
        """
        Closes the dialog window.

        This method is called when the exit button is clicked.
        """
        self.close()