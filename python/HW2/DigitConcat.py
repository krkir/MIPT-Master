def digit_concat(n: str, k: int):
    result = 0
    f = [int(n*(i+1)) for i in range(k)]
    for num in f:
        result += num
    return result


n = input()
k = int(input())
print(digit_concat(n, k))