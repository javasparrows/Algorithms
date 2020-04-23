# 深さ優先探索

N, M = map(int, input().split())
adj_matrix = [[0]*N for _ in range(N)]

# 隣接行列を作る
for i in range(N):
    a, b = map(int, input().split())
    adj_matrix[a-1][b-1] = 1
    adj_matrix[b-1][a-1] = 1


def dfs(v, used):
    if not False in used:
        return 1

    ans = 0
    for i in range(N):
      # vもiも0,1,,,N-1を通るので全通りを見れる
        if not adj_matrix[v][i]:
            continue
        if used[i]:
            continue

        # i=1以降を深く探索していく
        used[i] = True
        ans += dfs(i, used)
        # v=iで探索し終わったら次のiへ行く
        used[i] = False

    return ans


used = [False] * N
used[0] = True
print(dfs(0, used))
