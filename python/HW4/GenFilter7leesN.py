def filter7lessN(a, N):
    for i in a:
        if i < N and i % 7 == 0:
            yield i