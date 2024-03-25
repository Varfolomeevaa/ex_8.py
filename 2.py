start, finish = int(input()), int(input())
multiple_1, multiple_2 = int(input()), int(input())

print(sum(list(filter(lambda x: x % multiple_1 == 0 and x % multiple_2 == 0, range(start, finish + 1)))))
