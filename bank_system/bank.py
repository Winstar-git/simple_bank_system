import json
import os
from savings_account import SavingsAccount
from account import Account

class Bank(Account):
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        if os.path.exists("bank_data.json"):
            with open("bank_data.json", "r") as file:
                data = json.load(file)
                for acc_no, details in data.items():
                    acc = SavingsAccount(
                        acc_no,
                        details["account_holder"],
                        details["pin"],
                        details.get("balance", 0.0)
                    )
                    self.accounts[acc_no] = acc
    
    def save_data(self):
        data = {}
        for acc_no, acc in self.accounts():
            data[acc_no] = {
                "account_holder": acc._account_holder,
                "pin": acc._pin,
                "balance": acc.get_balance()
            }
        with open("bank_data.json", "a") as file:
            json.dump(data, file, indent=4)

    def add_account(self,account):
        self.accounts[account._account_number] = account
        self.save_data()

    def get_account(self, acc_no, pin):
        acc = self.accounts.get(acc_no)
        if acc and acc.verify_pin(pin):
            return acc
        return None
    def get_tottal_balance(self):
        return sum(acc.get_balance() for acc in self.accounts.values())
    
    def get_total_users(self):
        return len(self.accounts)