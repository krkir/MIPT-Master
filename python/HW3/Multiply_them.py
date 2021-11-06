from functools import reduce
l = [-i if i % 3 == 0 else i for i in range(1, int(input())+1)]
print(reduce(lambda x, y: x * y, l))
