def number_of_evens(numbers):
    return 0


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    """
    Test that two values are not equal. Raises AssertionError if both values
    are not equal.
    `a` is the actual value produced
    `b` is the value that was supposed to be produced
    """
    assert a != b, "{0} is equal to {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)


test_are_equal(number_of_evens(2), 2)