import functools
from datetime import datetime

'00:00:20'
def logger(tm, cnt):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
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
