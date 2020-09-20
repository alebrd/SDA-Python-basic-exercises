numbers = {1: "one", 2: "two", 3: "three"}

# a.
print(numbers)

# b.
numbers[4] = "four"

# c.       printing 2 the key word REMEMBER I AM CALLING THE KEY WORD AND NOT THE INDEX NUMBER OF THE DICTIONARY
print(numbers[2])

# d        trying to print not defined key word 10, give us back an error
# print(numbers[10])

# e.       trying to print not defined key word with the get method. in this way instead of an error u get a None
print(numbers.get(10))

# f.      avoiding the error and giving a the not defined key word 10 a temporally value, in this case 'unknown'
print(numbers.get(10, "unknown"))

# g.     if the key word is defined then you get its real value, so in this case three
print(numbers.get(3, "unknown"))

# h.     removing 2 by using pop method, in this way it shows which value are u removing
print(numbers.pop(2))
print(numbers)

# i.     updating the dictionary with
numbers.update({0: "zero"})
print(numbers)

# j.
numbers.clear()
print(numbers)



