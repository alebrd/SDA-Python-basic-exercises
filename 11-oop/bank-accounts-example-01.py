from user import User
from user import BankAccount


femi = User("Femi", "femi@sda.com", "Washington DC")
frank = User("Frank", "frank@sda.com", "12 Helsinki")
femi_account = BankAccount(femi, 0, "savings", 100)
frank_account = BankAccount(frank, 740, "savings", 2500)
# print(femi_account.user.email)
# femi_account.credit(50)
# print(femi_account.balance)
# femi_account.credit(23)
# print(femi_account.balance)
#
#
# femi_account.debit(1)
# print(femi_account.balance)
# femi_account.debit(100)
print(femi_account.balance)
print(frank_account.balance)
# femi_account.credit(500)
# print(femi_account.__balance)
frank_account.transfer(femi_account, 50)
print(femi_account.balance)
print(frank_account.balance)
