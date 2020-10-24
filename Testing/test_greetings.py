

def greetings(person):
    return 'Hi {name}'.format(**person)


def test_greetings():
    Ale = {'name': 'Ale'}       # Arrange
    greeting = greetings(Ale)   # Act
    assert greeting == 'Hi Ale'
