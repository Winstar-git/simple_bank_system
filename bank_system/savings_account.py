from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, pin, balance=0.0):
        super().__init__(account_number, account_holder, pin, balance)
        self._role = "Customer"

    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Deposited amount must be positive")
        self._balance += amount
        self.add_transactions(f"Deposited: P{amount:.2f}")
        return self._balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient Funds")
        self._balance -= amount
        self.add_transactions(f"Withdrew: P{amount:.2f}")
        return self._balance
        
    def get_balance(self):
        return self._balance