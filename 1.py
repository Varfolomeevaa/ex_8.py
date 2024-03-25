def count_title(letter):
    '''
    function to determine whether a letter is capitalized
    :param letter: letter to check
    :return: test result in true or false format
    '''
    return letter.isupper()


ptr = input()
start, finish = int(input()), int(input())

print(len(list(filter(count_title, ptr[start-1:finish]))))
