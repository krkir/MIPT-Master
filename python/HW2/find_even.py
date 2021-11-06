def find_even(*args):
    result = []
    for i in args:
        if i % 2 == 0:
            result.append(i)
    if len(result) == 0:
        result = "Not found"
    return result

st = [int(i) for i in input().split()]
print(find_even(*st))



