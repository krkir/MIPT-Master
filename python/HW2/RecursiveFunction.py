def rf(n):
    if n < 40:
        result = n
    else:
        result = rf(n - 40) + rf(n - 20) + rf(n - 5) + rf(n - 1)
    return result

n = int(input())
print(rf(n))