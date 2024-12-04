"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(20019, 1010, 1000.50, date(2024, 5, 10), -200.0, 0.05)
except ValueError as e:
    print (f"Error creating Chequing Account: {e}")


# 3. Print the ChequingAccount created in step 2.
print(chequing_account)
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service charges: {chequing_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges : {e}")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.deposit(1000.0)
except Exception as e:
    print(f"Error during deposit: {e}")
# 4b. Print the ChequingAccount
print(chequing_account)
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    print(f"Service Charges: {chequing_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try: 
    savings_account = SavingsAccount(20019, 1010, 1000.50, date.today(), 100.00)
except ValueError as e:
    print(f"Error creating Savings Account: {e}")

# 6. Print the SavingsAccount created in step 5.
print(savings_account)
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    print(f"Service Charges: {savings_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
try:
    savings_account.withdraw(1550.0)
except Exception as e:
    print(f"Error during withdrawal: {e}")

# 7b. Print the SavingsAccount.
print(savings_account)

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

try:
    print(f"Service Charges: {savings_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account = InvestmentAccount(20019, 1010, 1000.50, date(2008, 10, 5), 2.55)
except ValueError as e:
    print(f"Error creating InvestmentAccount: {e}")

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account)

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
try:
    print(f"Service Charges: {investment_account.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    investment_account1 = InvestmentAccount(20019, 1010, 1000.50, date(2015, 1, 1), 1.50)
except ValueError as e:
    print(f"Error creating InvestmentAccount: {e}")

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account1)

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
try:
    print(f"Service Charges: {investment_account1.get_service_charges()}")
except Exception as e:
    print(f"Error calculating service charges: {e}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
for account in [chequing_account, savings_account, investment_account, investment_account1]:
    try:
        service_charges = account.get_service_charges()
        account.withdraw(service_charges)
    except Exception as e:
        print(f"Error updating balance for account {account}: {e}")


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(chequing_account)
print(savings_account)
print(investment_account)
print(investment_account1)