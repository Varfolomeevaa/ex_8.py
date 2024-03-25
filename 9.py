import functools
import json
import yaml


def to_format(format=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result_python = func(*args, **kwargs)
            if format == 'yaml':
                result = yaml.dump(result_python)
            else:
                result = json.dumps(result_python)
            return result

        return wrapped

    return decorator


@to_format()
def finder(dct, num):
    find = {}
    for i in dct:
        if dct[i] == num:
            find[i] = num
    return find


@to_format('yaml')
def minimizer(lst_lst):
    mini = float('inf')
    mini_lst = []
    for i in range(len(lst_lst)):
        if len(lst_lst[i]) < mini:
            mini = len(lst_lst[i])
            mini_lst = lst_lst[i]
    return f'{mini_lst} has the minimum length. And it is {mini}'


dictionary = {'apple': 5, 'orange': 2, 'strawberry': 5, 'blueberry': 10}
print(finder(dictionary, 5))

print(minimizer([[1, 2, 4], [6, 7, 2], [8, 10, 12, 3], [1, 2]]))
