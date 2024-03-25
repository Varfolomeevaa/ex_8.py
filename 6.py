import functools


def logger(func):
    @functools.wraps(func)
    def wrapped(variable):
        result = func(variable)
        return result

    return wrapped
