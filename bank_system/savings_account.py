class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, pin, balance=0.0):
        super().__init__(self, account_holder, account_number, pin)
        self._balance = balance
        self._role = "Customer"