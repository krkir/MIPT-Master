def mean(sel):
    result = 0
    for i in sel:
        result += i
    result /= len(sel)
    return result


def statistics(sel: list, k: int):
    moment = 0
    m = mean(sel)
    for i in sel:
        moment += (i - m) ** k
    moment /= len(sel)
    return (m, moment)

sel = [int(i) for i in input().split()]
k = int(input())
print(*statistics(sel, k))