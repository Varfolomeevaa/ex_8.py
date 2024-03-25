from datetime import datetime
import functools


def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        filename = f'{func.__name__}_log.txt'
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            ex = type(ex).__name__
            with open(filename, 'a') as f:
                print(datetime.now(), ex, file=f)
            return 'Mistake!'

    return wrapped


@logger
def deli(a, b):
    return a / b


print(deli(1, 0))
