import numpy as np

N = int(input())
A = list(map(int, input().split()))
ans = [0]*N

A.append(0)

for i in range(0, N-1):
    ans[A[i]] += 1
for i in range(1, N):
    print(ans[i])
print(0)
