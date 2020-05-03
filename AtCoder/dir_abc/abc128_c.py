import itertools

N, M = map(int, input().split())
k = []
for i in range(M):
    k.append(list(map(int, input().split())))
p = list(map(int, input().split()))
ks = [i[0] for i in k]
ss = [i[1:] for i in k]

prods = list(itertools.product([0, 1], repeat=N))
count = 0
for prod in prods:
    check = 0
    for i in range(M):
        s = ss[i]
        # sごとに
        n = sum([prod[j-1] for j in s])
        if n % 2 == p[i]:
            check += 1
    if check == M:
        count += 1
print(count)
