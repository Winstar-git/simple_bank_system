import json
import os
from savings_account import SavingsAccount
from manager_account import ManagerAccount

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def load_data(self):
        print(">>> load_data() called")

        file_path = os.path.join(os.path.dirname(__file__), "bank_data.json")
        if not os.path.exists(file_path):
            file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bank_data.json")
        print(f">>> Looking for JSON at: {file_path}")
        print(f">>> File exists: {os.path.exists(file_path)}")

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
        print(f"Total accounts loaded: {len(self.accounts)}")

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
        print(f"get_account() → acc_no={acc_no}, pin={pin}")
        acc = self.accounts.get(str(acc_no))  # Ensure acc_no is a string
        if acc:
            print(f"Found account: {acc._account_holder}")
            if acc.verify_pin(str(pin)):  # Also ensure pin is a string
                print("PIN verified")
                return acc
            else:
                print("Wrong PIN")
        else:
            print("Account number not found in memory.")
        return None

    def get_total_balance(self):
        return sum(acc.get_balance() for acc in self.accounts.values() if hasattr(acc, "get_balance"))

    def get_total_users(self):
        return len([acc for acc in self.accounts.values() if hasattr(acc, "get_balance")])