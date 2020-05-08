W, H, N = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

xmax, xmin, ymax, ymin = W, 0, H, 0
for a in A:
    if a[2] == 1:
        xmin = max(xmin, a[0])
    if a[2] == 2:
        xmax = min(xmax, a[0])
    if a[2] == 3:
        ymin = max(ymin, a[1])
    if a[2] == 4:
        ymax = min(ymax, a[1])

S = (xmax-xmin) * (ymax-ymin)
if S < 0 or xmin > xmax or ymin > ymax:
    S = 0
print(S)
