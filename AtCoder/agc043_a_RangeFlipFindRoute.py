H, W = map(int, input().split())
s = []
for _ in range(H):
    s.append(input())


def main(H, W, s):
    # 動的計画法

    INF = float('inf')
    dp = [[INF]*W for _ in range(H)]
    if s[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    dx = (1, 0)
    dy = (0, 1)
    for i in range(H):
        for j in range(W):
            for dir_ in range(2):  # 右に行くか下に行くかの2通り
                ni = i + dx[dir_]
                nj = j + dy[dir_]
                if ni >= H or nj >= W:
                    continue
                add = 0
                if s[ni][nj] == '#' and s[i][j] == '.':
                    add = 1
                dp[ni][nj] = min(dp[ni][nj], dp[i][j] + add)

    return dp[H-1][W-1]


print(main(H, W, s))
