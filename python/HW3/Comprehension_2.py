m, n = input().split()
eq = [(-i ** 5) - 5 * (i ** 4) + 8 * (i ** 3) + 12 * (i ** 2) + 30 * i + 11 for i in range(int(m), int(n)+1)]
print(min(eq))
