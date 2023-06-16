from hello import more_hello, more_goog


def test_more_hello():
    assert "hi" == more_hello()


def test_more_goog():
    assert "go" == more_goog()


# nonsense code that generates a warning
# var = 1
# var = var

# bad syntax
# foo=
