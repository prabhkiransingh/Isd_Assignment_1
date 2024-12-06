from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox
from bank_account.bank_account import BankAccount
import copy
from ui_superclasses.details_window import DetailsWindow

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)  

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        
        self.account = None
        
        if isinstance(account, BankAccount):
            # Store a copy of the account to avoid external modifications
            self.account = copy.deepcopy(account)
            
            # Update account labels with the current account information
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:.2f}")
            
            # Connect buttons to corresponding methods
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()

    def __on_apply_transaction(self):
        """
        Attempt to perform a transaction (deposit or withdraw) using the amount entered
        into the corresponding BankAccount. Update balanceLabel upon success.
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Deposit Failed", "Please enter a valid amount.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            # Update balance label and clear amount field
            self.balance_label.setText(f"${self.account.balance:.2f}")
            self.transaction_amount_edit.clear()

            # Emit signal to notify that balance has been updated
            self.balance_updated.emit(self.account)

        except Exception as e:
            QMessageBox.warning(self, "Transaction Failed", 
                                f"{transaction_type} failed: {str(e)}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    def __on_exit(self):
        """
        Close the AccountDetails window and return to the ClientLookup window.
        """
        self.close()
