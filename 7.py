import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwards):
        result_python = func(*args, **kwards)
        result_json = json.dumps(result_python)
        return result_json

    return wrapped


@to_json
def finder(dct, num):
    find = {}
    for i in dct:
        if dct[i] == num:
            find[i] = num
    return find


dictionary = {'apple': 5, 'orange': 2, 'strawberry': 5, 'blueberry': 10}
print(finder(dictionary, 5))


@to_json
def minimizer(lst_lst):
    mini = float('inf')
    mini_lst = []
    for i in range(len(lst_lst)):
        if len(lst_lst[i]) < mini:
            mini = len(lst_lst[i])
            mini_lst = lst_lst[i]
    return f'{mini_lst} has the minimum length. And it is {mini}'


print(minimizer([[1, 2, 4], [6, 7, 2], [8, 10, 12, 3], [1, 2]]))
