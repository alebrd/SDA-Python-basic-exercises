def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


print(f'is 999999 prime: {is_prime(134252599)}')
print(f'is 25 prime: {is_prime(25)}')
print(f'is 27 prime: {is_prime(27)}')
print(f'is 3 prime: {is_prime(3)}')
