# Implement your solution here
amount = float(input())
number_of_installments = int(input())

if amount < 100.0 or amount > 10000.0:
    amount = 5000
if number_of_installments < 6 or number_of_installments > 48:
    number_of_installments = 36
if number_of_installments <= 12:
    interest_rate = 0.025
elif number_of_installments <= 24:
    interest_rate = 0.05
else:
    interest_rate = 0.1


print(amount * (1.0 + interest_rate) / number_of_installments)

