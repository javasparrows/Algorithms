import heapq

N = int(input())
v = list(map(int, input().split()))

heapq.heapify(v)

res = 0
for _ in range(N-1):
    a = heapq.heappop(v)
    b = heapq.heappop(v)
    res = (a+b)/2
    heapq.heappush(v, res)

print(res)
