

country_capital = {}
country, capital = input("Enter country and capital: ").split(",")
country_capital[country] = capital
print(country_capital)
country, capital = input("Enter country and capital: ").split(",")
country_capital[country] = capital
print(country_capital)
country, capital = input("Enter country and capital: ").split(",")
country_capital[country] = capital
print(country_capital)

# SAME EXERCISE WITH FOR LOOP INSTEAD
countries_capitals = {}

for i in range(3):
    county, capital = input('insert county and capital: ').split(',')
    countries_capitals[county] = capital

print(countries_capitals)
