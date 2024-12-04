from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A window that allows the user to look up client information and their associated bank accounts.

    Attributes:
        __client_listing (dict): A dictionary containing client information, with client numbers as keys.
        __accounts (dict): A dictionary containing bank account information, with account numbers as keys.
    """

    def __init__(self):
        """
        Initializes the ClientLookupWindow by loading client and account data, and connecting signals to slots.
        """
        # Initialize parent class
        super().__init__()

        # Load client and account data
        self.__client_listing, self.__accounts = load_data()

        # Connect signals to slots
        self.lookup_button.clicked.connect(self.on__lookup_client)
        self.account_table.cellClicked.connect(self.on__select_account)

    @Slot()
    def on__lookup_client(self):
        """
        Handles the lookup of a client by their client number, and displays the associated bank accounts.
        """
        try:
            # Get and sanitize client number input
            client_number_text = self.client_number_edit.text().strip()
            if not client_number_text:
                QMessageBox.warning(self, "Error", "Please enter a client number!")
                self.reset_display()
                return

            # Validate input is numeric
            if not client_number_text.isdigit():
                QMessageBox.warning(self, "Error", "Client Number must be numeric!")
                self.reset_display()
                return

            client_number = int(client_number_text)

            # Check if client exists in listing
            if client_number not in self.__client_listing:
                QMessageBox.warning(self, "Error", f"Client Number {client_number} not found!")
                self.reset_display()
                return

            # Get client and display info
            client = self.__client_listing[client_number]
            client_name = self.get_client_name(client)
            if client_name is None:
                QMessageBox.warning(self, "Error", "Unable to retrieve client name!")
                self.reset_display()
                return

            self.client_info_label.setText(f"Client Name: {client_name}")

            # Clear existing table rows
            self.account_table.setRowCount(0)

            # Display accounts for this client
            row = 0
            for account in self.__accounts.values():
                if account.client_number == client_number:
                    self.account_table.insertRow(row)
                    self.add_account_to_table(row, account)
                    row += 1

            # If no accounts found
            if row == 0:
                QMessageBox.information(self, "No Accounts", f"No accounts found for Client Number {client_number}.")

            self.account_table.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")
            self.reset_display()

    def get_client_name(self, client):
        """
        Helper method to get the client name from various possible attributes of the client object.

        Args:
            client (object): The client object for which the name is to be retrieved.

        Returns:
            str: The client name, or None if the name could not be retrieved.
        """
        if hasattr(client, 'full_name'):
            return client.full_name
        elif hasattr(client, 'first_name') and hasattr(client, 'last_name'):
            return f"{client.first_name} {client.last_name}"
        elif hasattr(client, 'client_name'):
            return client.client_name
        elif hasattr(client, 'name'):
            return client.name
        else:
            return None

    @Slot(int, int)
    def on__select_account(self, row: int, column: int) -> None:
        """
        Handles the selection of a bank account from the account table.

        Args:
            row (int): The row index of the selected account.
            column (int): The column index of the selected account.
        """
        account_number_item = self.account_table.item(row, 0)
        
        if not account_number_item or not account_number_item.text():
            QMessageBox.warning(self, "Error", "Invalid Selection!")
            return
            
        account_number = account_number_item.text()
        
        if account_number in self.__accounts:
            bank_account = self.__accounts[account_number]
            details_window = AccountDetailsWindow(bank_account)
            details_window.exec_()
        else:
            QMessageBox.warning(self, "Error", "Bank Account does not exist!")

    def add_account_to_table(self, row, account):
        """
        Helper method to add a bank account to the account table.

        Args:
            row (int): The row index to insert the account.
            account (BankAccount): The bank account object to be added.
        """
        account_num = str(account.account_number)
        balance = f"${account.balance:.2f}"
        date = str(account._date_created)
        acc_type = account.__class__.__name__

        # Set items with proper alignment
        self.account_table.setItem(row, 0, self._create_table_item(account_num))
        self.account_table.setItem(row, 1, self._create_table_item(balance, align_right=True))
        self.account_table.setItem(row, 2, self._create_table_item(date))
        self.account_table.setItem(row, 3, self._create_table_item(acc_type))

    def _create_table_item(self, text, align_right=False):
        """
        Helper method to create a QTableWidgetItem with the specified text and alignment.

        Args:
            text (str): The text to be displayed in the table item.
            align_right (bool): Whether to align the text to the right.

        Returns:
            QTableWidgetItem: The created table item.
        """
        item = QTableWidgetItem(text)
        if align_right:
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        else:
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        return item

    def update_data(self, account: BankAccount):
        """
        Updates the account data in the table and the underlying data structure.

        Args:
            account (BankAccount): The updated bank account object.
        """
        for row in range(self.account_table.rowCount()):
            account_number_in_table = self.account_table.item(row, 0).text()
            if str(account.account_number) == account_number_in_table:
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")
                self.__accounts[account.account_number] = account
                update_data(account)  # Update CSV file
                break

        # Update the accounts dictionary with the updated BankAccount
        self.__accounts[account.account_number] = account

        # Assuming update_data is a function from the manage_data module that updates the accounts.csv file
        from user_interface.manage_data import update_data
        update_data(account)

    def on__select_account(self, account):
        """
        Handles the selection of a bank account from the account table.

        Args:
            account (BankAccount): The selected bank account object.
        """
        # Create an instance of AccountDetailsWindow
        account_details_window = AccountDetailsWindow(account)

        # Connect the signal from AccountDetailsWindow to the update_data method
        account_details_window.balance_updated.connect(self.update_data)

        # Open the AccountDetailsWindow dialog
        account_details_window.exec_()