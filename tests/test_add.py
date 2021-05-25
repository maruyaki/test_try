from add import add

def test_add():
    value1 = 2
    value2 = 4
    expected = 6
    actual = add(value1, value2)
    assert actual == expected
