"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: {Prabhkiran Singh}
Date: {10/27/2024}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
from datetime import date
from bank_account import BankAccount, ChequingAccount, SavingsAccount
from client.client import Client

# 2. Create a Client object with data of your choice.
client1 = Client(1, "Prabhkiran", "Singh", "PrabhkiranSingh@gmail.com")

# 3a. Create a ChequingAccount object with data of your choice
chequing_account = ChequingAccount(
    account_number=20019,
    client_number=client1.client_number,
    balance=1000.0,
    date_created=date.today(),
    overdraft_limit=200.0,
    overdraft_rate=0.05
)

# 3b. Create a SavingsAccount object with data of your choice
savings_account = SavingsAccount(
    account_number=20020,
    client_number=client1.client_number,
    balance=1000.50,
    date_created=date.today(),
    minimum_balance=100.00
)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a. Attach the Client object (created in step 2) to the ChequingAccount object

# 4b. Attach the Client object (created in step 2) to the SavingsAccount object


# 5a. Create a second Client object with data of your choice
client2 = Client(2, "Parry", "Sidhu", "Prrsidhu@gmail.com")

# 5b. Create a SavingsAccount object with data of your choice
savings_account2 = SavingsAccount(
    account_number=20021,
    client_number=client2.client_number,
    balance=1050.50,
    date_created=date.today(),
    minimum_balance=101.00
)


# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
try:
    chequing_account.deposit(12000)  
except Exception as e:
    print(f"ChequingAccount deposit error: {e}")

try:
    chequing_account.withdraw(50000)   
except Exception as e:
    print(f"ChequingAccount withdraw error: {e}")


try:
    savings_account.deposit(30000)    
except Exception as e:
    print(f"SavingsAccount deposit error: {e}")

try:
    savings_account.withdraw(100000)    
except Exception as e:
    print(f"SavingsAccount withdraw error: {e}")


try:
    savings_account2.deposit(500000)   
except Exception as e:
    print(f"SavingsAccount2 deposit error: {e}")

try:
    savings_account2.withdraw(4000000)  
except Exception as e:
    print(f"SavingsAccount2 withdraw error: {e}")
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

