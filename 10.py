import functools
from datetime import datetime


def logger(tm, cnt):
    def decorator(func):
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
            time_first = datetime.now()
            result = func(*args, **kwargs)
            time_last = datetime.now()

            between = str(time_last - time_first)
            ind_comma = between.find('.')
            between = between[:ind_comma].split(':')
            between_int = int(between[0]) * 3600 + int(between[1]) * 60 + int(between[2])

            between_need = int(tm.split(':')[0]) * 3600 + int(tm.split(':')[1]) * 60 + int(tm.split(':')[2])

            wrapped.count += 1

            if wrapped.count >= cnt:
                raise Exception('CallsLimit')
            if between_int >= between_need:
                raise Exception('TimeLimit')
            else:
                return result

        wrapped.count = 0
        return wrapped

    return decorator
