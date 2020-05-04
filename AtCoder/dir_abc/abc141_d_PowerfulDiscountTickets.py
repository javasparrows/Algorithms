import heapq
import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] *= -1
    
heapq.heapify(A)  # Aをheapに変換
for _ in range(M):
    x = heapq.heappop(A)  # Aの中の最小値を取り出して返す
    heapq.heappush(A, (-x//2)*-1)
    
print(-sum(A))