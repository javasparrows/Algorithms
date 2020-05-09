N, X, Y = map(int, input().split())

X -= 1
Y -= 1
d = [0]*10000
for i in range(N):
    for j in range(i+1, N):
        c = min(j-i, abs(X-i) + 1 + abs(Y-j))
        d[c] += 1

for i in range(1, N):
    print(d[i])
