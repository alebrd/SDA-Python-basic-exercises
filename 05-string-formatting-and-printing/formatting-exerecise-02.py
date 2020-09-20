header1 = 'Name'
header2 = 'Age'
header3 = 'Salary'
name1 = 'John Doe'
name2 = 'John Wick'
name3 = 'Jeff Bezos'
age1 = 27
age2 = 40
age3 = 45
salary1 = 12345.34
salary2 = 500000
salary3 = 100000000
print(f'| {header1:15}| {header2:5} | {header3:12} |')
print("-" * 42)
print(f'| {name1:15} | {age1:5} | {salary1:<12} |')
print(f'| {name2:15} | {age2:5} | {salary2:<12} |')
print(f'| {name3:15} | {age3:5} | {salary3:<12} |')