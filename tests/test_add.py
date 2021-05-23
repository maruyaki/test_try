from add import add

def test_add(capsys):
    value1 = 2
    value2 = 4
    expected = 6
    actual = add(value1, value2)
    out, err = capsys.readouterr()
    assert out == expected
