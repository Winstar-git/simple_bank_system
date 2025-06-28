from account import Account
from savings_account import SavingsAccount
import random

class ManagerAccount(Account):
    def __init__(self, account_number, account_holder, pin):
        super().__init__(account_number, account_holder, pin)
        self._role = "Manager"

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def verify_pin(self, input_pin):
        return self._pin == input_pin

    def get_account_info(self):
        return {
            "Account Number": self._account_number,
            "Account Holder": self._account_holder
        }

    def create_account(self, name, bank):
        acc_number = str(random.randint(100000, 999999))
        pin = str(random.randint(1000, 9999))
        new_customer = SavingsAccount(acc_number, name, pin)
        bank.add_account(new_customer)
        return {
            "account_number": acc_number,
            "pin": pin
        }