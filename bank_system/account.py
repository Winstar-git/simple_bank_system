from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, account_holder, pin, balance=0.0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._pin = pin
        self._balance = balance
        self._transactions = []

    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
       pass