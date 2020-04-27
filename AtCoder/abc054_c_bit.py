# ビット演算を用いた方法

N, M = map(int, input().split())
g = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

memo = {}
All_used = (1 << N) - 1  # Nを2進数に変換


def dfs(v, used):
    if used == All_used:
        return 1

    key = (v, used)
    if key in memo:
        return memo[key]

    ans = 0
    for u in g[v]:
        if (used >> u) & 1 == 1:  # u番目のビットにフラグが立っているかどうかチェック
            continue

        used ^= (1 << u)  # u番目のビットのフラグを立てる。^はXOR
        ans += dfs(u, used)  # ここで再帰を回して、全ての頂点に辿れた分だけansに数が足される
        used ^= (1 << u)  # u番目のビットのフラグを戻す

    memo[key] = ans
    return ans


print(dfs(0, 1))
