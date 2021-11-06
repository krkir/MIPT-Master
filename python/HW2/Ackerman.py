def ackerman(m, n):
    if m == 0:
        result = n + 1
    elif n == 0:
        result = ackerman(m-1, 1)
    else:
        result = ackerman(m-1, ackerman(m, n-1))
    return result


m = int(input())
n = int(input())
print(ackerman(m, n))