def count_title(letter):
    return letter.isupper()


ptr = input()
start, finish = int(input()), int(input())

print(len(list(filter(count_title, ptr[start-1:finish]))))
