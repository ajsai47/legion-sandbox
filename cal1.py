def fizzbuzz(n: int) -> str:
    """Return 'fizzbuzz', 'fizz', 'buzz', or str(n) based on divisibility.

    >>> fizzbuzz(15)
    'fizzbuzz'
    >>> fizzbuzz(3)
    'fizz'
    >>> fizzbuzz(5)
    'buzz'
    >>> fizzbuzz(7)
    '7'
    """
    if n % 15 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return str(n)
