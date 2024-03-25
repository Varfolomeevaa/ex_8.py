import functools
import json


def to_json(func):
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
        result_python = func(*args, **kwargs)
        result_json = json.dumps(result_python)
        return result_json

    return wrapped


@to_json
def finder(dct, num):
    '''
    function to find dictionary keys whose values are equal to a certain number
    :param dct: dictionary in which to find
    :param num: the number in which to find
    :return: dictionary, where the desired key and its key value(num)
    '''
    find = {}
    for i in dct:
        if dct[i] == num:
            find[i] = num
    return find


dictionary = {'apple': 5, 'orange': 2, 'strawberry': 5, 'blueberry': 10}
print(finder(dictionary, 5))


@to_json
def minimizer(lst_lst):
    '''
    function to find a list with the minimum length
    :param lst_lst: a list containing the necessary lists
    :return: list with minimum length and what it equals in string format
    '''
    mini = float('inf')
    mini_lst = []
    for i in range(len(lst_lst)):
        if len(lst_lst[i]) < mini:
            mini = len(lst_lst[i])
            mini_lst = lst_lst[i]
    return f'{mini_lst} has the minimum length. And it is {mini}'


print(minimizer([[1, 2, 4], [6, 7, 2], [8, 10, 12, 3], [1, 2]]))
