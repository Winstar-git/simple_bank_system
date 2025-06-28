import json
import os
from savings_account import SavingsAccount
from manager_account import ManagerAccount

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        file_path = os.path.join(os.path.dirname(__file__), "bank_data.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                    for acc_no, details in data.items():
                        role = details.get("role", "Customer")
                        if role == "Customer":
                            acc = SavingsAccount(
                                acc_no,
                                details["account_holder"],
                                details["pin"],
                                details.get("balance", 0.0)
                            )
                        elif role == "Manager":
                            acc = ManagerAccount(
                                acc_no,
                                details["account_holder"],
                                details["pin"]
                            )
                        self.accounts[acc_no] = acc
                        acc._transactions = details.get("transactions", [])
                except json.JSONDecodeError:
                    print("JSON file is empty or invalid. Starting fresh.")

    def save_data(self):
        data = {}
        for acc_no, acc in self.accounts.items():
            data[acc_no] = {
                "account_holder": acc._account_holder,
                "pin": acc._pin,
                "role": getattr(acc, "_role", "Customer")
            }
            if hasattr(acc, "get_balance"):
                data[acc_no]["balance"] = acc.get_balance()
            if hasattr(acc, "get_transactions"):
                data[acc_no]["transactions"] = acc.get_transactions()

        file_path = os.path.join(os.path.dirname(__file__), "bank_data.json")
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def add_account(self, account):
        self.accounts[account._account_number] = account
        self.save_data()

    def get_account(self, acc_no, pin):
        acc = self.accounts.get(acc_no)
        if acc:
            if acc.verify_pin(pin):
                return acc
        return None

    def get_total_balance(self):
        return sum(acc.get_balance() for acc in self.accounts.values() if hasattr(acc, "get_balance"))

    def get_total_users(self):
        return len([acc for acc in self.accounts.values() if hasattr(acc, "get_balance")])