start, finish = int(input()), int(input())
not_multiple, ending = int(input()), int(input())

print(list(map(lambda x: x % not_multiple != 0 and x % 10 == ending, range(start, finish + 1))).count(True))
