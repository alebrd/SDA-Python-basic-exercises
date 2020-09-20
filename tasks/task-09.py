import sys
min = sys.maxsize * 2 + 1
max = -sys.maxsize - 1

while True:
    number = int(input())
    if number > max:
        max = number
    if number < min:
        min = number
    if number == 0:
        break

print(max + min)
print((max + min) / 2)



number = ""
num_list = []

while number != 0:
    number = int(input())
    num_list.append(number)

# smallest = min(num_list)
# biggest = max(num_list)

num_list.sort()
smallest = num_list[-1]
biggest = num_list[0]

print(f"{smallest + biggest}")
print(f"{(smallest + biggest) / 2}")



n = int(input())
my_list = []
total = 0
while n != 0:
    my_list.append(n)
    n = int(input())
summa = max(my_list) + min(my_list)
print(summa)
print(summa/2)