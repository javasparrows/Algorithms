K, N = map(int, input().split())
A = list(map(int, input().split()))

d = []
for i in range(N-1):
    d.append(A[i+1] - A[i])
d.append(K - A[-1] + A[0])

ans = sum(d) - max(d)

print(ans)
