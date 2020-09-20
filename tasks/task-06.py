a = int(input())
b = int(input())
empty_lst = []
empty_lst.append(a)
if b < a:
    print("Job finished")
while a < b:
    a += 1
    empty_lst.append(a)
    print(sum(empty_lst[:]))


a = int(input())
b = int(input())

if b <= a:
    print("Job finished")
else:
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print(sum)

