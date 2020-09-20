import sys

country_capital_dict = {}

country_and_capital_names_input = sys.argv[1]

country_and_capital_name_list = country_and_capital_names_input.split(",")

country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

country_and_capital_names_input = sys.argv[2]

country_and_capital_name_list = country_and_capital_names_input.split(",")

country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

country_and_capital_names_input = sys.argv[3]

country_and_capital_name_list = country_and_capital_names_input.split(",")

country_capital_dict[country_and_capital_name_list[0]] = country_and_capital_name_list[1]

print(country_capital_dict)


country_capital = {}
for i in range(1, len(sys.argv)):
    country, capital = sys.argv[i].split(",")
    country_capital[country] = capital
print(country_capital)