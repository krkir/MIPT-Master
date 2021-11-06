m, n, k = input().split()
print(sum([i for i in range(int(m), int(n)+1) if i % int(k) == 2]))
