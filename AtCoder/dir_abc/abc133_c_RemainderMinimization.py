L, R = map(int, input().split())

MOD = 2019

res = []
for i in range(L, min(L+MOD, R+1)):
    for j in range(i+1, min(L+MOD, R+1)):
        res.append((i*j) % MOD)
print(min(res))