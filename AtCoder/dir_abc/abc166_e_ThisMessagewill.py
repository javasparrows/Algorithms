import sys
import collections
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

countL = []
countR = []
for i in range(N):
    countL.append(i - A[i])
    countR.append(i + A[i])

countL = collections.Counter(countL)
countR = collections.Counter(countR)

ans = sum([countL[i] * countR[i] for i in countL.keys()])
print(ans)
