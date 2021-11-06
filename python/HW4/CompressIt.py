import itertools

f = itertools.groupby(input())
for key, group in f:
    t = len(list(group))
    if t != 1:
        print(key, t, end="", sep="")
    else:
        print(key, end='', sep='')