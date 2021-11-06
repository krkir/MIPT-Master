import itertools

s, k = input().split()
count = 0
p = list(map(lambda x: "".join(x), list(itertools.permutations(s, int(k)))))
for i in p:
    if "t" in i:
        count += 1
print('%.3f'%(count/len(p)))