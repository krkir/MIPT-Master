def bank(money, years, interest):
    result = money * ((1 + interest/1200) ** (12 * years))
    return int(result)


M = float(input())
Y = float(input())
I = float(input())

print(bank(M, Y, I))