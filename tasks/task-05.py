def odds_numbers(positive_integers):
    for i in range(0, positive_integers + 1):
        if i % 2 == 0:
            continue
        else:
            print(i)


print(odds_numbers(15))
