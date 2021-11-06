with open("input.txt", "r") as f:
    m, n, k = [int(i) for i in f.readline().split()]
with open("output.txt", "w") as f1:
    for i in range(m, n+1):
        if i % k == 2:
            f1.write(str(i) + '\n')