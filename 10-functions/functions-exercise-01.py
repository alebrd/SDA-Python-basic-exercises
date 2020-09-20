def max_of_three(a, b, c):
    if b < a > c:
        return a
    elif b < c > a:
        return c
    else:
        return b


print(max_of_three(5, 20, 1))


# def max_list(number):
#     i = 0
#     a = 0
#     maximum = number[0]
#     while i != len(number):
#         if number[i] > maximum:
#             maximum = number[i]
#         i += 1
#     return maximum
#
#
# print(max_list([3, 10, 1]))


def max_value(number):
    maximum = number[0]
    for i in number:
        if i > maximum:
            maximum = i
    return maximum


print(max_value([1, 2, 3, 10, 50, 20]))
