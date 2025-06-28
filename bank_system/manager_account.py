from account import Account
from savings_account import SavingsAccount
from bank import Bank
import random

class ManagerAccount(Account):
    def __init__(self, account_number, account_holder, pin):
        self._account_number = account_number
        self._account_holder = account_holder
        self._pin = pin
        self._role = "Manager"

    def verify_pin(self,input_pin):
        return self._pin == input_pin
    
    def get_account_info(self):
        return {
            "Account Number": self._account_number,
            "Account Holder": self._account_holder,
        }
    
    def create_acc(self,name,):
        acc_number = str(random.randint(1000000, 999999))
        pin = str(random.randint(1000, 9999))
        new_customer = SavingsAccount(acc_number, name, pin)
        Bank.add_account(new_customer)
        return {
            "account_number" : acc_number,
            "pin" : pin
        }