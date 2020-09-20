input_string = "Python is a really strong programming language!"

remainder = len(input_string) % 2
amount_of_letters = 2

middle_index = len(input_string) // 2
start_index = middle_index - amount_of_letters
end_index = middle_index + amount_of_letters + remainder

result = input_string[start_index:end_index]

print(f"Result: '{result}'")





