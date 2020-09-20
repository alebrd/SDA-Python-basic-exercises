given_dictionary = {1: 'one', 2: 'two', 3: 'three'}

print(len(given_dictionary))  # a

given_dictionary[4] = 'four'  # b
print(given_dictionary)

print(given_dictionary[2])  # c

print(given_dictionary.get(10))  # e

print(given_dictionary.get(10, 'unknown'))  # f

print(given_dictionary.get(3, 'unknown'))  # g

given_dictionary.pop(2)  # h
print(given_dictionary)

new_dictionary = {0: 'zero'}   # i
given_dictionary.update(new_dictionary)
print(given_dictionary)

given_dictionary.clear()  #j
print(given_dictionary)
