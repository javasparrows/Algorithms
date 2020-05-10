import itertools

N, M, X = map(int, input().split())
ca = []
for _ in range(N):
    ca.append(list(map(int, input().split())))

ns = [i for i in range(N)]
price = 1000000000000
for r in range(1, N+1):
    for v in itertools.combinations(ns, r):
        flag = True
        for j in range(M):
            s = sum([ca[i][j+1] for i in v])
            if s < X:
                flag = False
                continue
        if flag:
            p = sum([ca[i][0] for i in v])
            price = min(price, p)

if price == 1000000000000:
    print(-1)
else:
    print(price)
