try:
    # value = 10 / 0
    number = int(input('Enter a number'))
    print(number)
except ValueError as err:
    print(err)

except ZeroDivisionError as err:
    print(err)
