n = int(input())

current_power_of_two = 1

while True:
    print(current_power_of_two)
    current_power_of_two *= 2
    if current_power_of_two >= n:
        break
