W, H, x, y = map(int, input().split())

area = W*H

if x == W/2 and y == H/2:
    print(area/2, 1)
else:
    print(area/2, 0)