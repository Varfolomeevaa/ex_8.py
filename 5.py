from functools import reduce

start, finish = int(input()), int(input())
multiple = int(input())
suit = list(filter(lambda x: x % multiple == 0 and x ** 0.5 == int(x ** 0.5), range(start, finish + 1)))


def multiply(first, second):
    '''
    function for multiplying numbers
    :param first: first multiplier
    :param second: second multiplier
    :return:
    '''
    return first * second


print(reduce(multiply, suit))
