from datetime import datetime
import functools


def logger(func):
    '''
    decorating function
    :param func: function to be decorated
    :return: converted function
    '''
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        '''
        converted function
        :param args: parameters of the function to be decorated
        :param kwargs: default parameters  of the function to be decorated
        :return: new result of the decorated function
        '''
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
