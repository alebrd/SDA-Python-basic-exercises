capital = int(input("Enter Principle: "))
no_years = int(input("Enter number of years: "))
interest_rate = 3.5

i = 1
while i <= no_years:
    capital += capital * (interest_rate/100)
    i += 1
print(f'{capital:.2f}')

capital = int(input("Write initial capital here:"))
interest = float(input("Write interest rate here:"))
years = int(input("Write number of years here:"))
i=1
for i in range(years):
    capital = capital + capital * (interest / 100)
    i += 1
print(capital)




