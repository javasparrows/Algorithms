import heapq
from collections import deque


'''
キュー（queue, FIFO）として使う
'''
d = deque(['a', 'b', 'c'])
print(d)
# deque(['a', 'b', 'c'])

d.append('d')
print(d)
# deque(['a', 'b', 'c', 'd'])

print(d.popleft())
# a

print(d)
# deque(['b', 'c', 'd'])


'''
スタック（stack, LIFO）として使う
'''
d = deque(['a', 'b', 'c'])
print(d)
# deque(['a', 'b', 'c'])

d.append('d')
print(d)
# deque(['a', 'b', 'c', 'd'])

print(d.pop())
# d

print(d)
# deque(['a', 'b', 'c'])

print(heapq.heappush(d, -a))
# aを追加

print(heapq.heappop(d))
# 最小値を取る


'''
デック（deque, 両端キュー）として使う
'''
append(), appendleft(), pop(), popleft()