N, M = list(map(int, input().split()))
X = list(map(int, input().split()))

X = sorted(X)
diffs = [X[i] - X[i-1] for i in range(1, len(X))]
diffs = sorted(diffs, reverse=True)

# 一番遠い距離から、2点間の距離の中から大きい順に引いていくだけ
res = X[-1] - X[0]
for i in range(min(len(diffs), N-1)):
    res -= diffs[i]

print(res)
