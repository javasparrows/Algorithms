N, K = map(int, input().split())
A = list(map(int, input().split()))

c = [0]*N
c[0] = 1
cc = [0]
i = 0
while True:
    c[A[i]-1] += 1  # 来た場所に1を足す
    cc.append(A[i]-1)
    if c[A[i]-1] > 1:
        memo = A[i]-1
        break
    i = A[i] - 1  # 次の場所

used = [i for i in range(N) if c[i] > 0]
pos = [i for i in range(len(cc)) if cc[i] == memo]
res = pos[1] - pos[0]
loop = [i for i in cc[pos[0]:pos[1]]]

if K < N:
    ans = cc[K]+1
else:
    i = (K - (pos[0])) % res
    ans = loop[i]+1

print(ans)
