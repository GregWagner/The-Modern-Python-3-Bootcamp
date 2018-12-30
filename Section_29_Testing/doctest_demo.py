""" Execute doctest with
python3 -m doctest -v filename
"""

def add(a, b):
    """
    >>> add(2, 3)
    5
    >>> add(100, 200)
    300
    """
    return a + b

def double(values):
    """ double the values in a list

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * value for value in values]
