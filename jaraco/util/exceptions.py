from jaraco import context


def throws_exception(callable, *exceptions):
    """
    Return True if the callable throws the specified exception

    >>> throws_exception(lambda: int('3'))
    False
    >>> throws_exception(lambda: int('a'))
    True
    >>> throws_exception(lambda: int('a'), KeyError)
    False
    """
    with context.ExceptionTrap():
        with context.ExceptionTrap(*exceptions) as exc:
            callable()
    return bool(exc)
