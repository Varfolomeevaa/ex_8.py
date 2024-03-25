import functools


def logger(func):
    '''
    decorating function
    :param func: function to be decorated
    :return: converted function
    '''
    @functools.wraps(func)
    def wrapped(variable):
        '''
        converted function
        :param variable: parameter of the function to be decorated
        :return: new result of the decorated function
        '''
        result = func(variable)
        return result

    return wrapped
