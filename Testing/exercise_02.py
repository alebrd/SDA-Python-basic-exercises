def odd_indexes(string):
    if type(string) is str:
        return string[1::2]
    else:
        return string