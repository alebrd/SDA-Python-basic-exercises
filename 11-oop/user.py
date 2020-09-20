import datetime
import uuid


class BalanceNotSufficient(Exception):
    pass


class LimitExceeded(Exception):
    pass


class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address


class BankAccount:
    def __init__(self, input_user, input_balance, input_type, input_limit):
        self.user = input_user
        self.__balance = input_balance
        self.type = input_type
        self.limit = input_limit
        self.created = datetime.datetime.now()
        self.number = str(uuid.uuid4())

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if (self.__balance + amount) <= self.limit:
            self.__balance += amount
        else:
            raise LimitExceeded

    def debit(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise BalanceNotSufficient

    def credit(self, amount):
        self.balance += amount

    def transfer(self, recipient, amount):
        self.debit(amount)
        recipient.credit(amount)


