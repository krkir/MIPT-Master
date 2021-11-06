import itertools

print(*sorted(map(lambda x: x[0] + x[1], list(itertools.permutations(input(), 2)))))