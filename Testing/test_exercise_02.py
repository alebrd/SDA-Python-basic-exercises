def odd_indexes(string):
    if type(string) is str:
        return string[1::2]
    else:
        return string

def test_odd_indexes():
    assert odd_indexes(5)


 