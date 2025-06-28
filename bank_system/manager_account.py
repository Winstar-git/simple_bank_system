from account import Account

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
            "Balance" : self._balance
        }