from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()  # Initialize the LookupWindow superclass
        self.__client_listing, self.__accounts = load_data()

        # Connect the lookup button click event to the on_lookup_client method
        self.lookup_button.clicked.connect(self.on__lookup_client)  
        # Connect the account table's cell click event to the on_select_account method
        self.account_table.cellClicked.connect(self.on__select_account)  
        # Connect the filter button click event to the on_filter_clicked method
        self.filter_button.clicked.connect(self.on__filter_clicked)  

    def on__lookup_client(self):
        # Obtain the client number entered by the user
        try:
            client_number = int(self.client_number_edit.text().strip())  # Convert to int
        except ValueError:
            QMessageBox.warning(self, "Non-Numeric Client", "The client number must be numeric.")
            self.reset_display()  # Reset display if invalid input
            return

        # Check if the client exists in the client listing
        if client_number not in self.__client_listing:
            QMessageBox.warning(self, "Client Not Found", f"Client Number {client_number} does not exist.")
            self.reset_display()  # Reset display if client not found
            return

        # Display client information
        client = self.__client_listing[client_number]
        self.client_info_label.setText(f"{client.first_name} {client.last_name}")  # Set client name

        # Clear the table before populating with new data
        self.account_table.setRowCount(0)

        # Display all accounts associated with the client
        for account in self.__accounts.values():
            if account.client_number == client_number:
                row_index = self.account_table.rowCount()  # Get the next available row
                self.account_table.insertRow(row_index)  # Insert new row

                # Add account details to the row in the table
                self.account_table.setItem(row_index, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_index, 1, QTableWidgetItem(f"${account.balance:.2f}"))
                self.account_table.setItem(row_index, 2, QTableWidgetItem(str(account._date_created)))
                self.account_table.setItem(row_index, 3, QTableWidgetItem(account.__class__.__name__))

        # Resize columns to fit content
        self.account_table.resizeColumnsToContents()
        if self.client_number_edit:
        # Toggle filter to indicate data is not filtered
            self.__toggle_filter(False)

    @Slot(int, int)
    def on__select_account(self, row: int, column: int):
        account_number_item = self.account_table.item(row, 0)  # The account number is in column 0
        if not account_number_item:
            QMessageBox.warning(self, "Invalid Selection", "No account selected.")
            return

        account_number = int(account_number_item.text().strip())
        if account_number not in self.__accounts:
            QMessageBox.warning(self, "Bank Account does not Exist", f"Bank Account {account_number} does not exist.")
            return

        account = self.__accounts[account_number]
        details_window = AccountDetailsWindow(account)  # Pass the BankAccount object to the AccountDetailsWindow

        details_window.balance_updated.connect(self.__update_data)
        details_window.exec_()

    @Slot(BankAccount)
    def __update_data(self, account: BankAccount):
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if account_number_item and account_number_item.text() == str(account.account_number):
                balance_item = self.account_table.item(row, 1)
                if balance_item:
                    balance_item.setText(f"${account.balance:.2f}")
                self.__accounts[account.account_number] = account
                break

        update_data(account)  # Ensure the data is updated in the file

    @Slot()
    def on__filter_clicked(self):
        if self.filter_button.text() == "Apply Filter":
            # Get filter column index and filter text
            filter_column = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().lower()

            # Filter rows in account_table
            for i in range(self.account_table.rowCount()):
                # Get the item for the selected column
                item = self.account_table.item(i, filter_column)
                
                # Check if filter text is in the item's text (case-insensitive)
                if item and filter_text not in str(item.text()).lower():
                    self.account_table.setRowHidden(i, True)
                else:
                    self.account_table.setRowHidden(i, False)

            # Toggle filter to indicate filtering is applied
            self.__toggle_filter(True)
        else:
            # Reset filtering
            self.__toggle_filter(False)
    def __toggle_filter(self, filter_on):
        # Initially enable filter button
        self.filter_button.setEnabled(True)

        if filter_on:
            # Filtering is applied
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            # Restore full data view
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            # Show all rows
            for i in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(i, False)
            
            self.filter_label.setText("Data is Not Currently Filtered")