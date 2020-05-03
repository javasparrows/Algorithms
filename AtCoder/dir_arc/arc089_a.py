N = int(input())
L = []
for i in range(N):
    L.append([int(j) for j in input().split()])

times = [i[0] for i in L]
xs = [i[1:] for i in L]

x_move = [0, 0]
x1 = [1, 0]
x2 = [0, 1]
x3 = [-1, 0]
x4 = [0, -1]

# 距離を計算する関数
def prog(x_move, x, y):
    x0 = x_move[0]
    x1 = x_move[1]
    x_move = [x0+y[0], x1+y[1]]
    dist = (x[0]-x_move[0])**2 + (x[1]-x_move[1])**2
    return x_move, dist


ans = 'Yes'

times = [0] + times
for i, x in enumerate(xs):
    time_temp = times[i+1] - times[i]
    for j in range(time_temp):
        x1_next, dist1 = prog(x_move, x, x1)
        x2_next, dist2 = prog(x_move, x, x2)
        x3_next, dist3 = prog(x_move, x, x3)
        x4_next, dist4 = prog(x_move, x, x4)
        dists = [dist1, dist2, dist3, dist4]
        dist = min(dists)
        idx = dists.index(dist)
        x_nexts = [x1_next, x2_next, x3_next, x4_next]
        x_move = x_nexts[idx]
    if x_move != x:
        ans = 'No'
        break

print(ans)
